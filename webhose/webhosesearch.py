import webhose
webhose.config(token="35699326-6aec-4b1e-8aa4-a0794ba56819")
r = webhose.search("python java")
for i in xrange(0,20):
	print r.posts[i].title
#	print "\n"
