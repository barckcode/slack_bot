# List of commands
def init_commands(app):
    @app.command("/echo")
    def repeat_text(ack, say, command):
        # Acknowledge command request
        ack()
        say(f"{command['text']}")


    @app.command("/help")
    def repeat_text(ack, say, command):
        # Acknowledge command request
        ack()
        say(
            blocks=[
                {
                    "type": "divider",
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Hola <@{command['user_name']}>!*, te dejo los comandos que tengo disponibles:"
                    },
                },
            ],
            text=f"Hey there <@{command['user_name']}>!"
        )
