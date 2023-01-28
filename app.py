from databricks_google_sheets import df_to_sheets, sheets_to_df
import pandas as pd

# Create a test dataframe
df = pd.DataFrame({'greeting': ['Hello from databricks-google-sheets']})

# Write this dataframe to Google Sheets
df_to_sheets(df, spreadsheet_id='1V0TdAayYbiHo0PVscPbPha_2Tc2dBLEZ6L6b8d8PFwc', sheet_name='test', 
    dbsecret_scope='vbalasu', dbsecret_key='partner-enablement@fe-dev-sandbox.iam.gserviceaccount.com')

# Read from Google Sheets into a new dataframe
newdf = sheets_to_df(spreadsheet_id='1V0TdAayYbiHo0PVscPbPha_2Tc2dBLEZ6L6b8d8PFwc', sheet_name='test', 
    dbsecret_scope='vbalasu', dbsecret_key='partner-enablement@fe-dev-sandbox.iam.gserviceaccount.com')

# Compare the new dataframe to the original to ensure they are the same
assert df.equals(newdf) == True