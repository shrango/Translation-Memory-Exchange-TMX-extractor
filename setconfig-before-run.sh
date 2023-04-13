input_tmx_file='ecb2017.UNIQUE.en-it.tmx'
output_prefix='en-it'
sourcelang='en'
targetlang='it'

python TMX-extractor.py --inputfile $input_tmx_file --outputprefix $output_prefix --src $sourcelang --tgt $targetlang
