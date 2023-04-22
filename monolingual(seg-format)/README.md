# Target Format
This script is written for files recording monolingual texts wrapped in `<seg>` and `</seg>` tags. 

A typical example is `newstest2017-ende-src.en.sgm`, which can be find in http://data.statmt.org/wmt22/translation-task/dev.tgz

An example that is a combination from newstest2017-ende to newstest2020-ende can be found in `example` of this repo.

# Usage
There are 3 args in this script.
1. `--inputprefix`, short for `-i`, language sign (e.g. en) should be excluded from it. This is a required arg.
2. `--outputprefix`, short for `-o`, language sign (e.g. en) should be excluded from it. This is an optional arg, which is set to `inputprefix + '.text'`.
3. `--lang`. e.g en, zh, de, etc.

You can simply run the shell script `extracting-text.sh`, after passing your configurations by modifing this script.

It also works if you copy the commands within `extracting-text.sh` and directly run on commandline.

