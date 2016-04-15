import operator
from gensim.models import word2vec
import pattern.en as en
def find_similarity(query):
	model1 = word2vec.Word2Vec.load_word2vec_format('./word2vec/wiki.model.bin', binary=True)
	print "Model loaded"
	print "\n"
	a=query.split(",")
	scores={}
	f=open('./indexfile','r')
	for i in a:
		for line in f:
			line=line.strip("\n")
			try:
				sc=model1.similarity(i,line)
			except:
				sc=0
#	print sc
			try:
				scores[line]=scores[line]+sc
			except:
				scores[line]=sc

	sorted_x = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)
	k=0
	print "Printing Results"
	print "\n"
	flag=0
	output=[]
	for key,value in sorted_x:
		if key in a:
			continue
		for j in a:
			if en.lemma(key)==j or en.lemma(j)==key:
				flag=1
		if flag==1:
			flag=0
			continue
		for ll in output:
			if en.lemma(key)==ll or en.lemma(ll)==key:
				flag=1
		if flag==1:
			flag=0
			continue
		k=k+1
		output.append(key)
		print k,":",key
		if k==10:
			break
	
