import subprocess
import re

# The purpose of this script is to take two files
# the primary will be a file containing all found subdomains
# the secondary file will contain out of scope domains
# This script will parse the primary file, using the out of scope domains from the secondary file
# and remove out of scoped domains from the all found subdomains.


# This is useful, as it allows confidence to scan found subdomains and not worry about scanning out of scope domains

def noScope():
	# define empty list to hold out of scope domains
	out_of_scope = []

	with open("out_of_scope.txt", "r") as rf:
		for domain in rf:
			# strip newline character and append out of scope domains
			domain = domain.strip("\n")
			out_of_scope.append(domain)

	return out_of_scope

def scope(filename):
	for domain in noScope():
		# strip new line character
		domain = domain.strip("\n")

		# if domain starts with *,
		# find all domains, index off switch *. to .*[domain]*
		# then cat scope file, grep -v each domain, to remove out of scope domains
		if domain[0] == "*":
			#modified_domain=re.findall(r"(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))",domain)
			modified_domain=re.match(r"^[\*\.].([a-z0-9\-]+)", domain)
			domain = f".*{modified_domain.group(0)[2:]}*"

		process1 = subprocess.Popen(["cat", filename], stdout=subprocess.PIPE)
		process2 = subprocess.Popen(["grep", "-v", f"{domain}"], stdin=process1.stdout, stdout=subprocess.PIPE)
		process1.stdout.close()

		output = process2.communicate()[0]
		output = output.decode()

		# write new grepped domains to file, each loop
		# if we dont do this, it will never update file
		with open(filename, "w") as wf:
			wf.write(output.strip("\n"))

	# after all loops are finished, 
	# print domains that are in scope
	with open(filename, "r") as rf:
		for line in rf:
			print(line.strip("\n"))


def main():
	scope("scope.txt")

if __name__ == "__main__":
	main()
