import sys
import math
ipfilename=sys.argv[1]

uid=sys.argv[2]
moviename=sys.argv[3]
k=int(sys.argv[4])

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
 top_k=sorted(pearson_scores,key=pearson_scores.get,reverse=True)[:k]
 k_nn={key:pearson_scores[key] for key in top_k}
 #print k_nn
 return k_nn
   
def Predict(uid, movie, k_nn):
 num=0
 den=0
 for user in k_nn:
  if movie in ratings[user]:
   num+=k_nn[user]*ratings[user][movie]
   den+=k_nn[user]
 return num/den
 

def main():
 #populate ratings dataset
 loadratings(ipfilename)
 #print ratings
 #identify knn
 k_nn=K_nearest_neighbors(uid,k)
 #calculate prediction
 prediction=Predict(uid,moviename,k_nn)
 #print op
 for key in sorted(k_nn,key=k_nn.get,reverse=True):
  print key+' '+str(k_nn[key])
 print
 print
 print prediction
 

if __name__=="__main__":
 main()





