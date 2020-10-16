#!/bin/bash

# This script will parse the domain from massdns output

# Usage:
	# $1 = massdns output
	# $2 = file to send results to

if [ ! -f $1 ] ; then
	echo "Massdns results file does not exist! (arg 1)"
else
	cat $1 | awk '{print $1}' | sed 's/.$//' | sort -u | tee -a $2
fi
