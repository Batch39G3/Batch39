from eth_account import Account
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
#add=add_candidate("ram","bangr","con")
#print(add)
#res=get_candidate_details(2)
#rint(res)
#auth=authorisess("0xfAa35b9E28dE9624AE07be368c344a3524A30dB2")
#print(auth)
#vott=vote('pavan','bang',"cong",1)
#print(vott)
#res=get_candidates()
#print(res)
region=get_region_candidates("bang")
print(region)
#owner=ownerr()
#print(owner)