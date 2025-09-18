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

Create two .env file like below for and put them in the `adk_to_agent_engine/` folder. 

Name them .env-us and .env-eu.



`.env_us` 
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<YOUR PROJECT>
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.5-flash
STAGING_BUCKET=gs://<YOUR BUCKET>
APP_NAME=myagent-us-central1
```

`.env_eu`:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=<YOUR PROJECT>
GOOGLE_CLOUD_LOCATION=europe-west1
MODEL=gemini-2.5-flash
STAGING_BUCKET=gs://<YOUR BUCKET>
APP_NAME=myagent-europe-west1
```

Fill in with **project_id** and your **bucket name**


`cd adk_to_agent_engine/`

To deploy: ```deploy_us.sh``` or ```deploy_eu.sh``` 

To run: ```run_us.sh``` or ```run_eu .sh```




