# API Usage Example for haveibeenpwned
# Rename symbols file to zZ so that it is placed at end then merge all subfiles

#%% API variables
url = "https://haveibeenpwned.com/api/v3/breachedaccount/"
hibp_api_key = '7d2a0f75673...2'
item = "someone@somewhere.com"
payload={}
headers = {
  'hibp-api-key': str(hibp_api_key),
  'format': 'application/json',
  'timeout': '2.5',
  'HIBP': str(hibp_api_key)}

try:
  response = requests.request("GET", url+item+'?truncateResponse=false', headers=headers, data=payload, timeout=3)
  if response.status_code==200:
    print(response.json())
  else:
    print(response.status_code)
except Exception as excpn:
  print("Error processing "+item+" due to exception: "+str(excpn))
