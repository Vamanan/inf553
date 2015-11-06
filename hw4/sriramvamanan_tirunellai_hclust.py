import sys
import itertools
ipfilename=sys.argv[1]
k=sys.argv[2]
import heapq

data=[]
#load data
with open(ipfilename) as f:
 for line in f:
  l=line.rstrip().split(',')
  data.append(l)

#store just coordinates in a list
points={i:data[i][:len(data[i]-1)] for i in range(len(data))}

#create cluster mapping 
cluster_map={}

for i in range(len(data)):
 label=data[i][-1]

 if label not in cluster_map:
  cluster_map[label]=[i]
 else:
  cluster_map[label].append(i)

#store cluster distances
distances={} #key=distance;value=list of tuples each tuple is a cluster pair
#keep track of merged clusters
merged=[] #list of tuples; each tuple is a pair of clusters that are merged

def euclidian_dist(key1,key2):
 sum=0
 for i in range(len(points[key1])):
  sum+=(points[key1][i]-points[key2][i])**2
 return sum**0.5

def compute_dist:
 for p in itertools.combinations(points.keys(),2):
  dist=euclidian_dist(p[0],p[1])
  if dist not in distances:
   distances[dist]=[p]
  else:
   if p not in distances[dist]:
    distances[dist].append(p)
  
#HAC
def HAC():
 #first compute all pairwise distances
 compute_distances()
 #heapify
 heap=[]
 for item in distances:
  heapq.heappush(heap,item)
 #heap now is a heap of distances
 while len(merged)<=k-1:
  min_dist=heapq.heappop(heap)
  #check if this distance corresponds to that between merged clusters
  for pair in distances[min_dist]
  
    
  
 
 
