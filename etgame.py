#!/usr/bin/env python
from random import choice

score = 0
adjectives_bad = {'evil': 1,'immoral': 1, 'wicked': 2, 'corrupt': 2,'sinful': 2,
                  'depraved': 3,'rotten': 2,'contaminated': 2, 'spoiled': 2, 
                  'tainted':3, 'harmful':1, 
                  'injurious':3, 'unfavorable':3, 'defective':2, 'inferior':2, 'imperfect':3,
                  'substandard':2, 'faulty':4, 'improper':3, 'inappropriate':2, 'unsuitable':2, 
                  'disagreeable':3, 'unpleasant':2, 'cross':3, 'nasty':2, 'unfriendly':3, 
                  'irascible':5, 'horrible':2, 'atrocious':5, 'outrageous':4, 'scandalous':4,
                  'infamous':4, 'wrong':2, 'noxious':6, 'sinister':6, 'putrid':6, 'snide':6, 
                  'deplorable':7, 'dismal':7, 'gross':2, 'heinous':10, 'nefarious':10, 'base':5, 
                  'obnoxious':4, 'detestable':9, 'despicable':9, 'contemptible':5, 'foul':7, 
                  'rank':6, 'ghastly':10, 'execrable':10}

random_word = choice(adjectives_bad.keys())

# Replaces %s with the variable after '%'
print "What is a synonym for '%s'?" % random_word
user_input = raw_input('--> ')
if user_input in adjectives_bad.keys():
  score = str(adjectives_bad[user_input])
else:
  score = 0

print "You chose '%s'. Your score is: %s!" % (user_input, score)


