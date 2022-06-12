import requests

url = "https://aadhaarverify1.p.rapidapi.com/Uidverifywebsvcv1/Uidverify"

payload = "uidnumber=485820350393&consent=Y&method=uidvalidate&txn_id=4545533&clientid=111"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "aadhaarverify1.p.rapidapi.com",
	"X-RapidAPI-Key": "f4d75cc873mshd496ac1ef02dff9p12f8c9jsna891018cdb4f"
}

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)