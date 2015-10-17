import sys
import math
#ipfilename=sys.argv[1]
ipfilename='sample.tsv'
'''uid=sys.argv[2]
moviename=sys.argv[3]
k=sys.argv[4]'''

#holds all ratings. will be dictionary with keys=uid, value = {movie:rating} dict
ratings={}

def loadratings(filename):
 with open(filename) as f:
  for line in f:
   uid,rating,mname=line.rstrip().split('\t')
   if uid not in ratings:
    ratings[uid]={mname:float(rating)}
   else:
    ratings[uid][mname]=float(rating)

def pearsoncorrelation(u1,u2):
 commonmovies=list(set(ratings[u1].keys())&set(ratings[u2].keys()))
 u1_avg=sum(ratings[u1].values())/len(ratings[u1])
 u2_avg=sum(ratings[u2].values())/len(ratings[u2])
 num_sum=0
 den_sum_u1=0
 den_sum_u2=0
 for movie in commonmovies:
  num_sum+=(ratings[u1][movie]-u1_avg)*(ratings[u2][movie]-u2_avg)
  den_sum_u1+=(ratings[u1][movie]-u1_avg)**2
  den_sum_u2+=(ratings[u2][movie]-u2_avg)**2
 den_sum_u1=math.sqrt(den_sum_u1)
 den_sum_u2=math.sqrt(den_sum_u2)
 return num_sum/(den_sum_u1*den_sum_u2)
 
def K_nearest_neighbors(uid,k):
 pearson_scores={}
 for user in ratings:
  if user != uid:
   pearson_scores[user]=pearsoncorrelation(user,uid)
 k_nn={k:pearson_scores[k] for k in sorted(pearson_scores,key=pearson_scores.get,reverse=True)[:k]}
 return k_nn
   


def main():
 #populate ratings dataset
 loadratings(ipfilename)
 

if __name__=="__main__":
 main()





