#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")

print("SAAS")

cmd="sudo  ansible-playbook   docker-xpra.yml"
output=sp.getstatusoutput(cmd)
print(output)

if output[0]==0:
	print("Successful")
else:
	print("Failed")
