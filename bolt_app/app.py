import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Internal modules
from commands.list_commands import init_commands


# Init Bolt
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN")
)


init_commands(app)


# Start App
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
