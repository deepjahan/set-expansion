from wikiapi import WikiApi
def wiki_search(query):
	wiki = WikiApi()
	wikiurls=[]
	lst=query.split(",")
	num = 10/len(lst)
#	print num
	for i in lst:
		results = wiki.find(i)
		cnt=0
		for j in results:
			cnt=cnt+1
			article = wiki.get_article(j)
			wikiurls.append(article.url)
			if cnt==num:
				break
	return wikiurls


