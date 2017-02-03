#!/usr/bin/python
"""
Op5 check to get the health of the VCenter Appliance via REST API.

Copyright 2017 Martin Persson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

author = 'Martin Persson'
url = 'https://github.com/haeihaiehaei/Python-Projects/blob/master/vmware/op5_vcsa_plugin/check_vcsa.py'
version = '0.1'

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    import json
    import sys
    import argparse
    import base64

except ImportError:
    print "Error: missing one of the libraries (requests, json, sys, argparse, base64)"
    sys.exit()

# Disable the unverified HTTPS warnings. We are not running certificates.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Handle our arguments here.
parser = argparse.ArgumentParser(
    description=__doc__,
    epilog='Developed by %s - For more information see: "%s"'
    % (author, url))

parser.add_argument('-u', '--username', dest='username', required=False, help='Username, ex administrator')
parser.add_argument('-p', '--password', dest='password', required=False, help='Password for the user')
parser.add_argument('-d', '--domain', dest='domain', required=False, help='domain name for the vcenter')
parser.add_argument('-U', '--url', dest='url', required=False, help='url to the vcenter')
parser.add_argument('-c', '--check', dest='check', required=False, help='what are we checking, the following is avaliable: database-storage, load, mem, storage')
parser.add_argument('-v', '--version', action='version', version='%(prog)s (version 0.16)')

args = parser.parse_args()

def login():

    credentials = str(args.username) + ":" + str(args.password)

    # To send the authentication header we need to convert it to Base64.
    b64credentials = "Basic" + " " + base64.b64encode(credentials)

    url = "https://" + str(args.url) + "." + str(args.domain) + "/rest/com/vmware/cis/session"
    payload = ""
    headers = {
        'content-type': "application/json",
        'authorization': b64credentials,
    }

    # Set the session_id to a global variable so we can use it later.
    global session_id

    session = requests.request("POST", url, data=payload, headers=headers, verify=False)

    session_id = json.loads(session.text)['value']

def health_check():

    url = "https://" + str(args.url) + "." + str(args.domain) + "/rest/appliance/health/" + str(args.check)
    headers = {
        'vmware-api-session-id': "%s" % session_id
    }

    response = requests.request("GET", url, headers=headers, verify=False)

    value = json.loads(response.text)['value']

    if value == 'green':
        print('OK')
        logout()
        sys.exit(0)
    elif value == 'yellow':
        print('Warning')
        sys.exit(1)
    elif value == 'orange':
        print('Warning')
        sys.exit(1)
    elif value == 'red':
        print('Critical.')
        logout()
        sys.exit(2)

def logout():

    url = "https://" + str(args.url) + "." + str(args.domain) + "/rest/com/vmware/cis/session"
    headers = {
        'vmware-api-session-id': "%s" % session_id
    }

    logout_value = requests.request("DELETE", url, headers=headers, verify=False)

    print(logout_value.text)

login()
health_check()
logout()
