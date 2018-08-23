import os
from slackclient import SlackClient


def send_slack(room, msg):
    try:
        token = os.environ["SLACK_API_TOKEN"]
    except:
        raise EnvironmentError('Before using slack, configure slack token: SLACK_API_TOKEN=\'token\' python myapp.py.'
                               'More info: https://slackapi.github.io/python-slackclient/auth.html#handling-tokens')

    sc = SlackClient(token)
    sc.api_call("chat.postEphemeral",
                channel=room,
                text=msg)
