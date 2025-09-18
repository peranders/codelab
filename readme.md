Create and activate a python virtual env:
```
python -m venv .venv-agent
source .venv-agent/bin/activate
```

Install google adk:
```
pip install google-adk
```



Create a bucket for the staging environment needed for deployment.

Create a .env file like below for both folders 

`adk_to_agent_engine-us-central1` :
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<YOUR PROJECT>
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.5-flash
STAGING_BUCKET=gs://<YOUR BUCKET>
APP_NAME=myagent-us-central1
```

`adk_to_agent_engine-europe-west1`:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<YOUR PROJECT>
GOOGLE_CLOUD_LOCATION=europe-west1
MODEL=gemini-2.5-flash
STAGING_BUCKET=gs://<YOUR BUCKET>
APP_NAME=myagent-europe-west1
```

Fill in with project_id and your bucket name

cd to the respective folders.

To deploy: ```deploy.sh``` 

To run: ```run.sh```




