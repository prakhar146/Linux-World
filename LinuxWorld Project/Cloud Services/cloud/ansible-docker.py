#!/usr/bin/python2

import cgi
import commands  as sp

print("content-type: text/html")
print("")

print("<marquee><u>WELCOME TO CLOUD SERVICES</u></marquee>")

print("<br />")
print("<br />")
print("<br />")
print("<br />")

print("""
<table  border='5' align='center'>
<tr>
<td>SAAS</td>
<td><a href='software-service.py'>Click here to start SAAS</a></td>
</tr>
<tr>
<td>CAAS</td>
<td><a href='container-service.py'>Click here to start CAAS</a></td>
</tr>
<tr>
<td>PAAS</td>
<td><a href='platform-service.py'>Click here to start PAAS</a></td>
</tr>
<tr>
<td>STAAS</td>
<td><a href='storage-service.py'>Click here to start PAAS</a></td>
</tr>
</table>
""")





