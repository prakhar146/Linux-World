#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print("")

form = cgi.FieldStorage()
nstt = form.getvalue('nstt')

j = 1

print("<form action='mapreduce_ansible.py'>")
print("Namenode: <input name='mip' /></br>")
print("Jobtracker: <input name='jtip' /></br>")
while j <= int(nstt):
	print("Datanode/Tasktracker {0}: <input name='stip{0}' /></br>".format(j))
	j+=1
print("""
<input type='submit' />
</form>
""")
