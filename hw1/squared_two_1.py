import MapReduce
import sys
import re
from operator import mul
from collections import defaultdict
import itertools
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i,k), (k,j)
    # value: (j,a[i][j]) (i,a[i][j])
    i = record[0]
    j = record[1]
    value = record[2]	
    for k in range(5):
      mr.emit_intermediate(j,('a',i,value))
      mr.emit_intermediate(i,('b',j,value))	    

def reducer(key, list_of_values):
    # key: (i,k)
    # value: corresponding values
    adict={}
    bdict={}
    for t in list_of_values:
     key=(t[0],t[1])
     if(t[0]=='a'):
      if key in adict:
       continue
      else:
       adict[key]=t[2]
     elif(t[0]=='b'):
      if key in bdict:
       continue
      else:
       bdict[key]=t[2]

    for i in range(5):
     if(('a',i)not in adict):
      continue
     for k in range(5):
      if(('b',k)not in bdict):
       continue
      mr.emit([i,k,adict['a',i]*bdict['b',k]])
       

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
