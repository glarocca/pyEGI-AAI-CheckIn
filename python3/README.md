# pysetVOrights

## Requirements:
* Members of the VO should be identified via their EGI ePUID.
* Membership should be limited to the specified period.
* Different membership status values should be supported, namely `Active`, `Expired`, `Deleted`.
* Check-In should automatically change the membership status from `Active` to `Expired` beyond the validity period.
* Python 3

## Install requirements

```bash
pip install -r requirements.txt
```

## Authentication:
The REST client is authenticated via `login` & `password` credentials transmitted over HTTPS using the Basic Authentication scheme. More sophisticated authentication mechanisms, such as OpenID Connect, OAuth 2.0 access tokens, may be supported in the future.

Configure the `JSON`/`config.json` file:

```json
{
  "login" : "*****",
  "password" : "******",
  "url" : "https://aai.egi.eu/api/v1/VoMembers"
}
```

## User configuration

All these parameters are mandatory.

* Specifying the user’s EGI ID,
* The name of the VO (`vo.access.egi.eu` in the case of the EGI AoDs),
* The status (`Active`), and
* The valid from/through dates.

Configure the `JSON`/`user.json` file settings:

```json
{
  "RequestType": "VoMembers",
  "Version": "1.0",
  "VoMembers": [
    {
      "Version": "1.0",
      "VoId": "vo.access.egi.eu",
      "Person": {
        "Type": "CO",
        "Id": "****@egi.eu"
      },
      "Status": "Active",
      "ValidFrom": "2021-01-01",
      "ValidThrough": "2022-01-01"
    }
  ]
}
```

## Usage

Use the help option for the python command line interface as follows:

```bash
$ python pysetVOrights.py -h
```

* Adding a user to a VO requires:

Use the `--set` option to add the user to the VO:

```bash
$ python pysetVOrights.py -s
```

* Retrieving the VO membership information for a given EGI ID:

```bash
$ python pysetVOrights.py -g
```

Beyond the `valid_through` date, the status will be automatically changed to `Expired`. So, when querying for VO membership information, it’s important to check that the status is actually set to `Active`.

You can also check the VO membership information usign the APIs:

```bash
$ curl -vX GET https://aai.egi.eu/api/v1/VoMembers/01234567890123456789@egi.eu \
  --user "example-client":"veryverysecret"

{"id":85,"epuid":"01234567890123456789@egi.eu","vo_id":"vo.access.egi.eu","valid_from":"2017-05-20T22:00:00.000Z","valid_through":"2017-06-21T22:00:00.000Z","status":"Active"}
```
