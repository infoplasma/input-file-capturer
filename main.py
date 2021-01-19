from datetime import datetime
from config import config as cfg
from google.cloud import storage, bigquery
import pandas as pd
import re


# project configuration
PROJECT_ID = 'bosch-dashboard-295910'
BUCKET_NAME = 'file-uploader_vol'

# object instantiation
storage_client = storage.Client(PROJECT_ID)
bucket = storage_client.get_bucket(BUCKET_NAME)


def get_data(fname_with_date):
    """ Scan the configuration data based on the entered filename, if match, the corresponding config data is loaded

    :param fname_with_date:
    :return: dict with config data, or error if no match found.
    """
    regex_pattern_for_date = '\d{4}-?\d?-?\d?-?\d?\d?'
    try:
        extracted_date = re.findall(regex_pattern_for_date, fname_with_date)[0]
        file_cfg_index = fname_with_date.replace(extracted_date, "#")

        date_format = cfg[file_cfg_index]['#']

        data_file_completa = datetime.strptime(extracted_date, date_format)
        Y = data_file_completa.year
        m = data_file_completa.month
        d = data_file_completa.day
        data = {'index': file_cfg_index, 'Y': Y, 'm': m, 'd': d, 'iso8601': str(data_file_completa.date())}
        return data
    except IndexError as e:
        print(f"ERR {e}: FILENAME {fname_with_date} DOES NOT MATCH EXISTING FILE PATTERNS.")


def list_blobs(bucket_name=BUCKET_NAME):
    """Lists all the blobs in the bucket."""

    # Note: Client.list_blobs requires at least package version 1.17.0.
    return [blob.name for blob in storage_client.list_blobs(bucket_name)]


def get_raw_df(f, sheet_name=None) -> pd.DataFrame:
    if not sheet_name:
        sheet_name = list(f['tabs'].keys())[0]
    return pd.read_excel(f"gs://file-uploader_vol/{f['name']}", sheet_name=sheet_name)


def rename_cols_for_bq(df):
    """ rename columns to comply with BQ naming standard """
    df.columns = [c.upper().replace(" ", "_") for c in df.columns]
    df.columns = [c.upper().replace("-", "_") for c in df.columns]
    df.columns = [c.upper().replace("*", "_") for c in df.columns]
    df.columns = [re.sub(r'[()]', '_', c) for c in df.columns]
    df.columns = [re.sub(r'\n', '_', c) for c in df.columns]
    df.columns = [c.upper().replace("%", "_PERCENT") for c in df.columns]


def delete_data_if_date_exists(fname):
    client = bigquery.Client(project=PROJECT_ID)
    data = get_data(fname)
    date = data['iso8601']
    file_id = data['index']
    tabs = list(cfg[file_id]['tabs'].keys())
    for tab in tabs:
        tables = list(cfg[file_id]['tabs'][tab]['tables'].keys())
        for table in tables:
            return client.query(f'''DELETE FROM `{PROJECT_ID}.manual_input_files.{table}` WHERE DATE="{date}"''')


def preview(fname):
    """

    :param fname: string containing
    :return: dict. keys are the big query table names. values are the table contents.
    """
    change_list = {}
    data = get_data(fname)
    index = data['index']
    iso = data['iso8601']
    tabs = list(cfg[index]['tabs'].keys())
    print("================================================================")
    print(f"DATA: {data}")
    print(f"CONFIG: {cfg[index]}")

    for tab in tabs:
        print(f"TABS: {cfg[index]['tabs'][tab]}")
        tables = list(cfg[index]['tabs'][tab]['tables'].keys())
        print(f"TABLES: {tables}")
        for table in tables:
            change_list[table] = {}
            print("------------------------------------------------------------")
            usecols = cfg[index]['tabs'][tab]['tables'][table]['usecols']
            header = cfg[index]['tabs'][tab]['tables'][table]['header']
            if not header:  # to match excel inedxing in the configuration file
                header = 1

            cols_to_drop = cfg[index]['tabs'][tab]['tables'][table]['cols_to_drop']
            cols_to_ffill = cfg[index]['tabs'][tab]['tables'][table]['cols_to_ffill']

            from_row = cfg[index]['tabs'][tab]['tables'][table]['from_row']
            if from_row:
                from_row -= header  # offset if not zero
            to_row = cfg[index]['tabs'][tab]['tables'][table]['to_row']
            if to_row:
                to_row -= header  # offset if not zero
            # offset
            df = {}
            df = pd.read_excel(f"gs://file-uploader_vol/{fname}", sheet_name=tab, header=header-1, usecols=usecols, dtype=object)
            df['Date'] = f'{iso}'
            rename_cols_for_bq(df)
            # --- drop col
            if len(cols_to_drop):
                df.drop(cols_to_drop, axis=1, inplace=True)
            # --- fill col
            if len(cols_to_ffill):
                for col in cols_to_ffill:
                    df[col] = df[col].fillna(method='ffill')
            # --- skip rows
            if from_row and to_row:
                df = df[from_row-1:to_row]   # skipping the totals surmmary row (1st row below the header! :S)
            if from_row and not to_row:
                df = df[from_row - 1:]

            print(f"SHOWING FILE: {fname} - TAB: {tab} - TABLE: {table}")
            print("HEAD")
            print("----")
            print(df.head(2).to_string())
            print("TAIL")
            print("----")
            print(df.tail(2).to_string())
            change_list[table]['data'] = df
            change_list[table]['bq_schema'] = cfg[index]['tabs'][tab]['tables'][table]['bq_schema']

    return change_list


def push_to_bq(df, table_id, schema=None):
    df.to_gbq(f'manual_input_files.{table_id}', project_id=PROJECT_ID, if_exists='append', table_schema=schema)
    print("Ok")


def commit(change_list):
    for table_id in change_list.keys():
        push_to_bq(change_list[table_id]['data'], table_id, change_list[table_id]['bq_schema'])


# [START functions_helloworld_storage]
def gcs_function_hook(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.
    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """
    ACTIVATE = True  # set as ENV vars later
    DELETE_IF_DATE_EXISTS = True

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))

    fname = event['name']
    if DELETE_IF_DATE_EXISTS:
        delete_data_if_date_exists(fname)

    changes = preview(fname)

    if ACTIVATE:
        commit(changes)
    else:
        for table_id in changes.keys():
            print(f"TEST: WRITING ON TABLE: {table_id}")
            print(F"data: {changes[table_id]}")


# [END functions_helloworld_storage]


if __name__ == '__main__':
    preview('Mobile KPI 2020-08.xlsx')

