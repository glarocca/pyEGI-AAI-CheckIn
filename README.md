# pyEGI-AAI-CheckIn

## Requirements:
* Members of the VO should be identified via their EGI ePUID.
* Membership should be limited to the specified period.
* Different membership status values should be supported, namely ‘Active’, ‘Expired’, ‘Deleted’.
* CheckIn should automatically change the membership status from ‘Active' to ‘Expired’ beyond the validity period.

## Authentication:
The REST client is authenticated via username/password credentials transmitted over HTTPS using the Basic Authentication scheme. More sophisticated authentication mechanisms, such as OpenID Connect/OAuth 2.0 access tokens, may be supported in the future.

## Methods:
1. Adding a user to a VO requires specifying the user’s EGI ID, the name of the VO (“vo.access.egi.eu” in the case of the EGI AoDs), the status (“Active”) and the valid from/through dates. All these parameters are mandatory. Here is an example using curl (see attached ltos-add.json file):

```
curl -vX POST https://aai.egi.eu.eu/api/v1/VoMembers \
  —user “example-client”:”veryverysecret” \
  --data @ltos-add.json \
  --header "Content-Type: application/json"
```

2. Retrieving the VO membership information for a given EGI ID:

```
curl -vX GET https://aai.egi.eu.eu/api/v1/VoMembers/01234567890123456789@egi.eu \
  —user “example-client”:”veryverysecret”

{“id":85,"epuid":"01234567890123456789@egi.eu","vo_id":"vo.access.egi.eu","valid_from":"2017-05-20T22:00:00.000Z","valid_through":"2017-06-21T22:00:00.000Z","status":"Active"}
```
Beyond the valid_through date, the status will be automatically changed to “Expired”. So, when querying for VO membership information, it’s important to check that the status is actually set to “Active”, and of course that the vo_id equals “vo.access.egi.eu”.

3. Updating existing VO membership record:

```
curl -vX PUT https://aai.egi.eu.eu/api/v1/VoMembers \
  --user “example-client”:”veryverysecret”  \
  --data @ltos-add.json \
  --header "Content-Type: application/json"
```

The request body is the same as the one used for adding new members but update requires using PUT instead of POST.

4. Removing VO member:
Same as the update but requires setting the membership status to “Deleted”
