# generate_words.py

This script will generate words using dictionaries of the user's choice.

**Note: dictionary is limited. Some words may not be found, such as "don't" due to its apostraphe.**

# Usage
```
usage: generateWords.py [-h] [--reduce] [--letters LETTERS] [--out OUT]
                        [--length LENGTH] [--dict DICT]
                        [--check-dict CHECK_DICT] [--verbose] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --reduce, -r          Used with generate-words flag, used to produce all
                        words of a given length and reduce down to two words.
  --letters LETTERS, -L LETTERS
                        Used specific letters over entire alphabet.
  --out OUT, -o OUT     Write results to file.
  --length LENGTH, -l LENGTH
                        Specify length of words
  --dict DICT, -d DICT  Choose dictionary.
  --check-dict CHECK_DICT, -cd CHECK_DICT
                        Check if dictionary exists to be used.
  --verbose, -v         Turn on verbose mode.
  --version, -V         Print version and author information.
```

# Installation
```
git clone https://github.com/DFC302/SmallScripts.git
cd SmallScripts/GenerateWords/
pip install -r requirements.txt
```

# Issues
If you run into an issue with libenchant, you can go [here](https://pyenchant.github.io/pyenchant/install.html) to try and find a solution for your distro of choice.
