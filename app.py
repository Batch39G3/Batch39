from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')
    #return render_template('party.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['aadhar_num']
    return render_template('otp.html')

@app.route('/otp',methods = ['POST'])
def verification():
    otp_text = request.form['otp']
    return otp_text






if __name__ == '__main__':
    app.run(debug=True)