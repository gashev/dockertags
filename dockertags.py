#!/usr/bin/python

import certifi
import json
import os
import sys
import urllib3

def error(message):
    sys.stderr.write(message + '\n')
    sys.exit(1)

def validate_arguments():
    if (len(sys.argv) != 2):
        cmd = os.path.basename(sys.argv[0])
        error('Usage: %s TERM' % (cmd))

def send_request(term):
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    url = 'https://index.docker.io/v1/repositories/%s/tags' % (term)
    return http.request('GET', url)

def validate_status(status):
    if (status != 200):
        raise

def print_tags(data):
    data = json.loads(data)
    for item in data:
        print item['name']

def main():
    validate_arguments()
    try:
        r = send_request(sys.argv[1])
        validate_status(r.status)
        print_tags(r.data)
    except:
        error('Not found.')

    return 0

if __name__ == "__main__":
    sys.exit(main())
