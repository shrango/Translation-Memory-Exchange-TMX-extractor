from bs4 import BeautifulSoup
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--inputfile','-i',required=True,type=str)
parser.add_argument('--outputprefix','-o',type=str,default='output-of-tmx2txt')
parser.add_argument('--src',type=str,default='')
parser.add_argument('--tgt',type=str,default='')
args = parser.parse_args()

# Be careful! Memory usage may be explosively increase when the input file's size gets bigger.

with open(args.inputfile,'r',encoding='utf-8')as f:
    content = f.read()
soup = BeautifulSoup(content,'xml')

tuv_pairs = soup.find_all('tuv')

print('Total tuv sentences:',len(tuv_pairs),' sentences for each lang should be half of it')

src_data=[]
tgt_data=[]
auto_detect_src=tuv_pairs[0].attrs['xml:lang']
auto_detect_tgt=tuv_pairs[1].attrs['xml:lang']
if args.src=='':
    src = auto_detect_src
else:
    src = args.src
if args.tgt=='':
    tgt = auto_detect_tgt
else:
    tgt = args.tgt
if auto_detect_src==tgt and auto_detect_tgt==src:
    src,tgt=tgt,src
assert auto_detect_src==src and auto_detect_tgt==tgt, "Please check if src and tgt are correct."
for idx,line in tqdm(enumerate(tuv_pairs)):
    if idx%2==0:
        # should be src
        assert line.attrs['xml:lang']==src, "Unexpected lang id found in the "+str(idx)+" sentence."
        src_data.append(line.find('seg').text.strip())
    else:
        # should be tgt
        assert line.attrs['xml:lang']==tgt, "Unexpected lang id found in the "+str(idx)+" sentence."
        tgt_data.append(line.find('seg').text.strip())

print('Extraction Done!')
print('Saving into '+args.outputprefix+'.('+src+'/'+tgt+')')
with open(args.outputprefix+'.'+src,'w',encoding='utf-8')as f:
    for line in src_data:
        f.write(line+'\n')

with open(args.outputprefix+'.'+tgt,'w',encoding='utf-8')as f:
    for line in tgt_data:
        f.write(line+'\n')
print('Saving Done!')
