import spacy 
import ngrams
nlp=spacy.load("en_core_web_sm")
sentence4="Machine learning(ML) is best platflorm".
doc=nlp(sentence)
unigram=ngrams(doc,1)
print("unigram:\n",list(unigram))
bigrams=ngrams(doc,2)
print("bigrams:\n",list(bigram))
trigram=ngrams(doc,3)
print("trigram:\n",list(trigram))