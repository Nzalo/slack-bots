# This program needs to be started with the listed environment variables

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hola")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"hola, <@{message['user']}>!")

@app.message("que tal?")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"muy bien, <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
