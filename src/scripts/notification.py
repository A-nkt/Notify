import slackweb
import requests

SLACK_URL = ""
LINE_TOKEN = ""


class Notification():
    def slack_notify(*, text=None):
        slack = slackweb.Slack(url=SLACK_URL)
        slack.notify(text=text)

    def line_notify(*, text=None):
        line_notify_token = LINE_TOKEN
        line_notify_api = 'https://notify-api.line.me/api/notify'
        requests.post(line_notify_api, headers={'Authorization': f'Bearer {line_notify_token}'}, data={'message': f'{text}'})
