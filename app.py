from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/convert", methods=["POST"])
def convert():
    an = request.form['accountnumber']
    #Bank identify number for hekmat iranian
    bi = "065"
    #Iran code
    cc = "IR"
    bban =  bi + "00" + str(an)[:6] + "0" + str(an)[6:-1] + "00" + str(an)[-1]
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    print (iban)
    return render_template('index.html',iban=iban)    


