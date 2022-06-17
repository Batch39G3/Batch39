from eth_account import Account
from matplotlib.pyplot import get
from links import *

aadhar={"485820350395":{"aadhar":"485820350395","region":"Karnataka","phoneno":"7619670012"},
         "485820350397":{"aadhar":"485820350391","region":"Karnataka","phoneno":"7619670013"}}

######################################
#import random
#adhar="485820350366"
#user=verify_user(adhar)
#print(user)
#voted_add={}


#owner=ownerr()
#print(owner)



"""
c,i=generate_add()
print(c)
print(i)
if c not in voted_add:
  voted_add[c]=adhar
  auth=authorisess(c)
else:
    while c not in voted_add:
      c=generate_add()
      if c not in voted_add:
        voted_add[c]=adhar
        auth=authorisess(c)
        # print(auth)
        break
"""
#vott=vote('Rajesh', 'Karnataka',i)
#print(vott)
#res=get_candidate_details(0) 
#print(res)  
#####################
#add=add_candidate("sai","andra","Bjp")
#print(add)
#res=get_candidate_details(2)
#rint(res)
#auth=authorisess("0x20dfc31dEAecB16aA317AF0A54653B5334224B2D")
#print(auth["status"])
#vott=vote('pavan','bang',"cong",2)
#print(vott["status"])
#res=get_candidates()
#print(res)
#region=get_region_candidates("bang")
#print(region)
#owner=ownerr()
#print(owner)

    
#addressstore("fi")

#print(checkaddress("fi"))

#i=1
#address=web3.eth.accounts[i]
#print(address)


def get_votes(thre):
  votes=[]
  party=[]
  region=[]
  f_votes=[]
  res=get_candidates()
  for i in res :
      votes.append(i[1])
      party.append(i[3])
      region.append(i[2])

  if thre >0:
      for i in votes:
        if i%thre==0:
          f_votes.append(i)
        else:
           f_votes.append(0)
      return f_votes,party,region
  else:
      return votes,party,region
#a=get_votes(1)
#print(a)
  
#a=get_region_votes(res) 
#print(a)     
    
