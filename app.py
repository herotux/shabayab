from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acnttoiban/hekmat')
def hekmat():
    return render_template('/acnttoiban/hekmat.html')

@app.route("/acnttoiban/hekmat", methods=["POST"])
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
    return render_template('/acnttoiban/hekmat.html',iban=iban)

@app.route('/acnttoiban/mellat')
def mellat():
    return render_template('/acnttoiban/mellat.html')

@app.route("/acnttoiban/mellat", methods=["POST"])
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
    return render_template('/acnttoiban/mellat.html',iban=iban)


@app.route('/acnttoiban/melli')
def melli():
    return render_template('/acnttoiban/melli.html')

@app.route("/acnttoiban/melli", methods=["POST"])
def melliconvert():
    an = request.form['accountnumber']
    accounttype = request.form['accounttype']
    #Bank identify number for melli 
    bi = "017"
    #Iran code
    cc = "IR"
    if accounttype == "1" :
        #sepordeh
        bban =  bi + "00000" + str(an)
    elif accounttype == "2" :
        #tas,hilat
        bban =  bi + "10000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/melli.html',iban=iban)

@app.route('/acnttoiban/ayandeh')
def ayandeh():
    return render_template('/acnttoiban/ayandeh.html')

@app.route("/acnttoiban/ayandeh", methods=["POST"])
def ayandehconvert():
    an = request.form['accountnumber']
    #Bank identify number for ayandeh 
    bi = "062"
    #Iran code
    cc = "IR"
    bban =  bi + "000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/ayandeh.html',iban=iban)

@app.route('/acnttoiban/saderat')
def saderat():
    return render_template('/acnttoiban/saderat.html')

@app.route("/acnttoiban/saderat", methods=["POST"])
def saderatconvert():
    an = request.form['accountnumber']
    #Bank identify number for saderat 
    bi = "019"
    #Iran code
    cc = "IR"
    bban =  bi + "000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/saderat.html',iban=iban)

@app.route('/acnttoiban/keshavarzi')
def keshavarzi():
    return render_template('/acnttoiban/keshavarzi.html')

@app.route("/acnttoiban/keshavarzi", methods=["POST"])
def keshavarziconvert():
    an = request.form['accountnumber']
    #Bank identify number for keshavarzi 
    bi = "016"
    #Iran code
    cc = "IR"
    bban =  bi + "0000000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/keshavarzi.html',iban=iban)


@app.route('/acnttoiban/refah')
def refah():
    return render_template('/acnttoiban/refah.html')

@app.route("/acnttoiban/refah", methods=["POST"])
def refahconvert():
    an = request.form['accountnumber']
    #Bank identify number for refah 
    bi = "013"
    #Iran code
    cc = "IR"
    bban =  bi + "01000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/refah.html',iban=iban)

@app.route('/acnttoiban/tejarat')
def tejarat():
    return render_template('/acnttoiban/tejarat.html')

@app.route("/acnttoiban/tejarat", methods=["POST"])
def tejaratconvert():
    an = request.form['accountnumber']
    #Bank identify number for tejarat 
    bi = "018"
    #Iran code
    cc = "IR"
    bban =  bi + "0000000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/tejarat.html',iban=iban)

@app.route('/acnttoiban/saman')
def saman():
    return render_template('/acnttoiban/saman.html')

@app.route("/acnttoiban/saman", methods=["POST"])
def samanconvert():
    an = request.form['accountnumber']
    #Bank identify number for saman
    bi = "056"
    #Iran code
    cc = "IR"
    bban =  bi + "0" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/saman.html',iban=iban)

@app.route('/acnttoiban/parsian')
def parsian():
    return render_template('/acnttoiban/parsian.html')

@app.route("/acnttoiban/parsian", methods=["POST"])
def parsianconvert():
    an = request.form['accountnumber']
    #Bank identify number for parsian
    bi = "054"
    #Iran code
    cc = "IR"
    bban =  bi + "01219" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/parsian.html',iban=iban)

@app.route('/acnttoiban/shahr')
def shahr():
    return render_template('/acnttoiban/shahr.html')

@app.route("/acnttoiban/shahr", methods=["POST"])
def shahrconvert():
    an = request.form['accountnumber']
    #Bank identify number for shahr
    bi = "061"
    #Iran code
    cc = "IR"
    bban =  bi + "0000000" + str(an)
    #check digits
    cd=str(98 - int(bban + "182700") % 97)
    if len(cd) <2 :
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/shahr.html',iban=iban)