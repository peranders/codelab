source .env_eu
adk deploy agent_engine myagent --project $GOOGLE_CLOUD_PROJECT --region $GOOGLE_CLOUD_LOCATION --display_name $APP_NAME --staging_bucket $STAGING_BUCKET

