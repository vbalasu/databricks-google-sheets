# databricks-google-sheets

Store the secret as follows, using the databricks cli

```bash
databricks secrets put --scope vbalasu --key "partner-enablement@fe-dev-sandbox.iam.gserviceaccount.com" --binary-file chalicelib/google_secret.json --profile azure```