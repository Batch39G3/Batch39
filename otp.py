import random
otp = random.randint(1000,9999)
print("Your OTP is - ",otp)
#############################################


# python script for sending message update






import requests
from requests.structures import CaseInsensitiveDict

url = "https://sms.api.sinch.com/xms/v1/ae41684b4a1b4f618b952cd94c0721b4/batches"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer ba9a52d664e34c0eb2ded967992146fc"
headers["Content-Type"] = """{"id": "01G3X09GRCV1YX0RG4Q2PR0EPX",
    "to": ["91719670012"],
    "from": "447520650759",
    "canceled": false,
    "body": "1234",
    "type": "mt_text",
    "created_at": "2022-05-25T07:00:57.740Z",
    "modified_at": "2022-05-25T07:00:57.740Z",
    "delivery_report": "none",
    "expire_at": "2022-05-28T07:00:57.740Z",
    "flash_message": false}"""

data = """

  {
    "from": "447520650759",
    "to": ["919916407340"],
    "body": "4858"
  }
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)







