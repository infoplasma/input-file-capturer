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
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
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
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
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
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
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
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
                                   # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   }
                              }},
                    'Sheet2':
                        {'tables':
                             {'MobileInstallsToolboxDetailed':
                                  {'usecols': None,
                                   'header': 0,
                                   'cols_to_drop': [],  # empty list if none
                                   'cols_to_ffill': [],
                                   'from_row': 0,  # FROM EXCEL INDEX 1 based
                                   'to_row': 0,  # FROM EXCEL index,,
                                   'bq_schema': [{'name': 'CHANNEL', 'type': 'STRING'},
                                                 {'name': 'IMPRESSIONS', 'type': 'INT64'},
                                                 {'name': 'DATE', 'type': 'STRING'}]
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
                                  {'usecols': 'A:I',
                                   'header': 7,  # SAME AS EXCEL ROW NUMBER
                                   'cols_to_drop': [],
                                   'cols_to_ffill': ['DELTA_TARGET__ACHIEVEMENT_LOCAL'],
                                   # not sure if i should fill those empty values
                                   'from_row': 9,  # SAME AS EXCEL
                                   'to_row': 13,  # SAME AS EXCEL
                                   'bq_schema': None  # to automatically infer schema
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
                                   'bq_schema': None  # to automatically infer schema
                                   },
                              'data_by_source_user_southkorea':
                                  {'usecols': 'K:M',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 12,
                                   'bq_schema': None  # to automatically infer schema
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
                                   'bq_schema': None  # to automatically infer schema
                                   },
                              'data_by_source_user':
                                  {'usecols': 'K:M',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 0,
                                   'bq_schema': None  # to automatically infer schema
                                   }
                              }
                         }
                    }
               },
          'Reach_Marketing Cloud_#.xlsx':  # THE COLUMNS HAVE BEEN CHANGED HERe, I WILL USE THE LAST FILE AS TEMPLATE!!!
              {'#': '%Y-%m-%d',
               'tabs':
                   {'Sent Emails - Previous Month':
                        {'tables':
                             {'Reach_Marketing Cloud':
                                  {'usecols': None,
                                   'header': 0,  # default
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,  # default, header on top
                                   'to_row': 0,  # this file have variable number of rows
                                   'bq_schema': None  # to automatically infer schema
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
                                  {'usecols': None,  # all cols
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0,
                                   'bq_schema': None  # to automatically infer schema
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
                                   'bq_schema': None  # to automatically infer schema
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
                                   'to_row': 10  # 0 to aoutselect them all. same index as excel, 1-based
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
                                                 {'name': 'DATE', 'type': 'STRING'}]  # [{'name':'col_name', 'type': 'STRING'}, {'name':'col_name', 'type': 'INT64'}, {'name':'col_name', 'type': 'FLOAT64'}, {'name':'col_name', 'type': 'NUMERIC'}, {'name':'col_name', 'type': 'DATE'}, {'name':'col_name', 'type': 'DATETIME'}, ... ] use big query types OR None

                                   }
                              }
                         }
                    }
               }
          }
