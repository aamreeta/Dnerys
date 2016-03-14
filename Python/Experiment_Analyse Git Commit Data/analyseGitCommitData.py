
# coding: utf-8

# In[3]:

import pandas as pd
import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
from time import gmtime, strftime


# In[2]:
#Analyses commit statistics of d3.js codebase in git
df = pd.read_json('d3CommitLastyr.json')


# In[4]:

df['weekFormatted'] = df['week'].map(lambda x:strftime("%W,%Y-%m-%d", gmtime(x)))


# In[5]:

df


# In[10]:

#what week in the last year had the greatest number of commits.

maxCommit = df['total'].max()
#print "Maximum commit in last year is",maxCommit


# In[14]:

weekOfMaxCommit=df['weekFormatted'][df['total']==maxCommit].iloc[0]

print "The week of maximum commit is week",weekOfMaxCommit


# In[16]:

#Over the last year, what day of the week had the most commits?

commitPerDayDf=df['days']
totalCommitPerday=[sum(i) for i in zip(*commitPerDayDf)]

print "The total commits per day of the for the whole year are ",totalCommitPerday


# In[60]:

daysofTheWeekLst=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday']
dayOftheWeekIndex=totalCommitPerday.index(max(totalCommitPerday))
print daysofTheWeekLst[dayOftheWeekIndex]," has Maximum commits"


# In[61]:

bar_width=.35
opacity=.4
index = [1, 2, 3, 4, 5, 6,7]

plt.title('Number of commits per day of the week')
#labels
plt.xlabel("Days of the week")
plt.ylabel("Number of Commits")

plt.bar(index,totalCommitPerday,bar_width,alpha=opacity,color='g')
plt.xticks(index , ('Sun', 'Mon', 'Tues', 'Wed', 'Thurs','Fri','Sat'))
plt.show()

# In[47]:




# In[ ]:



