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


