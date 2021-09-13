import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Internal modules
from commands.help import help_command
from commands.pullall import pullall_command
from commands.download_file import dowload_file_command


# Init Bolt
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN")
)

# Commands List
help_command(app)
pullall_command(app)
dowload_file_command(app)


# Start App
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
