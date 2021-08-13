import subprocess


def pullall_command(app):
    @app.command("/pullall")
    def pullall(ack, say, command):
        # Acknowledge command request
        ack()

        script_output = subprocess.call(["/usr/local/bin/ansible_bot", "-t", "pullall", "r2d2.yml"])
        print(script_output)

        if script_output == 0:
            say(
                blocks=[
                    {
                        "type": "divider",
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"@{command['user_name']} Se ha hecho pull de todos los repos con éxito!"
                        },
                    },
                    {
                        "type": "divider",
                    },
                ],
                text=f"PullAll by <@{command['user_name']}>!"
            )
        else:
            say(
                blocks=[
                    {
                        "type": "divider",
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"ERROR: @{command['user_name']}, por favor, revisa los logs:"
                        },
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"- /home/r2d2/r2d2_bot.log"
                        },
                    },
                    {
                        "type": "divider",
                    },
                ],
                text=f"PullAll by <@{command['user_name']}>!"
            )