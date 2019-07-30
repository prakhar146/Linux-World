#!/usr/bin/python2


print("content-type: text/html")
print("")

print("Welcome to PAAS Services")
print("<br />")
print("""
<form action='docker-paas-setup.py'>
<select name='passname'>
<option>python2</option>
<option>python36</option>
<option>java</option>
<option>scala</option>
</select>
<br />
<input  type='submit'>
</form>


""")
