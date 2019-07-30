#!/usr/bin/python2

print("content-type: text/html")
print("")

import cgi
import commands as sp

print("This is Python Prompt.")

form=cgi.FieldStorage()
passname=form.getvalue("passname")

cmd="sudo ansible-playbook  python.yml"
output=getstatusoutput(cmd)
print(output)

print("EEEEEEEEEEEEEEEE")

if output[0]==0:
	print("Successful")
else:
	print("Error")



