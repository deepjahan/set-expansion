from py_bing_search import PyBingSearch

def bing_search(query):
	bing = PyBingSearch('rLSasvRW9cvlU5fG9hoSGjJG2M1eIjR+Ld27nFC9Pj8=')
	buildquery=query.replace(',',' ')
	result_list = bing.search_all(query, limit=10, format='json')
	bingurls=[]
	for result in result_list:
		 bingurls.append(result.url)
	return bingurls
