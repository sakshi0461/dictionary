import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json",'r'))

def fun2(word):
   item =0
   for item in range(len(data[word])):
       print(data[word][item])
def fun3(word):
    word2=get_close_matches(word,data.keys(),1)
    ask=input("do you mean %s" % word2[0] +" ? yes or no\n")
    if ask == "yes":
        fun2(word2[0])
    else:
       print("word doesnot exist")

def fun(word):
  if word in data:
   return fun2(word)
  else:
   fun3(word)
word=input("enter a word\n")
fun(word.lower())