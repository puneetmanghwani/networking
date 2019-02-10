#!/usr/bin/python3


import os

os.system(' while read p; do cat command.sh | sshpass -p "redhat" ssh -tt -o StrictHostKeyChecking=no root@192.168.10.$p; done <ip.txt')







