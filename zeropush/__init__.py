# encoding: utf-8
import logging
import requests

from django.conf import settings
#from models import PushDevice

ZEROPUSH_NOTIFY_URL = "https://api.zeropush.com/notify"

log = logging.getLogger(__name__)

def notify_devices(devices, alert=None, sound=None, badge_number=None):
    if len(devices) > 0:
        params = {
            "auth_token": settings.ZEROPUSH_AUTH_TOKEN,
            "device_tokens[]": [device.device_token for device in devices]
        }
        if alert is not None:
            params.update({ "alert": alert })
        if sound is not None:
            params.update({ "sound": sound })
        if badge_number is not None:
            params.update({ "badge": badge_number })

        response = requests.post(ZEROPUSH_NOTIFY_URL, params)
        if response.ok:
            #log.info("Push successfully sent to zeropush")
            print 'Push successfully sent to zeropush'
            return True
        else:
            print 'Push Failed'+response.text
            #log.error("Error! Push failed to be sent to zeropush! Error response: %s" % response.text)
            return False

    return False

def notify_user(user, alert=None, sound=None, badge_number=None):
    #a=['56bb10f4e01ee153ebef459b9dbdbde5dd39f4f8455d3e9515fb63942bf52580']
    return notify_devices(user, alert=alert, sound=sound, badge_number=badge_number)
