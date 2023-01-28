def sheets_to_df(spreadsheet_id, sheet_name, dbsecret_scope, dbsecret_key):
  # Service account credentials should be stored under the specified Databricks Secrets scope and key
  # This service account should be granted access to read/write the spreadsheet in the Sheets UI
  service_account_key = dbutils.secrets.get(scope=dbsecret_scope, key=dbsecret_key)
  import tempfile
  import pandas as pd
  from gspread_pandas import Spread, conf
  with tempfile.NamedTemporaryFile() as t:
    with open(t.name, 'w') as f:
      f.write(service_account_key)
    spread = Spread(spreadsheet_id, config=conf.get_config(file_name=t.name))
    return spread.sheet_to_df(sheet=sheet_name)

def df_to_sheets(df, spreadsheet_id, sheet_name, dbsecret_scope, dbsecret_key):
  # Service account credentials should be stored under the specified Databricks Secrets scope and key
  # This service account should be granted access to read/write the spreadsheet in the Sheets UI
  service_account_key = dbutils.secrets.get(scope=dbsecret_scope, key=dbsecret_key)
  import tempfile
  import pandas as pd
  from gspread_pandas import Spread, conf
  with tempfile.NamedTemporaryFile() as t:
    with open(t.name, 'w') as f:
      f.write(service_account_key)
    spread = Spread(spreadsheet_id, config=conf.get_config(file_name=t.name))
    return spread.df_to_sheet(df, sheet=sheet_name, replace=True, index=False)