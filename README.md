# pyEGI-AAI-CheckIn

## Requirements:
* Members of the VO should be identified via their EGI ePUID.
* Membership should be limited to the specified period.
* Different membership status values should be supported, namely 'Active', 'Expired', 'Deleted'.
* CheckIn should automatically change the membership status from 'Active' to 'Expired' beyond the validity period.
* Python 2.7.12+

## Authentication:
The REST client is authenticated via username/password credentials transmitted over HTTPS using the Basic Authentication scheme. More sophisticated authentication mechanisms, such as OpenID Connect/OAuth 2.0 access tokens, may be supported in the future.

## Methods:
1. Adding a user to a VO requires:
* Specifying the user’s EGI ID, 
* The name of the VO ("vo.access.egi.eu" in the case of the EGI AoDs), 
* The status ("Active"), and 
* The valid from/through dates. 

All these parameters are mandatory. 

Use the setVOMembership(login, password, url) method to add the user to the VO:

```
login = "*****"
password = "******"
url = "https://aai.egi.eu/api/v1/VoMembers"

# Configure here and add the user's unique, non-reassignable, persistent pseudonymous EGI ID
EGI_ID = "<EGI_user_ID>" # e.g.: <ASCII>@egi.eu
[..]

def main():
  # Set the VO memberships for a given EGI ID
  setVOMembership(login, password, url)
```

Configure the JSON/ltos-add-USER.json file settings:

```
{
  "RequestType": "VoMembers",
  "Version": "1.0",
  "VoMembers": [
    {
      "Version": "1.0",
      "VoId": "vo.access.egi.eu",
      "Person": {
        "Type": "CO",
        "Id": "<ADD HERE THE UNIQUE PERSISTENT EGI ID FOR THE USER>" 
      },
      "Status": "Active",
      "ValidFrom": "2019-01-01",
      "ValidThrough": "2020-12-31"
    }
  ]
}
```

Execute the python script as follows:

```
]$ python pySetVOEntitlements.py
[.] Set VO membership information for a given EGI ID
[ Request ] = https://aai.egi.eu/api/v1/VoMembers
[ Payload ] = {u'RequestType': u'VoMembers', u'Version': u'1.0', u'VoMembers': [{u'Status': u'Active', u'VoId': u'vo.access.egi.eu', u'Person': {u'Type': u'CO', u'Id': u'012345689[..]@egi.eu'}, u'Version': u'1.0', u'ValidThrough': u'2020-03-11', u'ValidFrom': u'2019-03-11'}]}

[ Response ]
- {u'message': [{u'status': u'Active', u'vo_id': u'vo.access.egi.eu', u'valid_from': u'2019-03-10T22:00:00.000Z', u'valid_through': u'2020-03-10T22:00:00.000Z', u'epuid': u'0123456789[..]@egi.eu', u'id': 93}], u'code': u'InvalidFields'}
- [{u'status': u'Active', u'vo_id': u'vo.access.egi.eu', u'valid_from': u'2019-03-10T22:00:00.000Z', u'valid_through': u'2020-03-10T22:00:00.000Z', u'epuid': u'0123456789[..]@egi.eu', u'id': 93}]
```

* Retrieving the VO membership information for a given EGI ID:

```
]$ curl -vX GET https://aai.egi.eu/api/v1/VoMembers/01234567890123456789@egi.eu \
  --user "example-client":"veryverysecret"

{"id":85,"epuid":"01234567890123456789@egi.eu","vo_id":"vo.access.egi.eu","valid_from":"2017-05-20T22:00:00.000Z","valid_through":"2017-06-21T22:00:00.000Z","status":"Active"}
```
Beyond the valid_through date, the status will be automatically changed to "Expired". So, when querying for VO membership information, it’s important to check that the status is actually set to "Active", and of course that the vo_id equals "vo.access.egi.eu".

You can also check the VO membership information usign the getVOMembership() method.
