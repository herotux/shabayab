from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hekmat')
def hekmat():
    return render_template('hekmat.html')

@app.route("/hekmat", methods=["POST"])
def hekmatconvert():
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
    return render_template('hekmat.html',iban=iban)

@app.route('/mellat')
def mellat():
    return render_template('mellat.html')

@app.route("/mellat", methods=["POST"])
def mellatconvert():
    an = request.form['accountnumber']
    accounttype = request.form['accounttype']
    #Bank identify number for mellat
    bi = "012"
    #Iran code
    cc = "IR"
    if accounttype == "1" :
        bban =  bi + "00000000" + str(an)
    elif accounttype == "2" :
        bban =  bi + "01000000" + str(an)
    elif accounttype == "3" :
        bban =  bi + "02000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('mellat.html',iban=iban)
