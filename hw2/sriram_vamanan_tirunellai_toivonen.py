import sys
import random
import itertools
ipfile=sys.argv[1]
support=int(sys.argv[2])

fraction=0.4
samplesupport=fraction*support
print 'samplesupport='+str(samplesupport)
def gencombinations(l,k):
 #print 'l='+str(l)
 #print 'k='+str(k)
 m=[]
 if k ==1:
  m=[x for x in l]
  #print m
  return m
 else:
  for t in itertools.combinations(list(l),k):
   m.append(t)
  #print m
  return m



baskets=[]
#---PREPROCESSING---
#populate baskets
with open(ipfile) as f:
 for line in f:
  basket=line.rstrip().split(',')
  basket.sort()
  baskets.append(basket)
  


#sample basket
samplebaskets=random.sample(baskets,int(fraction*len(baskets)))

singleton={}
#print baskets
#populate singleton counts
for basket in samplebaskets:
 for item in basket:
  if item not in singleton:
   singleton[item]=1
  else:
   singleton[item]+=1

c=singleton

i=1
iterations=1

while(True):
 
 #generate li
 if(i>=2):
  li=[x for x in c if c[x]>=samplesupport]
 else:
  actualcount={}
  for basket in baskets:
   for item in basket:
    if item not in actualcount:
     actualcount[item]=1
    else:
     actualcount[item]+=1
  li=[x for x in actualcount if actualcount[x]>=support]  
 li.sort()
 print 'li='+str(li)
 if len(li)==0:
  break
 cnext={}
 #GENERATE cn+1
 for basket in samplebaskets:
  combinations=gencombinations(basket,i+1)
  for comb in combinations:
   subset=gencombinations(comb,i)
   if set(subset).issubset(li):
    if comb in cnext:
     cnext[comb]+=1
    else: 
     cnext[comb]=1
 
 print 'cnext='+str(cnext)
 c=cnext
 
 #compute ln+1
 lnext=[x for x in cnext if cnext[x]>=samplesupport]
 lnext.sort()
 print 'lnext='+str(lnext)
 li=[set(x) for x in li]

 liunion=set.union(*li)
 liunion=list(liunion)
 liunion.sort()
 
 licombs=gencombinations(liunion,i+1)
 
 #generate negborder
 negborder=[]
 for licomb in licombs:
  if licomb not in lnext:
   negborder.append(licomb)

 print 'negborder='+str(negborder)
 if(len(negborder)==0):
  print iterations
  print fraction
  print lnext
 else:
  #generate actual counts
  actualcounts={}
  falsenegs=[]
  for basket in baskets:
   combinations=gencombinations(basket,i+1)
   for comb in combinations:
    if comb  in actualcounts:
     actualcounts[comb]+=1
    else:
     actualcounts[comb]=1
  falsenegs=[x for x in actualcounts if actualcounts[x]>=support and x in negborder]
  print'falenegs='+str(falsenegs)
  if len(falsenegs)==0:
   print iterations
   print fraction
   print lnext
   i+=1
  else:
   i=1
   iterations+=1  
   
 

 
 
