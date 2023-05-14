import slackweb
import requests

class Notification():
    def slack_notify(*,text='てすと'):
        slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
        #slack.notify(text="pythonからslackさんへ")
        slack.notify(text=text)

    def line_notify(*,text='てすと'):
        line_notify_token = 'oSEfAxb2DcHoYsFhSPkBHeki8z70wFYUXCYj8fjXyV6'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'{text}'}
        requests.post(line_notify_api, headers = headers, data = data)
