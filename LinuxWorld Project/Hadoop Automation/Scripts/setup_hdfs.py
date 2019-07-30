#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
ns = form.getvalue('ns')

j = 1

print("<form action='hadoop_ansible_install.py'>")
print("Namenode: <input name='mip' /></br>")
while j <= int(ns):
	print("Datanode {0}: <input name='sip{0}' /></br>".format(j))
	j+=1
print("""
<input type='submit' />
</form>
""")
