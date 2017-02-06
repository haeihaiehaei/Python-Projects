### This Op5-plugin will use the GET function to pull the status of the various health APIs avaliable.

Currently you can get:

 * database-storage
 * load
 * mem
 * storage

Example of how to use the command in Op5.
```sh
Command line example for OP5: $USER1$/check_vcsa_rest.py --username $ARG1$ --password $ARG2$ --url $HOSTNAME$ --domain $ARG3$ --check $ARG4$
```

### Required Permissions
The check needs a user with READ-ONLY global permissions.
