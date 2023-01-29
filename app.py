#from databricks_google_sheets import df_to_sheets, sheets_to_df
from databricks_google_sheets import DatabricksGoogleSheets
dgs = DatabricksGoogleSheets(dbutils)  # Pass in dbutils from the global scope of your Databricks runtime

# OPTION 1 - Create a Pandas dataframe from a Spark SQL query in Python
df = spark.sql("SELECT 'Hello from databricks-google-sheets' greeting;").toPandas()

# OPTION 2 - Create a dataframe directly in Pandas
import pandas as pd
df = pd.DataFrame({'greeting': ['Hello from databricks-google-sheets']})

# Write this dataframe to Google Sheets
dgs.df_to_sheets(df, spreadsheet_id='1V0TdAayYbiHo0PVscPbPha_2Tc2dBLEZ6L6b8d8PFwc', sheet_name='test', 
    dbsecret_scope='databricks-google-sheets', dbsecret_key='databricks-google-sheets@fe-dev-sandbox.iam.gserviceaccount.com')

# Read from Google Sheets into a new dataframe
newdf = dgs.sheets_to_df(spreadsheet_id='1V0TdAayYbiHo0PVscPbPha_2Tc2dBLEZ6L6b8d8PFwc', sheet_name='test', 
    dbsecret_scope='databricks-google-sheets', dbsecret_key='databricks-google-sheets@fe-dev-sandbox.iam.gserviceaccount.com')

# Compare the new dataframe to the original to ensure they are the same
assert df.equals(newdf) == True