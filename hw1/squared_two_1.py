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
      mr.emit_intermediate(j,(i,value))
      mr.emit_intermediate(i,(j,value))	    

def reducer(key, list_of_values):
    # key: (i,k)
    # value: corresponding values
    pairlist=itertools.combinations(list_of_values,2)
    opdict={}
    for t in pairlist:
     opdict[(t[0][0],t[1][0])]=t[0][1]*t[1][1]
    for key in opdict:
     mr.emit([key[0],key[1],opdict[key]])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
