import re
from collections import Counter, defaultdict
import operator

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
				if i.isalpha():
					result.append(i)

def main():
	seeds=['php','java','perl','python']
	file='htmloutput.html'
	f=open(file,"r")
	data=f.read()
	data=data.split('**************  New PAGE *********************')
	while '' in data: data.remove('')
	for i in data:
		expandUsingPatterns(i,seeds)
	f.close()
	return Counter(result)

print main()
