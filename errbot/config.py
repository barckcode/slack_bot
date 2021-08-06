import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_IDENTITY = {
    'token': 'xoxb-1682904913810-2355938020322-LsqpGwFZpzFpd83dkPtaXNVr',
}


BOT_DATA_DIR = r'/Users/cristianandrescordovavalencia/Desktop/SRE/Projects/personal_repo/slack_bot/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/Users/cristianandrescordovavalencia/Desktop/SRE/Projects/personal_repo/slack_bot/errbot/plugins'

BOT_LOG_FILE = r'/Users/cristianandrescordovavalencia/Desktop/SRE/Projects/personal_repo/slack_bot/errbot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@barckcode', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!
