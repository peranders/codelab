import os
from dotenv import load_dotenv
import logging
import json
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler

import vertexai
from vertexai import agent_engines

# Load environment variables and initialize Vertex AI
load_dotenv()
project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
location = os.environ["GOOGLE_CLOUD_LOCATION"]
app_name = os.environ.get("APP_NAME")
bucket_name = os.environ.get("STAGING_BUCKET")

print(f"Using project_id: {project_id}, location: {location}, app_name: {app_name}, bucket_name: {bucket_name}")


# Initialize Google Cloud Logging with the correct project ID
cloud_logging_client = google.cloud.logging.Client(project=project_id)
handler = CloudLoggingHandler(cloud_logging_client, name=app_name)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)

# Initialize Vertex AI with the correct project and location
vertexai.init(
    project=project_id,
    location=location,
    staging_bucket=bucket_name,
)

# Filter agent engines by the app name in .env
ae_apps = agent_engines.list(filter=f'display_name="{app_name}"')
remote_app = next(ae_apps)

print(f"Using remote app: {remote_app.display_name}")


#schema = remote_app.operation_schemas()
#print("Operation schemas:")
#print(json.dumps(schema, indent=2))

# Get a session for the remote app
remote_session = remote_app.create_session(user_id="u_456")

my_message = "Give me a receipe for a pizza."
# Run the agent with this hard-coded input
events = remote_app.stream_query(
    user_id="u_456",
    session_id=remote_session["id"],
    message=my_message,
)

print("Agent response:")

#for event in remote_app.stream_query(
#    user_id="u_456",
#    message=my_message,
#):
#  print(event)


# Print responses
for event in events:
    print("Event:")
    for part in event["content"]["parts"]:
        if "text" in part:
            response_text = part["text"]
            print("[remote response]", response_text)
            logging.info("[remote response] " + response_text)



cloud_logging_client.flush_handlers()