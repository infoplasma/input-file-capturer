config = {'#_Input_Additional_Impressions.xlsx':
              {'#': '%Y%m',
               'tabs':
                   {'Tabelle3':
                        {'tables':
                             {'InputAdditionalImpressions':
                                  {'usecols': 'B:C',
                                   'header': 2,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 3,
                                   'to_row': 0
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
                             {'Social_fb_overview':
                                  {'usecols': 'A:L',
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 2,
                                   'to_row': 20
                                   }
                              }
                          },
                    'facebook_fancount':
                        {'tables':
                             {'Social_fb_fancount ':
                                  {'usecols': 'A:B',
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0,
                                   }
                              }
                         },
                      'instagram_overview':
                        {'tables':
                             {'Social_ig_overview  ':
                                  {'usecols': 'A:L',
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 1,
                                   'to_row': 10,
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
                             {
                                 'Toolbox':
                                  {'usecols': 'A:Z',
                                   'header': 0,
                                   'cols_to_drop': ['UNNAMED:_14'],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0
                                   }
                              }},
                    'Sheet2':
                        {'tables':
                             {'Toolbox_detailed':
                                  {'usecols': 'A:C',
                                   'header': 0,
                                   'cols_to_drop': [],  # empty list if none
                                   'cols_to_ffill': [],
                                   'from_row': 1,  # FROM EXCEL INDEX 1 based
                                   'to_row': 24  # FROM EXCEL index,
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
                                   'header': 7, # SAME AS EXCEL
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,  # SAME AS EXCEL
                                   'to_row': 13  # SAME AS EXCEL
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
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 12
                                   },
                              'data_by_source_user_southkorea':
                                  {'usecols': 'K:M',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 12
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
                                   'to_row': 35
                                   },
                              'data_by_source_user':
                                  {'usecols': 'K:M',
                                   'header': 7,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 9,
                                   'to_row': 17
                                   }
                              }
                         }
                    }
               },
          'Reach_Marketing Cloud_#.xlsx':
              {'#': '%Y-%m-%d',
               'tabs':
                   {'Sent Emails - Previous Month':
                        {'tables':
                             {'Reach_Marketing Cloud':
                                  {'usecols': 'A:E',
                                   'header': 0,  # default
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,   # default, header on top
                                   'to_row': 0
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
                                   'to_row': 0
                                   }
                              }
                         }
                    }
               },
          'Video _ Youtube Crafstmen #  (Temporary).xlsx':
              {'#': '%Y',
               'tabs':
                   {'Sheet1':
                        {'tables':
                             {'yt_craftsmen':
                                  {'usecols': None,
                                   'header': 0,
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 0,
                                   'to_row': 0
                                   }
                              }
                         }
                    }
               },
          '#<filename>.xlsx': # the `#` is the placeholder for the DATE
              {'#': '%Y%m',
               'tabs':
                   {'<TAB_NAME1>':
                        {'tables':
                             {'<TABLE_ID1>':
                                  {'usecols': 'A:Z', # None, o auto select them all
                                   'header': 0,     # will take the first row as the header
                                   'cols_to_drop': [],
                                   'cols_to_ffill': [],
                                   'from_row': 1,   # 0 to autoselect them all. same index as excel, 1-based
                                   'to_row': 10     # 0 to aoutselect them all. same index as excel, 1-based
                                   },
                              '<TABLE_ID2>':
                                  {'usecols': 'A:Z',
                                   'header': 0,
                                   'cols_to_drop': [''],
                                   'cols_to_ffill': [''],
                                   'from_row': 1,
                                   'to_row': 10
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
                                   },
                              '<TABLE_ID2>':
                                  {'usecols': 'A:Z',
                                   'header': 0,
                                   'cols_to_drop': [''],
                                   'cols_to_ffill': [''],
                                   'from_row': 1,
                                   'to_row': 10,
                                   }
                              }
                         }
                    }
               }
          }
