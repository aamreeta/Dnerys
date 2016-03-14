import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC ,NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import pickle
from nltk.tokenize import word_tokenize

class VoteClassifier(ClassifierI):
 def __init__(self, *classifiers):
  self._classifiers = classifiers
 def classify(self, features):
   votes = []
   for c in self._classifiers:
    v = c.classify(features)
    votes.append(v)
   return mode(votes)
 def confidence(self,features):
  votes = []
  for c in self._classifiers:
   v = c.classify(features)
   votes.append(v)

  choice_votes = votes.count(mode(votes))
  conf = choice_votes / len(votes)
  return conf

'''
starting comment
#Training set
print("reading training data")
short_pos = open("TrainingData/positive.txt","r").read()
short_neg = open("TrainingData/negative.txt","r").read()


documents = []
all_words = []

#Part of speech tagging for better training of the algorithm
# j is adjective, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]

#The data needs to be a tuple
print("*******for positive data***********")
for p in short_pos.split('\n'):
 documents.append((p,"pos"))
 words = word_tokenize(p)
 pos = nltk.pos_tag(words)
 for w in pos:
  if w[1][0] in allowed_word_types:
   all_words.append(w[0].lower())


print("**********for negative data********************")
for p in short_neg.split('\n'):
 documents.append((p,"neg"))
 words = word_tokenize(p)
 pos = nltk.pos_tag(words)
 for w in pos:
  if w[1][0] in allowed_word_types:
   all_words.append(w[0].lower())

#Pickle the documents
print("Pickle the documents")
save_documents = open("pickled_algorithms/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()
ending comments
'''
print("***********reading documents**************")
documents_f = open("pickled_algorithms/documents.pickle","rb")
documents = pickle.load(documents_f)
documents_f.close()

'''
****starting comments
all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(10))


word_features = list(all_words.keys())[:5000]

print("****Pickle word_features***")

save_word_features = open("pickled_algorithms/word_features5k.pickle","wb")
pickle.dump(word_features,save_word_features)
save_word_features.close()
****ending comments
'''
word_features5k = open("pickled_algorithms/word_features5k.pickle","rb")
word_features = pickle.load(word_features5k)
word_features5k.close()

def find_features(document):
 words =  word_tokenize(document)
 features = {}
 for w in word_features:
   features[w] = (w in words) 
 return features 
 

print("******Creating featuresets*********")
'''
starting comments
#
#featureset looks something like ({'gore-free': False, 'expanded': True,},'pos')
#

featuresets = [(find_features(rev),category) for (rev,category) in documents]
#print(featuresets[1])
ending comments
'''
featuresets_f = open("pickled_algorithms/featuresets.pickle","rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)
print("Featuresets len",len(featuresets))

training_set = featuresets[:10000]
testing_set = featuresets[10000:]



#classifier = nltk.NaiveBayesClassifier.train(training_set)
#Using pickled classifier
classifier_f = open("pickled_algorithms/nltkNaiveBayes5k.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
#print("Original Classifier classification::",classifier.classify(testing_set[0][1]))
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

#Pickle
#save_classifier = open("pickled_algorithms/nltkNaiveBayes5k.pickle","wb")
#pickle.dump(classifier,save_classifier)
#save_classifier.close()


MNBClassifier_f = open("pickled_algorithms/MNB_classifier5k.pickle","rb")
MNB_classifier = pickle.load(MNBClassifier_f)
MNBClassifier_f.close()
#print("MNB Classifier classification::",MNB_classifier.classify(testing_set[0][1]))
print("MNB classifier accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)

#Pickle MNB Classifier
#MNB_classifier = SklearnClassifier(MultinomialNB())
#MNB_classifier.train(training_set)
#save_MNBClassifier = open("pickled_algorithms/MNB_classifier5k.pickle","wb")
#pickle.dump(MNB_classifier,save_MNBClassifier)
#save_MNBClassifier.close()


#BNB_classifier = SklearnClassifier(BernoulliNB())
#BNB_classifier.train(training_set)
BNBClassifier_f = open("pickled_algorithms/BNB_classifier5k.pickle","rb")
BNB_classifier = pickle.load(BNBClassifier_f)
BNBClassifier_f.close()
print("BNB classifier accuracy percent:",(nltk.classify.accuracy(BNB_classifier, testing_set))*100)

#pickle Bernoulli
#save_BNBClassifier = open("pickled_algorithms/BNB_classifier5k.pickle","wb")
#pickle.dump(BNB_classifier,save_BNBClassifier)
#save_BNBClassifier.close()


#LogisticRegression,SGDClassifier
#SVC, LinearSVC, NuSVC


#LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
#LogisticRegression_classifier.train(training_set)
LogisticRegression_classifier_f = open("pickled_algorithms/LogisticRegression_classifier5k.pickle","rb")
LogisticRegression_classifier = pickle.load(LogisticRegression_classifier_f)
LogisticRegression_classifier_f.close()
print("LogisticRegression classifier accuracy percent:",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

#pickle Logistic regression
#save_LogisticRegression_classifier = open("pickled_algorithms/LogisticRegression_classifier5k.pickle","wb")
#pickle.dump(LogisticRegression_classifier,save_LogisticRegression_classifier)
#save_LogisticRegression_classifier.close()



#SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
#SGDClassifier_classifier.train(training_set)
SGDClassifier_classifier_f = open("pickled_algorithms/SGDC_classifier5k.pickle","rb")
SGDClassifier_classifier = pickle.load(SGDClassifier_classifier_f)
SGDClassifier_classifier_f.close() 
print("SGDClassifier classifier accuracy percent:",(nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

#Pickle SGD classifier
#save_SGDClassifier_classifier = open("pickled_algorithms/SGDC_classifier5k.pickle","wb")
#pickle.dump(SGDClassifier_classifier,save_SGDClassifier_classifier)
#save_SGDClassifier_classifier.close()



#LinearSVC_classifier = SklearnClassifier(LinearSVC())
#LinearSVC_classifier.train(training_set)
LinearSVC_classifier_f = open("pickled_algorithms/LinearSVC_classifier5k.pickle","rb")
LinearSVC_classifier = pickle.load(LinearSVC_classifier_f)
LinearSVC_classifier_f.close()
print("LinearSVC classifier accuracy percent:",(nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

#Pickle Linear SVC

#save_LinearSVC_classifier = open("pickled_algorithms/LinearSVC_classifier5k.pickle","wb")
#pickle.dump(LinearSVC_classifier,save_LinearSVC_classifier)
#save_LinearSVC_classifier.close()


voted_classifier = VoteClassifier(classifier,MNB_classifier,BNB_classifier,LogisticRegression_classifier,LinearSVC_classifier)

#print("Voted classifier accuracy percent:",(nltk.classify.accuracy(voted_classifier, testing_set))*100)

#print("clasiification:", voted_classifier.classify(testing_set[0][0]),"Confidence %",voted_classifier.confidence(testing_set[0][0])*100)

def sentiment(text):
 feats = find_features(text)
 return voted_classifier.classify(feats),voted_classifier.confidence(feats)
