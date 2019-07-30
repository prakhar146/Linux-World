#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")

print("CAAS")

cmd="sudo ansible-playbook  docker-shellinabox.yml"
output=sp.getstatusoutput(cmd)
print(output)

if output[0]==0:
	print("CAAS service started")
	
else:
	print("ERROR")

