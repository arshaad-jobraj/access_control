import RPi.GPIO as GPIO
import json
import requests
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Webhook_url
webhook_url = 'https://hooks.slack.com/services/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'

# Data to send slack
slack_data = {
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Someone is at the Main Door!\n"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Approve"
                    },
                    "style": "primary",
                    "url": "http://192.168.2.105:8100/maindoor"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Check whose there?"
                    },
                    "style": "danger",
                    "url": "http://192.168.2.105:8100/image"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "N.B. Actions only work while connected to simtech"
            }
        }
    ]
}

# GPIO 12 set up as input, pulled down to avoid false detection
# Rising edge detection
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# If someone at the door, send message to slack
def message_slack(channel):
    print("Interrupt Triggered")
    os.system('ffmpeg -y -i rtsp://admin:admin@192.168.2.106/live -f image2 image.jpg')
    # POST Request to slack
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'})


# Interrupt Event, Call message_slack functon, with debounce time 600ms
GPIO.add_event_detect(12, GPIO.RISING, callback=message_slack, bouncetime=600)

GPIO.cleanup()