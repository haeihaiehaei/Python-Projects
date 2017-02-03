Example line of how to use the command in Op5.
```sh
Command line example for OP5: $USER1$/check_vcsa_rest.py --username $ARG1$ --password $ARG2$ --url $HOSTNAME$ --domain $ARG3$ --check $ARG4$
```

Use this JSON to create the local user that we will use to monitor. POST /appliance/techpreview/local-accounts/user
```json
{
    "config": {
		"username": "op5",
		"role": "operator",
		"fullname": "Op5 REST API User",
		"email": "",
		"password": ""
       }
}
```
