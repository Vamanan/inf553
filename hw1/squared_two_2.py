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
    mr.emit_intermediate((i,j),value)

def reducer(key, list_of_values):
    # key: (i,k)
    # value: corresponding values
    mr.emit((key[0],key[1],sum(list_of_values)))
     
       

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
