from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('text8')
model = word2vec.Word2Vec(sentences, size=200)
model.save_word2vec_format('text.model.bin', binary=True)
model1 = word2vec.Word2Vec.load_word2vec_format('text.model.bin', binary=True)
print model1.most_similar('man',number=10)
