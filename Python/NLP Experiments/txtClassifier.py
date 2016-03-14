import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC ,NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import pickle


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



#print(movie_reviews.categories())
#print(list(movie_reviews.words('neg/cv997_5152.txt')))

documents = []

for category in movie_reviews.categories():
 for fileid in movie_reviews.fileids(category):
   documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)

#print(documents[1])

all_words = []
for w in movie_reviews.words():
 all_words.append(w.lower())
 
#print(all_words)

all_words = nltk.FreqDist(all_words)
#print(all_words.keys())

word_features = list(all_words.keys())[:3000]

#print(word_features)

def find_features(document):
 words = set(document)
 features = {}
 for w in word_features:
   features[w] = (w in words) 
 return features 
 
#print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_features(rev),category) for (rev,category) in documents]
#print(featuresets[1])

training_set = featuresets[:1900]
testing_set = featuresets[1900:]



#classifier = nltk.NaiveBayesClassifier.train(training_set)
#Using pickled classifier
classifier_f = open("NaiveBayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
#print("Original Classifier classification::",classifier.classify(testing_set[0][1]))
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

#Pickle
#save_classifier = open("NaiveBayes.pickle","wb")
#pickle.dump(classifier,save_classifier)
#save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
#print("MNB Classifier classification::",MNB_classifier.classify(testing_set[0][1]))
print("MNB classifier accuracy percent:",(nltk.classify.accuracy(MNB_classifier, testing_set))*100)

#GNB_classifier = SklearnClassifier(GaussianNB())
#GNB_classifier.train(training_set)
#print("Gaussian classifier accuracy percent:",(nltk.classify.accuracy(GNB_classifier, testing_set))*100)

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BNB classifier accuracy percent:",(nltk.classify.accuracy(BNB_classifier, testing_set))*100)

#LogisticRegression,SGDClassifier
#SVC, LinearSVC, NuSVC
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression classifier accuracy percent:",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier classifier accuracy percent:",(nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC classifier accuracy percent:",(nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC classifier accuracy percent:",(nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(classifier,MNB_classifier,BNB_classifier,LogisticRegression_classifier,SGDClassifier_classifier,LinearSVC_classifier,NuSVC_classifier)

print("Voted classifier accuracy percent:",(nltk.classify.accuracy(voted_classifier, testing_set))*100)

print("clasiification:", voted_classifier.classify(testing_set[0][0]),"Confidence %",voted_classifier.confidence(testing_set[0][0])*100)

