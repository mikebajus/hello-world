import requests
import json

"""
Add vlans to NXOSv
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "vlan 600 ;name Construction ;vlan 700 ;name Analysis",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# Add static route to CSRv

url = "http://192.168.10.80/restconf/api/config/native/ip/route/ip-route-interface-forwarding-list/"

payload = "{\r\n\t\"ned:ip-route-interface-forwarding-list\": [{\r\n\t\t\"prefix\": \"216.48.1.0\",\r\n\t\t\"mask\": \"255.255.255.0\",\r\n\t\t\"fwd-list\": [{\r\n\t\t\t\"fwd\": \"10.1.1.1\"\r\n\t\t}]\r\n\t}]\r\n}"
headers = {
  'Content-Type': 'application/vnd.yang.data+json',
  'Accept': 'application/vnd.yang.data+json',
  'Accept': 'application/vnd.yang.collection+json',
  'Authorization': 'Basic YWRtaW46Y2lzY28='
}

response = requests.request("PATCH", url, headers=headers, data = payload)

print(response.text.encode('utf8'))


