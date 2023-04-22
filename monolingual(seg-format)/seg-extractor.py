from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inputprefix','-i',required=True,type=str)
parser.add_argument('--outputprefix','-o',type=str,default='')
parser.add_argument('--lang',type=str,default='any')
args = parser.parse_args()

inputfile = '.'.join([args.inputprefix,args.lang])
with open(inputfile,'r',encoding='utf-8')as f:
    content = f.read()
soup = BeautifulSoup(content,'lxml')

segs = soup.find_all('seg')
texts = [i.text for i in segs]
print('Extracted {} sentences.'.format(len(texts)))
if args.outputprefix=='':
    outputprefix = args.inputprefix+'.text'
else:
    outputprefix = args.outputprefix
outputfile = '.'.join([outputprefix,args.lang])
with open(outputfile,'w',encoding='utf-8')as f:
    for line in texts:
        f.write(line+'\n')
print('Finished saving into file {}'.format(outputfile))
