import MapReduce
import sys
import re

"""
tf df Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    dname = record[0]
    content = record[1].lower()
    words = content.split()
    for w in set(words):
     if re.match(r'\w+$', w):
      mr.emit_intermediate(w, [1,(dname,words.count(w))])

def reducer(key, list_of_values):
    # key: word
    # value: df along with individual tf tuples
    dftotal = 0
    pairs=[]
    for l in list_of_values:
      dftotal += l[0]
      pairs.append(l[1])
    mr.emit((key, dftotal,pairs))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
