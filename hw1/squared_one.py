import MapReduce
import sys
import re
from operator import mul
from collections import defaultdict
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
      mr.emit_intermediate((i,k),(j,value))
      mr.emit_intermediate((k,j),(i,value))	    

def reducer(key, list_of_values):
    # key: (i,k)
    # value: corresponding values
    total = 0
    jdict=defaultdict(list)
    proddict={}
    #print (key,list_of_values)
    for v in list_of_values:
     jdict[v[0]].append(v[1])
    #print jdict
    for jkey in jdict:
     proddict[jkey]=reduce(mul,jdict[jkey],1) if len(jdict[jkey])>1 else 0
    mr.emit((key[0],key[1],sum(proddict.values())))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
