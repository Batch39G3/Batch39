import json
from pyrfc3339 import generate
from web3 import Web3   
from abis import abis
import random
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
abise = abis()
abi=json.loads(abise)
address=web3.toChecksumAddress("0x25352934f210d1e3b0eF841ce8e20aa2A938562D")
contract=web3.eth.contract(address=address,abi=abi)


############################################################## user verification using aadhar ##############################################################
def add_aadhar(aadhar_no):
     web3.eth.defaultAccount = web3.eth.accounts[0]
     h=contract.functions.aadhar_user(str(aadhar_no)).transact()
     web3.eth.waitForTransactionReceipt(h)
     return h
     

def verify_user(aadhar_no):
  if len(str(aadhar_no))==12:  
    a=0
    web3.eth.defaultAccount = web3.eth.accounts[0]
    h=contract.functions.get_adhaar_status(str(aadhar_no)).call()
    #print(h)
    if h=="Not Voted":
      #sett=add_aadhar(aadhar_no)
      #print(sett)
      return "not voted"
    else:
      return "You Already Voted"
  else:
    return "Invalid Aadhar Number" 

#####################################################################################################################################################
def ownerr():
    web3.eth.defaultAccount=web3.eth.accounts[0]
    h=contract.functions.owner().call()
    return h


def generate_add():
    a=random.randint(1,9)
    b=web3.eth.accounts[a]
    return b,a

def authorisess(b):
    web3.eth.defaultAccount = web3.eth.accounts[0]
    h=contract.functions.authorize(str(b)).transact()
    h=web3.eth.waitForTransactionReceipt(h)
    #print(h)
    return h






def add_candidate(name,region,party):
    web3.eth.defaultAccount = web3.eth.accounts[0]
    h=contract.functions.addCandidate(str(name),str(region),str(party)).transact()
    h=web3.eth.waitForTransactionReceipt(h)
    #print(h)
    return "sucess"



     

#####################################################################################################################################################

def vote(name,region,party,i):
  web3.eth.defaultAccount = web3.eth.accounts[i]
  print(web3.eth.defaultAccount)
  h=contract.functions.vote(str(name),str(region),str(party)).transact()
  #print(h)
  h=web3.eth.waitForTransactionReceipt(h)
  return h
  
def get_candidates():
    l=[]
    s=contract.functions.get_no_candidates().call()
    print(s)
    for i in range (int(s)):
      a=contract.functions.candidates(i).call()
      l.append(a)
    return l


def get_region_candidates(region):
    l=get_candidates()
    r=[]
    for i in range(len(l)):
       if l[i][2]==region:
         r.append(l[i][3])
    return r 

def get_candidate_names(region):
    namess={}
    l=get_candidates()
    for i in range(len(l)):
       if l[i][2]==region:
         namess[l[i][3]]=l[i][0]
    return namess
  

#a=get_candidate_names("bang")
#print(type(a))
def addressstore(c):
  with open("address.txt","a+") as f:
      f.write(str(c)+"\n")
      
def checkaddress(a):
    file = open("address.txt")
    if(a in file.read()):
        return True
    else:
        return False

def generatee():
    for i in range(1,len(web3.eth.accounts)):
        #print(web3.eth.accounts[i])
      if i<=(len(web3.eth.accounts)-2):
        a=web3.eth.accounts[i]
        if checkaddress(a)==False and i<=(len(web3.eth.accounts)-2):
            addressstore(a)
            #print(a)
            return [a,i]
      else:
            return(" no more address ")


#a=generatee()
#print(a)