import json
import watson_developer_cloud
import winsound

creds = {
  "url": "https://gateway.watsonplatform.net/assistant/api",
  "username": "5b230243-c6fa-410a-8d77-96f48e9e4661",
  "password": "7gNUHt4ooNzu"
}

assistant = watson_developer_cloud.AssistantV1(
    **creds,
    version='2018-07-10'
)

def send_message(txt):
    response = assistant.message(
        workspace_id='cbb8cec2-2155-4adb-ad3f-f29dd664eac1',
        input={"text": txt})
    return response['output']['text']

#print(json.dumps(response, indent=2))
