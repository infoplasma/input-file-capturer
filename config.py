config = {'#_Input_Additional_Impressions.xlsx':
              {'#': '%Y%m',
               'tabs':
                   {'Tabelle3':
                        {'tables':
                             {'AdditionalImpressions':
                                  {'usecols': 'B:C',
                                   'header': 2,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 3,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None
                                   },

                              }
                         }
                    }

               },
          'Bosch Social Data #.xlsx':
              {'#': '%Y%m',
               'tabs':
                   {'facebook_overview':
                        {'tables':
                             {'FbSocialOverview':
                                  {'usecols': 'A:L',
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 2,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'SALES_REGION', 'type': 'STRING'},
                                                 {'name': 'WEBSITE', 'type': 'STRING'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'TOTAL_IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'ORGANIC_IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'PAID_IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'CPM', 'type': 'FLOAT64'},
                                                 {'name': 'AD_SPENT', 'type': 'FLOAT64'},
                                                 {'name': 'TOTAL_ENGAGEMENT', 'type': 'INT64'},
                                                 {'name': 'ENGAGEMENT_RATE', 'type': 'FLOAT64'},
                                                 {'name': 'FAN_COUNT', 'type': 'INT64'},
                                                 {'name': 'UNIQUE_PAID_REACH', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None
                                   }
                              }
                         },
                    'facebook_fancount':
                        {'tables':
                             {'FbAccountFans':
                                  {'usecols': 'A:B',
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'PAGES', 'type': 'STRING'},
                                                 {'name': 'FANS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   }
                              }
                         },
                    'instagram_overview':
                        {'tables':
                             {'InstaSocialOverview':
                                  {'usecols': 'A:L',
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 1,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'SALES_REGION', 'type': 'STRING'},
                                                 {'name': 'WEBSITE', 'type': 'STRING'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'TOTAL_IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'ORGANIC_IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'PAID_IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'CPM', 'type': 'FLOAT64'},
                                                 {'name': 'AD_SPENT', 'type': 'FLOAT64'},
                                                 {'name': 'TOTAL_ENGAGEMENT', 'type': 'INT64'},
                                                 {'name': 'ENGAGEMENT_RATE', 'type': 'FLOAT64'},
                                                 {'name': 'FAN_COUNT', 'type': 'INT64'},
                                                 {'name': 'UNIQUE_PAID_REACH', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   },
                              }
                         }
                    }
               },
          'Mobile KPI #.xlsx':
              {'#': '%Y-%m',
               'tabs':
                   {'Total':
                        {'tables':
                             {'MobileInstallsToolbox':
                                  {'usecols': None,
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'MONTH', 'type': 'STRING'},
                                                 {'name': 'RATING__ANDROID__MONTHLY', 'type': 'FLOAT64'},
                                                 {'name': 'RATING__IOS__MONTHLY', 'type': 'FLOAT64'},
                                                 {'name': 'NO_OF_RATINGS_MONTHLY', 'type': 'INT64'},
                                                 {'name': 'NO_OF_REVIEWS_MONTHLY', 'type': 'INT64'},
                                                 {'name': 'RATING__ANDROID__TOTAL', 'type': 'FLOAT64'},
                                                 {'name': 'RATING__IOS__TOTAL', 'type': 'FLOAT64'},
                                                 {'name': 'NO_OF_RATINGS_TOTAL', 'type': 'INT64'},
                                                 {'name': 'NO_OF_REVIEWS_TOTAL', 'type': 'INT64'},
                                                 {'name': 'INSTALLS_ON_ACTIVE_DEVICES', 'type': 'FLOAT64'},
                                                 {'name': 'SESSIONS', 'type': 'STRING'},
                                                 {'name': 'MONTHLY_ACTIVE_USERS__MAU_', 'type': 'INT64'},
                                                 {'name': 'ACTIVE_USAGE_QUOTA', 'type': 'FLOAT64'},
                                                 {'name': 'NEW_USERS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   }
                              }},
                    'Sheet2':
                        {'tables':
                             {'MobileInstallsToolboxDetailed':
                                  {'usecols': 'B:C,E,G:H',
                                   'header': 0,
                                   'cols_to_drop': [],  # empty list if none
                                   'cols_to_ffill': [],
                                   'from_row': 0,  # FROM EXCEL INDEX 1 based
                                   'to_row': 0,  # FROM EXCEL index,,
                                   'bq_schema': [
                                       {'name': 'COUNTRY', 'type': 'STRING'},
                                       {'name': 'INSTALLS_ON_ACTIVE_DEVICES', 'type': 'FLOAT64'},
                                       {'name': 'USERS', 'type': 'INT64'},
                                       {'name': 'NEW_USERS', 'type': 'INT64'},
                                       {'name': 'SESSIONS', 'type': 'INT64'},
                                       {'name': 'DATE', 'type': 'DATE'}
                                   ]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   }
                              }
                         }
                    }
               },
          'PT-UMS-REA-Counts-SAO-NEW-#.xlsx':
              {'#': '%Y%m%d',
               'tabs':
                   {'PDH Data Summary REA NEW':
                        {'tables':
                             {'statusquo_user_SAO':
                                  {'usecols': 'A:F,H:I',
                                   'header': 7,  # SAME AS EXCEL ROW NUMBER
                                   'cols_to_drop': [],
                                   'cols_to_ffill': ['DELTA_TARGET__ACHIEVEMENT_LOCAL'],
                                   # not sure if i should fill those empty values
                                   'from_row': 9,  # SAME AS EXCEL
                                   'to_row': 13,  # SAME AS EXCEL
                                   'bq_schema': [{'name': 'REGION', 'type': 'STRING'},
                                                 {'name': 'R_SORT', 'type': 'INT64'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'ALL_DATA', 'type': 'INT64'},
                                                 {'name': 'CONSENT', 'type': 'INT64'},
                                                 {'name': 'CONSENT_PY', 'type': 'INT64'},
                                                 {'name': 'LOCAL_USER_CONSENT', 'type': 'INT64'},
                                                 {'name': 'DELTA_TARGET__ACHIEVEMENT_LOCAL', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'},
                                                 ]  # to automatically infer schema
                                   }
                              }
                         }
                    }
               },
          'PT-UMS-REA-Counts-South-Korea-NEW-#.xlsx':
              {'#': '%Y%m%d',
               'tabs':
                   {'PDH Data Summary REA NEW':
                        {'tables':
                             {'statusquo_user_southkorea':
                                  {'usecols': 'A:F,H:I',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': ['DELTA_TARGET__ACHIEVEMENT_LOCAL'],
                                   'from_row': 9,
                                   'to_row': 12,
                                   'bq_schema': [{'name': 'REGION', 'type': 'STRING'},
                                                 {'name': 'R_SORT', 'type': 'INT64'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'ALL_DATA', 'type': 'INT64'},
                                                 {'name': 'CONSENT', 'type': 'INT64'},
                                                 {'name': 'CONSENT_PY', 'type': 'INT64'},
                                                 {'name': 'LOCAL_USER_CONSENT', 'type': 'INT64'},
                                                 {'name': 'DELTA_TARGET__ACHIEVEMENT_LOCAL', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]  # to automatically infer schema
                                   },
                              'data_by_source_user_southkorea':
                                  {'usecols': 'K:M',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 12,
                                   'bq_schema': [{'name': 'DATA_BY_SOURCE', 'type': 'STRING'},
                                                 {'name': '_DATA_ALL_DATA', 'type': 'INT64'},
                                                 {'name': '_DATA_CONSENT', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]  # to automatically infer schema
                                   }
                              }
                         }
                    }
               },
          'PT-UMS-REA-Counts-Summary-NEW-#.xlsx':
              {'#': '%Y%m%d',
               'tabs':
                   {'PDH Data Summary REA NEW':
                        {'tables':
                             {'statusquo_user':
                                  {'usecols': 'A:F,H:I',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'REGION', 'type': 'STRING'},
                                                 {'name': 'R_SORT', 'type': 'INT64'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'ALL_DATA', 'type': 'INT64'},
                                                 {'name': 'CONSENT', 'type': 'INT64'},
                                                 {'name': 'CONSENT_PY', 'type': 'INT64'},
                                                 {'name': 'LOCAL_USER_CONSENT', 'type': 'INT64'},
                                                 {'name': 'DELTA_TARGET__ACHIEVEMENT_LOCAL', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}]  # to automatically infer schema
                                   },
                              'data_by_source_user':
                                  {'usecols': 'K:M',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'DATA_BY_SOURCE', 'type': 'STRING'},
                                                 {'name': '_DATA_ALL_DATA', 'type': 'STRING'},
                                                 {'name': '_DATA_CONSENT', 'type': 'STRING'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]  # to automatically infer schema
                                   }
                              }
                         }
                    }
               },
          'Reach_Marketing Cloud_#.xlsx':  # THE COLUMNS HAVE BEEN CHANGED HERe, I WILL USE THE LAST FILE AS TEMPLATE!!!
              {'#': '%Y-%m-%d',
               'tabs':
                   {'PTEU Campaign Report':
                        {'tables':
                             {'Reach_Marketing Cloud':
                                  {'usecols': 'A:F',
                                   'header': 0,  # default
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,  # default, header on top
                                   'to_row': 0,  # this file have variable number of rows
                                   'bq_schema': [{'name': 'REGION', 'type': 'STRING'},
                                                 {'name': 'MEASURES', 'type': 'STRING'},
                                                 {'name': 'MONTH', 'type': 'STRING'},
                                                 {'name': 'SENT_MESSAGES', 'type': 'INT64'},
                                                 {'name': 'OPENED_MESSAGE_RATE', 'type': 'FLOAT64'},
                                                 {'name': 'CTR', 'type': 'FLOAT64'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]  # to automatically infer schema
                                   }
                              }
                         }
                    }
               },
          'SAO_Reach_Marketing Cloud_#.xlsx':
              {'#': '%Y-%m-%d',
               'tabs':
                   {'Sheet1':
                        {'tables':
                             {'SAO_Reach_Marketing Cloud':
                                  {'usecols': 'A:F',  # all cols
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'REGION', 'type': 'STRING'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'MONTH', 'type': 'STRING'},
                                                 {'name': 'SENT_EMAILS', 'type': 'FLOAT64'},
                                                 {'name': 'OPEN_RATE__PERCENT', 'type': 'FLOAT64'},
                                                 {'name': 'CLICK_RATE__PERCENT', 'type': 'STRING'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]
                                   }
                              }
                         }
                    }
               },
          'Video _ Youtube Crafstmen #.xlsx':  # the filename has been changed. using the latest
              {'#': '%Y',
               'tabs':
                   {'Sheet1':
                        {'tables':
                             {'YTCraftsman':
                                  {'usecols': None,
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0,
                                   'bq_schema': [{'name': 'SALES_REGION', 'type': 'STRING'},
                                                 {'name': 'WEBSITE', 'type': 'STRING'},
                                                 {'name': 'COUNTRY', 'type': 'STRING'},
                                                 {'name': 'YOUTUBE', 'type': 'STRING'},
                                                 {'name': '_YT_ESTIMATED_NUMBER_OF_ONLINE_CRAFTSMENS_PER_COUNTRY',
                                                  'type': 'INT64'},
                                                 {'name': '_YT__PERCENT_OF_CRAFTSMENS_REACHED_YTD__', 'type': 'STRING'},
                                                 {'name': '_VIDEO_ESTIMATED_NUMBER_OF_ONLINE_CRAFTSMENS_PER_COUNTRY',
                                                  'type': 'INT64'},
                                                 {'name': '_VIDEO__PERCENT_OF_CRAFTSMENS_REACHED_YTD__',
                                                  'type': 'STRING'},
                                                 {'name': 'DATE', 'type': 'DATE'}, ]
                                   }
                              }
                         }
                    }
               },

          # ------- USE THIS AS TEMPLATE ----------
          '#<filename>.xlsx':  # the `#` is the placeholder for the DATE, must me in the same position as in the filename
              {'#': '%Y%m',
               'tabs':
                   {'<TAB_NAME1>':
                        {'tables':
                             {'<TABLE_ID1>':
                                  {'usecols': 'A:Z',  # None, o auto select them all
                                   'header': 0,  # will take the first row as the header
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 1,  # 0 to autoselect them all. same index as excel, 1-based
                                   'to_row': 10,  # 0 to aoutselect them all. same index as excel, 1-based
                                   'bq_schema': None
                                   },
                              '<TABLE_ID2>':
                                  {'usecols': 'A:Z',
                                   'header': 0,
                                   'cols_to_drop': [''],
                                   'cols_to_ffill': [''],
                                   'from_row': 1,
                                   'to_row': 10,
                                   'bq_schema': None  # to automatically infer schema
                                   }
                              }},
                    '<TAB_NAME2>':
                        {'tables':
                             {'<TABLE_ID1>':
                                  {'usecols': 'A:Z',
                                   'header': 0,
                                   'cols_to_drop': [''],
                                   'cols_to_ffill': [''],
                                   'from_row': 1,
                                   'to_row': 10,
                                   'bq_schema': None  # to automatically infer schema
                                   },
                              '<TABLE_ID2>':
                                  {'usecols': 'A:Z',
                                   'header': 0,
                                   'cols_to_drop': [''],
                                   'cols_to_ffill': [''],
                                   'from_row': 1,
                                   'to_row': 10,
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   }
                              }
                         }
                    }
               }
          }
