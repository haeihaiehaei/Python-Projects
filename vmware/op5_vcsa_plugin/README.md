[logo]: https://s29.postimg.org/pm7a5xlk7/python_logo_1.png "Powered by Python")


> This Op5-plugin will use the GET function to pull the status of the various health APIs avaliable.

Currently you can get:

 * database-storage
 * load
 * mem
 * storage


Example of how to use the command in Op5.
```sh
Command line example for OP5: $USER1$/check_vcsa_rest.py --username $ARG1$ --password $ARG2$ --url $HOSTNAME$ --domain $ARG3$ --check $ARG4$
```

# User creation
This check needs a local user created on the Appliance, you can create this in two different ways.

### Command Shell
######Easier for most people

```sh
Command> localaccounts.user.add --role operator --username op5 --password
```
### REST API Json
##### Need to be logged in as an Admin user.

Use this JSON to POST to /rest/appliance/techpreview/local-accounts/user.
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
