#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp
import cgi

form = cgi.FormContent()

k=0

fh=open('/root/automate/hosts','w')

fh.write("\n[master]\n")
for i in form.keys():
	if 'mip' in i:	
		fh.write(form[i][0]+" ansible_ssh_user=root ansible_ssh_pass=redhat\n")
	else:
		if k==0:     
			fh.write("[slave]\n")
			k=k+1
		fh.write(form[i][0]+" ansible_ssh_user=root ansible_ssh_pass=redhat\n")

fh.close()

frame = cgi.FieldStorage()
mip = frame.getvalue('mip')

fm=open('/root/automate/nnip.yml','w')
fm.write("ip: {}".format(mip))
fm.close()

sp.getoutput("sudo ansible-playbook /root/ansible_project/hdfs_install.yml")
print("Setup installed")

print("""
<form action='hadoop_ansible_namenode.py'>
<a href='hadoop_ansible_namenode.py'>Click here to create namenode</a>
""")

#sp.getoutput("sudo ansible-playbook /root/ansible_project/hdfs_nn.yml")
#print("Namenode created")
print("\n")

print("""
<form action='hadoop_ansible_datanode.py'>
<a href='hadoop_ansible_datanode.py'>Click here to create datanodes</a>
""")

#sp.getoutput("sudo ansible-playbook /root/ansible_project/hdfs_dn.yml")
#print("Datanode created")
