def help_command(app):
    @app.command("/help")
    def help(ack, say, command):
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
                        "text": "- */pullAll*: Comando para hacer pull de todas las aplicaciones que hay en sauron"
                    }
                },
                {
                    "type": "divider",
                },
            ],
            text=f"Help by <@{command['user_name']}>!"
        )
