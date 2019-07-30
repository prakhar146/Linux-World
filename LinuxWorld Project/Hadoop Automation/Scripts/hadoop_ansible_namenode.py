#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess as sp
import cgi


sp.getoutput("sudo ansible-playbook /root/ansible_project/hdfs_nn.yml")
print("Namenode created")

