# pyEGI-AAI-CheckIn

## Requirements:
* Members of the VO should be identified via their EGI ePUID.
* Membership should be limited to the specified period.
* Different membership status values should be supported, namely 'Active', 'Expired', 'Deleted'.
* CheckIn should automatically change the membership status from 'Active' to 'Expired' beyond the validity period.

## Authentication:
The REST client is authenticated via username/password credentials transmitted over HTTPS using the Basic Authentication scheme. More sophisticated authentication mechanisms, such as OpenID Connect/OAuth 2.0 access tokens, may be supported in the future.

## Methods:
* Adding a user to a VO requires:
**Specifying the user’s EGI ID, 
**The name of the VO ("vo.access.egi.eu" in the case of the EGI AoDs), 
**The status ("Active"), and 
**The valid from/through dates. 

All these parameters are mandatory. Here is an example using curl (see attached ltos-add-USER.json file):

```
]$ curl -vX POST https://aai.egi.eu.eu/api/v1/VoMembers \
  -user "example-client":"veryverysecret" \
  --data @ltos-add-USER.json \
  --header "Content-Type: application/json"
```
Use the setVOMembership(login, password, url) method to add the user to the VO:


```
# Configure here and add the user's unique, non-reassignable, persistent pseudonymous EGI ID
EGI_ID = "<EGI_user_ID>" # e.g.: <ASCII>@egi.eu
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
```



* Retrieving the VO membership information for a given EGI ID:

```
]$ curl -vX GET https://aai.egi.eu.eu/api/v1/VoMembers/01234567890123456789@egi.eu \
  -user "example-client":"veryverysecret"

{"id":85,"epuid":"01234567890123456789@egi.eu","vo_id":"vo.access.egi.eu","valid_from":"2017-05-20T22:00:00.000Z","valid_through":"2017-06-21T22:00:00.000Z","status":"Active"}
```
Beyond the valid_through date, the status will be automatically changed to "Expired". So, when querying for VO membership information, it’s important to check that the status is actually set to "Active", and of course that the vo_id equals "vo.access.egi.eu".

* Updating existing VO membership record:

```
curl -vX PUT https://aai.egi.eu.eu/api/v1/VoMembers \
  --user "example-client":"veryverysecret"  \
  --data @ltos-add.json \
  --header "Content-Type: application/json"
```

The request body is the same as the one used for adding new members but update requires using PUT instead of POST.

* Removing VO member:
Same as the update but requires setting the membership status to "Deleted"
