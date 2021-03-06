import MapReduce
import sys
import re
import itertools
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: itemsets
    # value: count of itemset in basket (1)
    keys = list(itertools.combinations(record,2))
    for itemset in keys:
      mr.emit_intermediate(itemset, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    if(total>=100):
     mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
