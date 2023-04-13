# Translation-Memory-Exchange-TMX-extractor
This repository aims to extract translation sentence pairs from "tmx" format file.

Some of open-sourced translation datasets provide parallel dataset in "tmx" format. 

E.g. the European languages datasets: https://tilde-model.s3-eu-west-1.amazonaws.com/Tilde_MODEL_Corpus.html,
or WMT19 FI-EN dataset https://s3.amazonaws.com/web-language-models/paracrawl/release3/en-fi.bicleaner07.tmx.gz, etc.

# Requirement for this script
BeautifulSoup is needed to parse the `xml` format.

Please use `pip install bs4` to install it.

# Script for Usage
To start from a shell script:
1. set input, output, languages in `setconfig-before-run.sh`
2. run `bash setconfig-before-run.sh`

To directly use in Python:
run python TMX-extractor.py --inputfile <Your tmx file> --outputprefix <file name of output> --src <source language> --tgt <target language>

This is an example:
python TMX-extractor.py --inputfile 'ecb2017.UNIQUE.en-it.tmx' --outputprefix 'en-it' --src 'en' --tgt 'it'

# Warning
Be careful! Memory usage may be explosively increase when the input file's size gets bigger.

When processing this file `en-fi.bicleaner07.tmx`, which takes 8GB hardware usage, my RAM usage goes up to 120GB.
This is because BeautifulSoup uses a lot of memory when paring the whole file.