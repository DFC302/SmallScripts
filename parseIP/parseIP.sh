#!/bin/bash

# outfile
# grab last argument as write to file
out=${!#}

# Take unknown number of filenames that have IPs in them
for file in "$@"; do
	# parse the IPs out of them
	# user can choose redirection to write to a file
	cat ${file} | grep -Eo "([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})" >> ${out}
	sort -u ${out} -o ${out}
done

cat ${out}
