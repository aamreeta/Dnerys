import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer,word_tokenize


#Train the testing data
#train_text = state_union.raw("2005-GWBush.txt")
#sample_text = "The sailor dogs the hatch"
sample_text = state_union.raw("2006-GWBush.txt")

#custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = word_tokenize(sample_text)
#print('******************')
#print(tokenized)
 #for words in tokenized: 
tagged = nltk.pos_tag(tokenized)


#for w in tagged:
 #print(w[1][0])
 #print("******************")

chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
chunkParser = nltk.RegexpParser(chunkGram)
chunked = chunkParser.parse(tagged)
#chunked.draw()
#print(chunked)
for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
 print(subtree)

