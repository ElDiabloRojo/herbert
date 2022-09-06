from slack import WebClient
from herbert import Herbert
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new CoinBot
herbert = Herbert("#general")

# Get the onboarding message payload
message = herbert.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)