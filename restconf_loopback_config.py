import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

url= "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=Loopback200"

auth = HTTPBasicAuth("developer","C1sco12345")

data= { "ietf-interfaces:interface": 
    {
         "name": "Loopback200", 
         "description": "Added with RESTCONF",
         "type": "iana-if-type:softwareLoopback",
         "enabled": True,
         "ietf-ip:ipv4": 
         { 
             "address": 
             [ 
                 { 
                     "ip": "172.16.110.1",
                     "netmask": "255.255.255.0"
                 } 
            ]
         }
    } 
}
headers = {
  'Content-Type': 'application/yang-data+json',
}


response = requests.put(url,auth=auth,headers=headers,data=json.dumps(data),verify=False)
print(response.text)
print(response.status_code)

#can use PUT to modify 

