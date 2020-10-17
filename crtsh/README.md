# crtsh.py

# Description
Parse crt.sh for sub-domains.

[![version](https://img.shields.io/badge/version-1.5.1-green.svg)](https://semver.org)

# Installation
git clone https://github.com/DFC302/crtsh.git \
cd crtsh \
sudo pip3 install -r requirements.txt \
sudo chmod 755 crtsh.py

**Create an alias** \
alias [alias name]='python3 [path to crtsh.py]' \
**EXAMPLE: alias crtsh='python3 ~/tools/crtsh/crtsh.py'

# Usage
```
usage: crtsh.py [-h] [-d DOMAIN [DOMAIN ...]] [-l LOOPS]
                [-k KEYWORDS [KEYWORDS ...]] [-f FILE] [-t THREADS] [-o OUT]
                [-v] [-V]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN [DOMAIN ...], --domain DOMAIN [DOMAIN ...]
                        Specify single or multiple domains to search.
  -l LOOPS, --loops LOOPS
                        Specify number of loops to append to wildcard search.
  -k KEYWORDS [KEYWORDS ...], --keywords KEYWORDS [KEYWORDS ...]
                        Use a list of keywords to search.
  -f FILE, --file FILE  Supply list of keywords from file.
  -t THREADS, --threads THREADS
                        Set number of threads.
  -o OUT, --out OUT     Write results to file.
  -v, --verbose         Turn on verbose mode. (detailed output).
  -V, --version         Display version, author information.

```
# Example Usage
In each example, crtsh stores the domains in a python set, essentially removing any duplicate domains, so you do not have to sort the file afterwards.

### Basic usage
python3 crtsh.py --domain example.com, linux.com

**The set that stores the unique domains is cleared after each domain to help separate.

### Find deep level subdomains
python3 crtsh.py --domain example.com --loops 6

crtsh.py will keep appending wildcard notation onto the end of the domain, essentially finding deep level subdomains. Once crtsh responds with no more domains, the loop is then broken, regardless if it hasnt reached its cap limit yet.

### Keyword search
python3 crtsh.py --domain example.com --keywords test, dev, stage, ops --threads [thread count]

python3 crtsh.py --domain example.com, linux.com --file [filename] --threads [thread count]
