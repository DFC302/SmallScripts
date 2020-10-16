#!/bin/bash

# parse's domains from amass active
# script is based off of amass command (amass enum -active -ip -brute -d [domain] -o [outfile])

if [ $# -lt 1 ] ; then
    echo "[ usage ]: parseDomainFrmAmass [file]"

else
	cat $1 | cut -d ' ' -f1
fi
