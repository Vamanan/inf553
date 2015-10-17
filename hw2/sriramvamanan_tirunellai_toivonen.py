import random
import sys
import itertools

ipfilename=sys.argv[1]
support=int(sys.argv[2])
fraction=0.4
samplesupport=fraction*0.8*support

def gencombinations(l,k):

 m=[]
 if k ==1:
  m=[x for x in l]

  return m
 else:
  for t in itertools.combinations(list(l),k):

   m.append(t)
  return m

lanswers=[]

baskets=[]

with open(ipfilename) as f_in:
 for line in f_in:
  basket=line.rstrip().split(',')
  basket.sort()
  baskets.append(basket)

i=1
iterations=1
c={}
li=[]
samplebaskets=[]
#BEGIN APRIORI WITH NEGBORDER CALCULATION
while(True):


 if i==1:
  lanswers=[]
  c={}	#resample if i=1
  samplebaskets=random.sample(baskets,int(fraction*len(baskets)))
  for basket in samplebaskets:
   for item in basket:
    if item not in c:
     c[item]=1
    else:
     c[item]+=1
 li=[x for x in c if c[x]>=samplesupport]
 if len(li)==0:
  print iterations
  print fraction
  for l in lanswers:
   l.sort()
   m=[list(x) for x in l]
   print m
   print
  break
 #calculatenegborder
 negborder=list(set(c.keys())-set(li))
 #check if anything in negborder is frequent in overall data
 actualcounts={}

 for basket in baskets:
  combinations=gencombinations(basket,i)
  for comb in combinations:
   if comb in actualcounts:
    actualcounts[comb]+=1
   else:
    actualcounts[comb]=1

 falsenegs=[x for x in negborder if actualcounts[x]>=support]
 if len(falsenegs)>0:
  i=1
  iterations+=1
 else:
  #eliminate false positives
  li=[x for x in li if actualcounts[x]>=support]

  if len(li)>0:
   lanswers.append(li)
  cnext={}
  for basket in samplebaskets:
   combinations=gencombinations(basket,i+1)

   for comb in combinations:

    subset=gencombinations(comb,i)
    if set(subset).issubset(li):
     if comb in cnext:
      cnext[comb]+=1
     else: 
      cnext[comb]=1
  c=cnext
  i+=1
 
    


