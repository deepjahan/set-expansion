import sys
sys.path.append('word2vec')
sys.path.append('PatternRecognition')
sys.path.append('outputfiles')
sys.path.append('Crawling')
sys.path.append('API/googlesearch')
sys.path.append('API/bing')
sys.path.append('API/faroo.py-master')
sys.path.append('API/wikisearch')
import re
from collections import Counter, defaultdict
import operator
import urllib
import os
from search import *
import urllib2
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from getpage import getandparseurls

result=[]
def expandUsingPatterns(data,seeds):
	patterns=[]
	wrappers=defaultdict(list)
	for i in seeds:
		j=i.lower()
		patterns.append('(?=(<.*'+j+'.*>))')
	f=data.split('\n')
	while '' in f: f.remove('')
	for line in f:
		j=line.lower()
		for p,s in zip(patterns,seeds):
			m=re.findall(p,j)
			if m==[]:
				continue
			m=min(m,key=len)
			#print m
			sp=m.split(s.lower())
			"""M=''
			for i in sp[1]:
				if i == '>':
					M+=i
					break
				M+=i
			wrappers.append((sp[0],M))"""
			M=[sp[0]]
			for i in range(1,len(sp)):
				Mk=''
				for k in sp[i]:
					if k =='>':
						Mk+=k
						break
					Mk+=k
				M.append(Mk)
			#print M
			wrappers[tuple(M)].append(s)
	d=wrappers
	#sorted_d = sorted(d.items(),key=operator.itemgetter(1))
	#print sorted_d
	wrappers=[]
	for i in d.keys():
		if len(seeds)<=3:
			if len(set(d[i]))>1:
				wrappers.append(i)
		elif len(set(d[i]))>2:
			#print d[i],i
			wrappers.append(i)
	patterns=[]
	for i in wrappers:
		wrap=i[0]
		for j in range(1,len(i)):
			wrap=wrap+".*?"+i[j]
		wrap = "(?=("+wrap+"))"
		#print wrap
		patterns.append(wrap)
	global result
	for line in f:
		j=line.lower()
		for p,w in zip(patterns,wrappers):
			m=re.findall(p,j)
			for i in m:
				#print j,"\n\n",i,"\n"
				i=i.split(w[0])[1].split(w[1])[0].strip()
				#print i,"\n"
				if all(x.isalpha() or x.isspace() for x in i) and i!='':
					result.append(i)

def main():
	#seeds=["mahatma gandhi", "bhagat singh", "rani lakshmibai" ,"mangal pandey"]
	seeds = sys.argv[1].split(',')
	for i in range(len(seeds)):
		seeds[i]=seeds[i].strip().lower()
	getandparseurls(sys.argv[1])
	file='outputfiles/htmloutput.html'
	f=open(file,"r")
	data=f.read()
	data=data.split('**************  New PAGE *********************')
	print "Looking for patterns\n"
	while '' in data: data.remove('')
	for i in data:
		expandUsingPatterns(i,seeds)
	f.close()
	d=Counter(result)
	d=sorted(d,key=d.__getitem__,reverse=True)
	for i in seeds:
		if i in d:
			d.remove(i)
	for i in range(min(10,len(d))):
		print i+1,":",d[i]

main()
