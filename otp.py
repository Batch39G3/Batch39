import random
import http.client
import json


def otp_generate(ph_no):

    otp = random.randint(1000,9999)
    print("Your OTP is - ",otp)
    #############################################
    conn = http.client.HTTPConnection("2factor.in")
    payload = "hi gandu"
    headers = { 'content-type': "application/x-www-form-urlencoded" }
    conn.request("GET", f"/API/V1/91c4a232-dbea-11ec-9c12-0200cd936042/SMS/{str(ph_no)}/{str(otp)}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    b=data.decode("utf-8")
    j=json.loads(b)
    return j["Status"],otp

    
''''
a,b=otp_generate("7619670012")
print(a)
print(b)
'''


