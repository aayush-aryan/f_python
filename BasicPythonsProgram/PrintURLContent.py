"""
author - ${Aayush Aryan}
date - ${03-11-2020}
time - ${08:45am}
package - ${Basicpython}
Title -"Write a Python program to access and print a URL's content to the console."

"""
from http.client import HTTPConnection
try:
 conn = HTTPConnection("google.com")
 conn.request("GET", "/")
 result = conn.getresponse()
 contents = result.read()
 print(contents)
except:
    print("EnterValidDomainName")