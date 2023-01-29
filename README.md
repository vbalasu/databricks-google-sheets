# databricks-google-sheets

Interact with Google Sheets from Databricks. 

Please follow these steps. Be sure to replace all {{PLACEHOLDERS}} with appropriate values:

1. Create a spreadsheet in Google Sheets, and note the spreadsheet_id (You can get this from the URL)
2. Go to console.cloud.google.com and create a new project (OR select an existing project)
3. Within this project, create a service account [IAM & Admin --> Service Accounts --> Create], and call it `databricks-google-sheets`. You can skip the optional steps
4. Note down the email address associated with your new service account. Eg. `databricks-google-sheets@{{MY-AWESOME-PROJECT}}.iam.gserviceaccount.com`
5. Switch to the Keys tab and create a new key. Choose JSON as the Key type. This will generate a JSON file and download it locally
6. On your local machine, use the Databricks CLI to create a new secret scope. Eg. `databricks secrets create-scope --scope databricks-google-sheets --profile DEFAULT`
7. Create a new secret within the newly created secret scope. Eg. `databricks secrets put --scope databricks-google-sheets --key "databricks-google-sheets@{{MY-AWESOME-PROJECT}}.iam.gserviceaccount.com" --binary-file {{PATH-TO-JSON-FILE-FROM-STEP-5}} --profile DEFAULT`
8. Share your Google Sheet with the user `databricks-google-sheets@{{MY-AWESOME-PROJECT}}.iam.gserviceaccount.com`, and give Editor privileges



### Usage within Databricks Python notebook

```python
from databricks_google_sheets import DatabricksGoogleSheets
dgs = DatabricksGoogleSheets(dbutils)  # Pass in dbutils from the global scope of your Databricks runtime


# OPTION 1 - Create a Pandas dataframe from a Spark SQL query in Python
df = spark.sql("SELECT 'Hello from databricks-google-sheets' greeting;").toPandas()

# OPTION 2 - Create a dataframe directly in Pandas
import pandas as pd
df = pd.DataFrame({'greeting': ['Hello from databricks-google-sheets']})

# Write this dataframe to Google Sheets
dgs.df_to_sheets(df, spreadsheet_id='{{SPREADSHEET-ID-FROM-STEP-1}}', sheet_name='test', 
    dbsecret_scope='databricks-google-sheets', dbsecret_key='databricks-google-sheets@{{MY-AWESOME-PROJECT}}.iam.gserviceaccount.com')

# Read from Google Sheets into a new dataframe
newdf = dgs.sheets_to_df(spreadsheet_id='{{SPREADSHEET-ID-FROM-STEP-1}}', sheet_name='test', 
    dbsecret_scope='databricks-google-sheets', dbsecret_key='databricks-google-sheets@{{MY-AWESOME-PROJECT}}.iam.gserviceaccount.com')

# Compare the new dataframe to the original to ensure they are the same
assert df.equals(newdf) == True
```
