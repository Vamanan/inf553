import sys
import itertools
from operator import mul

ipfile=sys.argv[1]
support=int(sys.argv[2])
bucket_size=int(sys.argv[3])

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def genhash1(tuple):
 return (sum([hash(x)for x in tuple]))%bucket_size

def genhash2(tuple):
 return reduce(mul,[hash(x)for x in tuple],1)%bucket_size

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
  
 
singleton={}
#print baskets
#populate singleton counts
for basket in baskets:
 for item in basket:
  if item not in singleton:
   singleton[item]=1
  else:
   singleton[item]+=1

c=singleton
#print c
#print(singleton)
#----END OF PREPROCESSING----

i=1

while(True):
 #----PASS1------
 #find li
 li=[key for key in c.keys() if c[key]>=support]
 li.sort()
 #print li
 
 if len(li)==0:
  break
 
 buckets1=[0]*bucket_size
 buckets2=[0]*bucket_size

 #hash combinations to buckets
 for basket in baskets:
  combinations=gencombinations(basket,i+1)
  #print str(pairs)+' '+str(basket)
  for c in combinations:
   hashvalue1=genhash1(c)
   hashvalue2=genhash2(c)
   #print(str(pair)+' '+str(hashvalue))
   buckets1[hashvalue1]+=1
   buckets2[hashvalue2]+=1
# print buckets1
# print buckets2
 #print(buckets)if i>=2

 if i>=2:
  print {i:buckets1[i] for i in range(len(buckets1))}
  print {i:buckets2[i] for i in range(len(buckets2))}
  print [list(x) for x in li]
 else:
  print li
 print

 #change to bitvector
 bitvector1=buckets1
 bitvector2=buckets2
 for x in range(len(buckets1)):
  bitvector1[x]=1 if buckets1[x]>=support else 0
  bitvector2[x]=1 if buckets2[x]>=support else 0
 #print(bitvector)

 #-----END OF PASS1------
 #-----PASS2------


 cnext={}

 #find cn+1
 #print 'blah'
 #print baskets
 for basket in baskets:
  #print basket
  #print 'PASS2'
  combinations=gencombinations(basket,i+1)
  #print combinations
  for comb in combinations:
   subsets=gencombinations(comb,i)
   #print(str(subsets)+' as '+str(comb))
   if set(subsets).issubset(li):
    if(bitvector1[genhash1(comb)]==1 and bitvector2[genhash2(comb)]==1):
     if comb in cnext:
      cnext[comb]+=1
     else:
      cnext[comb]=1

 #print cnext
  
 


 c=cnext
 #print c
 
 #if(len(c)==0):
 # break
 
 i+=1

 #------END OF PASS2----
  
'''
#print(candidatepairs)

candidatepaircounts={}
#now count only candidate pairs
for basket in baskets:
 pairs=genpairs(basket)
 for pair in pairs:
  if pair in candidatepairs:
   if pair in candidatepaircounts:
    candidatepaircounts[pair]+=1
   else:
    candidatepaircounts[pair]=1

#print candidatepaircounts

pairop=[t for t in candidatepaircounts.keys() if candidatepaircounts[t]>=support]

pairop.sort()
print
print
print pairop

''' 
 






  

