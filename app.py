from flask import Flask, request, render_template,url_for,redirect
from aadhar import aadhar_details
from otp import otp_generate
from links import *
import json

n=0

#parties=["A","B","C","D"]


app = Flask(__name__)

@app.route('/')
def my_form():
    a=region_votes(n)
    return render_template('home.html',a=a)
    #return render_template('admin.html')

#############################################################################################
@app.route('/', methods=['GET','POST'])
def my_form_post():     
    if request.method == "POST":
        try:
           if request.form['admin_button'] == "ADMIN":
               return redirect(url_for('admin_login'))
        except:
            a=region_votes(0) #give thresold for getting no of votes
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
               a=region_votes(0)
               return render_template("home.html",error="Aadhar number not found",a=a)
               #return redirect(url_for("my_form_post",erro="Aadhar number not found"))          
       return render_template("otp.html")

    elif  request.method == "POST":
        otp_text = request.form['otp']
        if ph_no != "not found":
            if str(otp_text) == str(otp):
                if len(region_lst)==0:
                  a=region_votes(0)
                  return render_template("home.html",error="No Candidates in this region",a=a)
                else:
                    a=verify_user(a_no)
                    if a=="not voted":
                        return redirect(url_for('votss',region=region,a_no=a_no))
    
                        #return render_template("party.html",n_party=region_lst)
                        #return str(region_lst)
                    else:
                        a=region_votes(0)
                        return render_template("home.html",error="Already Voted",a=a)
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
               a=region_votes(0)
               return render_template("home.html",error="Thanks for voting",a=a)


@app.route('/admin_login',methods = ['POST','GET'])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    elif request.method == "POST":
        try:
            admin_id = request.form['admin_id']
            admin_password= request.form['admin_pass']
        
            if admin_id == "admin" and admin_password == "admin":
                 return redirect(url_for('admin'))
            else:   
               return render_template("admin_login.html",error="Wrong Credentials")
        except:
            a=region_votes(0)
            return render_template("home.html",a=a)

               

@app.route('/admin',methods = ['POST','GET'])
def admin():
    if request.method == "GET":
        a=region_votes(0)
        return render_template("admin.html",a=a)
    elif request.method == "POST":
        try:           
            data=request.get_data()
            if len(str(data)) !=3:
               print(str(data))
               a_data=json.loads(data)
               a=candi_add(a_data)
               #print(a)
            #data=json.loads(str(data))
            #print(data)
            a=region_votes(0)
            #print(a)
            return render_template('admin.html', Error="Added Candidates")
        except:
            a=region_votes(0)
            return render_template("home.html",a=a)
    return "not post request"

if __name__ == '__main__':
    app.run(debug=True)