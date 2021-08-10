import subprocess

# List of commands
def init_commands(app):
    @app.command("/help")
    def help_command(ack, say, command):
        # Acknowledge command request
        ack()
        say(
            blocks=[
                {
                    "type": "divider",
                },
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Comandos de R2D2"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Hola <@{command['user_name']}>*, te dejo los comandos que tengo disponibles:"
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "- */echo* [text]: Comando que responde con lo que hayas escrito"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "- */rollback* [application]: Comando para dar marcha atrás tras un deploy en PROD"
                    }
                },
                {
                    "type": "divider",
                },
            ],
            text=f"Help by <@{command['user_name']}>!"
        )


    @app.command("/rollback")
    def rollback_command(ack, say, command):
        # Acknowledge command request
        ack()

        script_output = subprocess.call(["echo", f"{command['text']}"])
        print(script_output)

        say(
            blocks=[
                {
                    "type": "divider",
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{command['text']}"
                    },
                },
                {
                    "type": "divider",
                },
            ],
            text=f"Rollback by <@{command['user_name']}>!"
        )
