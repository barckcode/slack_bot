import subprocess


def dowload_file_command(app):
    @app.command("/dowload_file")
    def dowload_file(ack, say, command):
        # Acknowledge command request
        ack()

        script_output = subprocess.run([
            "/usr/local/bin/aws",
            "s3",
            "presign",
            "s3://source.helmcode.com/api_blog/api_blog_prod.tar.gz",
            "--expires-in",
            "600" # 10min
        ], capture_output=True)

        output = str(script_output.stdout).replace('\\n', ' ')

        print(output)

        say(
            blocks=[
                {
                    "type": "divider",
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"@{command['user_name']} Para descargar el fichero de click en este link: {output}"
                    },
                },
                {
                    "type": "divider",
                },
            ],
            text=f"Dowload_file by <@{command['user_name']}>!"
        )

        # if script_output == 0:
        #     say(
        #         blocks=[
        #             {
        #                 "type": "divider",
        #             },
        #             {
        #                 "type": "section",
        #                 "text": {
        #                     "type": "mrkdwn",
        #                     "text": f"@{command['user_name']} Para descargar el fichero de click en este link: {script_output}"
        #                 },
        #             },
        #             {
        #                 "type": "divider",
        #             },
        #         ],
        #         text=f"Dowload_file by <@{command['user_name']}>!"
        #     )
        # else:
        #     say(
        #         blocks=[
        #             {
        #                 "type": "divider",
        #             },
        #             {
        #                 "type": "section",
        #                 "text": {
        #                     "type": "mrkdwn",
        #                     "text": f"ERROR: @{command['user_name']}, por favor, revisa los logs:"
        #                 },
        #             },
        #             {
        #                 "type": "section",
        #                 "text": {
        #                     "type": "mrkdwn",
        #                     "text": f"- /home/r2d2/r2d2_bot.log"
        #                 },
        #             },
        #             {
        #                 "type": "divider",
        #             },
        #         ],
        #         text=f"PullAll by <@{command['user_name']}>!"
        #     )
