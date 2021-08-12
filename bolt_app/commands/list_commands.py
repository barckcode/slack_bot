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
                        "text": "- */pullAll*: Comando para hacer pull de todas las aplicaciones que hay en sauron"
                    }
                },
                {
                    "type": "divider",
                },
            ],
            text=f"Help by <@{command['user_name']}>!"
        )


    @app.command("/pullAll")
    def pullall_command(ack, say, command):
        # Acknowledge command request
        ack()

        script_output = subprocess.call([
            "ansible-playbook",
            "-t",
            "pullall",
            "r2d2.yml"
        ])
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
                        "text": f"Salida del comando: {script_output}"
                    },
                },
                {
                    "type": "divider",
                },
            ],
            text=f"PullAll by <@{command['user_name']}>!"
        )
