import re
from flask import Flask, request, render_template





parties=["zania","vijetha","KP","bhu"]



app = Flask(__name__)

@app.route('/')
def my_form():
    #return render_template('home.html')
    return render_template('admin.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['aadhar_num']
    return render_template('otp.html')

@app.route('/otp',methods = ['POST','GET'])
def verification():
    otp_text = request.form['otp']
    return render_template('party.html',n_party=parties,n=len(parties))

@app.route('/vote',methods = ['POST','GET'])
def vote():
    candi = request.form['likebtn']
    return candi

@app.route('/admin',methods = ['POST','GET'])
def admine():
    candi_name = request.form['party[]']
    
    return candi_name[1]






if __name__ == '__main__':
    app.run(debug=True)