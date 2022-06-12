from crypt import methods
from logging import error
import re
from flask import Flask, request, render_template,url_for,redirect
from grpc import Status
from aadhar import aadhar_details
from otp import otp_generate
from links import *



#parties=["A","B","C","D"]


app = Flask(__name__)

@app.route('/')
def my_form():
    #return render_template('home.html')
    return render_template('admin.html')

#############################################################################################
@app.route('/', methods=['GET','POST'])
def my_form_post():     
    if request.method == "POST":
       adhar_no = request.form['aadhar_num']
       return redirect(url_for('verification',adhar_no=adhar_no))
    
       

   

@app.route('/otp',methods = ['POST','GET'])
def verification():
    if request.method =="GET":
       global ph_no,status,otp,region_lst,a_no,region
       a_no=request.args.get('adhar_no')
       ph_no,region = aadhar_details(a_no)
       region_lst=get_region_candidates(region)
       namess=get_candidate_names(region)
       if ph_no != "not found":
          status,otp = otp_generate(ph_no)
       #print(ph_no,otp)
       if ph_no == "not found":
               return render_template("home.html",error="Aadhar number not found")
               #return redirect(url_for("my_form_post",erro="Aadhar number not found"))          
       return render_template("otp.html")

    elif  request.method == "POST":
        otp_text = request.form['otp']
        if ph_no != "not found":
            if str(otp_text) == str(otp):
                if len(region_lst)==0:
                  return render_template("home.html",error="No Candidates in this region")
                else:
                    a=verify_user(a_no)
                    if a=="not voted":
                        return redirect(url_for('votss',region=region,a_no=a_no))
    
                        #return render_template("party.html",n_party=region_lst)
                        #return str(region_lst)
                    else:
                        return render_template("home.html",error="Already Voted")
                        #return "voted"
            else:
               return render_template("otp.html",error="Wrong OTP")
               #return "Wrong OTP"
        


    
#vott=vote('pavan','bang',"cong",i)

###################################################################################################
@app.route('/vote',methods = ['POST','GET'])
def votss():
    if request.method =="GET":
          global region_lst,a_no
          region_lst=request.args.get('region')
          a_nos=request.args.get('a_no')
          region_ls=get_region_candidates(region_lst)
          return render_template("party.html",n_party=region_ls)
          #return str(region_ls)
    
    if request.method == "POST":
        candi = request.form['likebtn']
        namess=get_candidate_names(region_lst)
        c_name=namess[candi]
        a=generatee()
        i=a[1]
        address=web3.eth.accounts[int(i)]
        auth=authorisess(str(address))
        if str(auth["status"])==str(1):
            vott=vote(c_name,region_lst,candi,i)
            if str(vott["status"])==str(1):
               sett=add_aadhar(a_no)
               return render_template("home.html",error="Thanks for voting")
                        
               

@app.route('/admin',methods = ['POST','GET'])
def admine():
    candi_name=[]
    candi_name= request.form['name[]']  
    return candi_name






if __name__ == '__main__':
    app.run(debug=True)