import requests

req = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print( req.status_code == requests.codes.ok)   # if no error then True
req.raise_for_status()  # if error occurs it will raise an exception
print(req.text[:250])