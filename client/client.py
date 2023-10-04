#!/usr/bin/python3

import requests

# creta esession
session = requests.session()

# create data
data = {
    'username' : 'admin',
    'password' : 'admin'
}

session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
page = session.post("http://127.0.0.1:5000/login?next=%2F", data=data)

if 'Welcome' in page.text:
    page2 = session.get("http://127.0.0.1:5000/phones")
    print(page2.text)