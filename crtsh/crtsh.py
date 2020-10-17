#!/usr/bin/env python3

import requests
import tldextract
import re
import argparse 
import sys
import random
import concurrent.futures

def options():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--domain",
        nargs="+",
        help="Specify single or multiple domains to search.",
        type=str,
    )

    parser.add_argument(
        "-l", "--loops",
        help="Specify number of loops to append to wildcard search.",
        type=int,
        action="store",
    )

    parser.add_argument(
        "-k", "--keywords",
        help="Use a list of keywords to search.",
        nargs="+",
        type=str,
    )

    parser.add_argument(
        "-f", "--file",
        help="Supply list of keywords from file.",
        action="store",
    )

    parser.add_argument(
        "-t", "--threads",
        help="Set number of threads.",
        action="store",
    )

    parser.add_argument(
        "-o", "--out",
        help="Write results to file.",
        action="store",
    )

    parser.add_argument(
        "-v", "--verbose",
        help="Turn on verbose mode. (detailed output).",
        action="store_true",
    )

    parser.add_argument(
        "-V", "--version",
        help="Display version, author information.",
        action="store_true",
    )
    
    # if not arguments are given, print usage message
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()
        
    args = parser.parse_args()
    
    return args

def display_version():
    print("crtsh.py v1.5.1\n")

def userAgents():
    # List of useragents
    headers = {
        "Windows-10" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Linux-OS" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Chrome-OS" : "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mac-OS" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    }
    # pick a random user agent to use
    header = random.choice(list(headers.values()))
    # return user agent to be used
    return header

def crtsh():
    scope = options().domain
    unique_domains = set()

    for domain in scope:

        # if user separates domains with a comma, but no space, replace comma, add space
        if "," in domain:
            domain = domain.strip(",")

        if "*." in domain:
            domain = domain.strip("*")

        # If user does not specify number of loops, use a default of 1
        if not options().loops:
            loops = 1
            counter = 1
            wildcard = "%25."
        # for each loop, append url encode of * to domain
        elif options().loops:
            wildcard = "%25."
            counter = 1
            loops = options().loops

        while counter <= loops:
            domain = f"{wildcard}{domain}"
            url = f"https://crt.sh/?q={domain}&output=json"
            
            # Replace encoded asteriks with actual asteriks to show user
            # their original search
            if options().verbose:
                decoded_domain = domain.replace("%25", "*")
                print(f"Gathering results for: {decoded_domain}({counter})")
    
            try:
                response = requests.get(url, headers={'User-Agent':userAgents()})
                regex = r'[^%*].*'
                data = response.json()
        
                if data:
                    for row in data:
                        row = re.findall(regex, row["name_value"])[0]
                        unique_domains.add(row)
                
                elif not data:
                    if options().verbose:
                        print(f"[x] No data found for {decoded_domain} using crtsh.")
                    
                    break
    
            except ValueError:
                pass
        
            counter+=1

        # If actual subdomains are present in the set
        if len(unique_domains):
            print(f"\nUnique domains found for {domain}\n")
            print("\n".join(unique_domains))
            print("\n")

            if options().out:
                with open(options().out, "a") as wf:
                    wf.write("\n".join(unique_domains)+"\n")
                    unique_domains.clear()

            else:
                unique_domains.clear()

def thread_execution():
	domains = []

	if options().file:
		with open(options().file, "r") as f:
			for keyword in f:
				if keyword == "":
					pass

				else:
					keyword = str(keyword.strip("\n"))
					domains.append(keyword)

	elif options().keywords:
		for keyword in options().keywords:
			domains.append(keyword)

	if options().threads:
		threads = options().threads
	
	else:
		threads = 20

	with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
		executor.map(keyword_crtsh, domains)

def keyword_crtsh(keyword):
    unique_domains = set()

    scope = options().domain

    if "," in keyword:
        keyword = keyword.strip(",")

    for domain in scope:

        try:
            url = f"https://crt.sh/?q=%25.{keyword}%25.{domain}&output=json"
            response = requests.get(url, headers={'User-Agent':userAgents()})
            regex = r'[^%*].*'
            data = response.json()
            
            if data:
                for row in data:
                    row = re.findall(regex, row["name_value"])[0]
                    unique_domains.add(row)
                
            elif not data:
                if options().verbose:
                    print(f"[x] No data found for: {keyword}")

        except ValueError:
            pass
    
    # If actual subdomains are present in the set
    if len(unique_domains):
        print("\n".join(unique_domains))

    if options().out and len(unique_domains):
        with open(options().out, "a") as wf:
            wf.write("\n".join(unique_domains)+"\n")

def version():
    print('''
        Author: Matthew Greer
        Github: github.com/DFC302
        Twitter: github.com/Vail__

        Version: 1.5.1

    ''')

def main():
    if (options().domain) and (options().keywords or options().file) and not (options().loops):
        display_version()
        thread_execution()
    elif options().domain  and not (options().keywords or options().file):
        display_version()
        crtsh()
    elif options().version:
        version() 

if __name__ == "__main__":
    main()
