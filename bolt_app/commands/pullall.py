import subprocess


def pullall_command(app):
    @app.command("/pullall")
    def pullall(ack, say, command):
        # Acknowledge command request
        ack()

        #
        # TEST ANSIBLE EXEC
        ###
        # script_output = subprocess.call([
        #     "/usr/local/bin/ansible_bot",
        #     "-t",
        #     "pullall",
        #     "r2d2.yml"
        # ])
        # print(script_output)


        #
        # TEST TAKE PARAMETERS FROM SLACK TEXT
        ###
        ALL_PARAMETERS=f"{command['text']}"
        FIRST_PARAMETER=f"{ALL_PARAMETERS.split()[0]}"
        SECOND_PARAMETER=f"{ALL_PARAMETERS.split()[1]}"

        script_output = subprocess.call([
            "echo",
            f"{FIRST_PARAMETER}",
            f"{SECOND_PARAMETER}",
        ])
        print(script_output)
        print(FIRST_PARAMETER)
        print(SECOND_PARAMETER)

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