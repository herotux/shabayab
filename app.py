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
    # Bank identify number for hekmat iranian
    bi = "065"
    # Iran code
    cc = "IR"
    bban = bi + "00" + str(an)[:6] + "0" + str(an)[6:-1] + "00" + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/hekmat.html', iban=iban)


@app.route('/acnttoiban/mellat')
def mellat():
    return render_template('/acnttoiban/mellat.html')


@app.route("/acnttoiban/mellat", methods=["POST"])
def mellatconvert():
    an = request.form['accountnumber']
    accounttype = request.form['accounttype']
    # Bank identify number for mellat
    bi = "012"
    # Iran code
    cc = "IR"
    if accounttype == "1":
        bban = bi + "00000000" + str(an)
    elif accounttype == "2":
        bban = bi + "01000000" + str(an)
    elif accounttype == "3":
        bban = bi + "02000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/mellat.html', iban=iban)


@app.route('/acnttoiban/melli')
def melli():
    return render_template('/acnttoiban/melli.html')


@app.route("/acnttoiban/melli", methods=["POST"])
def melliconvert():
    an = request.form['accountnumber']
    accounttype = request.form['accounttype']
    # Bank identify number for melli
    bi = "017"
    # Iran code
    cc = "IR"
    if accounttype == "1":
        # sepordeh
        bban = bi + "00000" + str(an)
    elif accounttype == "2":
        # tas,hilat
        bban = bi + "10000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/melli.html', iban=iban)


@app.route('/acnttoiban/ayandeh')
def ayandeh():
    return render_template('/acnttoiban/ayandeh.html')


@app.route("/acnttoiban/ayandeh", methods=["POST"])
def ayandehconvert():
    an = request.form['accountnumber']
    # Bank identify number for ayandeh
    bi = "062"
    # Iran code
    cc = "IR"
    bban = bi + "000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/ayandeh.html', iban=iban)


@app.route('/acnttoiban/saderat')
def saderat():
    return render_template('/acnttoiban/saderat.html')


@app.route("/acnttoiban/saderat", methods=["POST"])
def saderatconvert():
    an = request.form['accountnumber']
    # Bank identify number for saderat
    bi = "019"
    # Iran code
    cc = "IR"
    bban = bi + "000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/saderat.html', iban=iban)


@app.route('/acnttoiban/keshavarzi')
def keshavarzi():
    return render_template('/acnttoiban/keshavarzi.html')


@app.route("/acnttoiban/keshavarzi", methods=["POST"])
def keshavarziconvert():
    an = request.form['accountnumber']
    # Bank identify number for keshavarzi
    bi = "016"
    # Iran code
    cc = "IR"
    bban = bi + "0000000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/keshavarzi.html', iban=iban)


@app.route('/acnttoiban/refah')
def refah():
    return render_template('/acnttoiban/refah.html')


@app.route("/acnttoiban/refah", methods=["POST"])
def refahconvert():
    an = request.form['accountnumber']
    # Bank identify number for refah
    bi = "013"
    # Iran code
    cc = "IR"
    bban = bi + "01000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/refah.html', iban=iban)


@app.route('/acnttoiban/tejarat')
def tejarat():
    return render_template('/acnttoiban/tejarat.html')


@app.route("/acnttoiban/tejarat", methods=["POST"])
def tejaratconvert():
    an = request.form['accountnumber']
    # Bank identify number for tejarat
    bi = "018"
    # Iran code
    cc = "IR"
    bban = bi + "0000000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/tejarat.html', iban=iban)


@app.route('/acnttoiban/saman')
def saman():
    return render_template('/acnttoiban/saman.html')


@app.route("/acnttoiban/saman", methods=["POST"])
def samanconvert():
    an = request.form['accountnumber']
    # Bank identify number for saman
    bi = "056"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/saman.html', iban=iban)


@app.route('/acnttoiban/parsian')
def parsian():
    return render_template('/acnttoiban/parsian.html')


@app.route("/acnttoiban/parsian", methods=["POST"])
def parsianconvert():
    an = request.form['accountnumber']
    # Bank identify number for parsian
    bi = "054"
    # Iran code
    cc = "IR"
    bban = bi + "01219" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/parsian.html', iban=iban)


@app.route('/acnttoiban/shahr')
def shahr():
    return render_template('/acnttoiban/shahr.html')


@app.route("/acnttoiban/shahr", methods=["POST"])
def shahrconvert():
    an = request.form['accountnumber']
    # Bank identify number for shahr
    bi = "061"
    # Iran code
    cc = "IR"
    bban = bi + "0000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/shahr.html', iban=iban)


@app.route('/acnttoiban/dey')
def dey():
    return render_template('/acnttoiban/dey.html')


@app.route("/acnttoiban/dey", methods=["POST"])
def deyconvert():
    an = request.form['accountnumber']
    # Bank identify number for dey
    bi = "066"
    # Iran code
    cc = "IR"
    bban = bi + "000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/dey.html', iban=iban)


@app.route('/acnttoiban/sepah')
def sepah():
    return render_template('/acnttoiban/sepah.html')


@app.route("/acnttoiban/sepah", methods=["POST"])
def sepahconvert():
    an = request.form['accountnumber']
    # Bank identify number for sepah
    bi = "015"
    # Iran code
    cc = "IR"
    bban = bi + "0000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/sepah.html', iban=iban)


@app.route('/acnttoiban/karafarin')
def karafarin():
    return render_template('/acnttoiban/karafarin.html')


@app.route("/acnttoiban/karafarin", methods=["POST"])
def karafarinconvert():
    an = request.form['accountnumber']
    # Bank identify number for karafarin
    bi = "053"
    # Iran code
    cc = "IR"
    bban = bi + "000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/karafarin.html', iban=iban)


@app.route('/acnttoiban/kosar')
def kosar():
    return render_template('/acnttoiban/kosar.html')


@app.route("/acnttoiban/kosar", methods=["POST"])
def kosarconvert():
    an = request.form['accountnumber']
    # Bank identify number for kosar
    bi = "073"
    # Iran code
    cc = "IR"
    bban = bi + "00000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/kosar.html', iban=iban)


@app.route('/acnttoiban/khavarmiane')
def khavarmiane():
    return render_template('/acnttoiban/khavarmiane.html')


@app.route("/acnttoiban/khavarmiane", methods=["POST"])
def khavarmianeconvert():
    an = request.form['accountnumber']
    # Bank identify number for khavarmiane
    bi = "078"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/khavarmiane.html', iban=iban)


@app.route('/acnttoiban/eghnovin')
def eghnovin():
    return render_template('/acnttoiban/eghnovin.html')


@app.route("/acnttoiban/eghnovin", methods=["POST"])
def eghnovinconvert():
    an = request.form['accountnumber']
    # Bank identify number for eghnovin
    bi = "055"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)[:5] + "0" + str(an)[5:8] + \
        "0" + str(an)[8:-1] + "0" + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/eghnovin.html', iban=iban)


@app.route('/acnttoiban/ansar')
def ansar():
    return render_template('/acnttoiban/ansar.html')


@app.route("/acnttoiban/ansar", methods=["POST"])
def ansarconvert():
    an = request.form['accountnumber']
    # Bank identify number for ansar
    bi = "063"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)[0:-1] + "00" + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/ansar.html', iban=iban)


@app.route('/acnttoiban/iranzamin')
def iranzamin():
    return render_template('/acnttoiban/iranzamin.html')


@app.route("/acnttoiban/iranzamin", methods=["POST"])
def iranzaminconvert():
    an = request.form['accountnumber']
    # Bank identify number for iranzamin
    bi = "069"
    # Iran code
    cc = "IR"
    bban = bi + "00" + str(an)[0:4] + "0" + str(an)[4:-1] + "0" + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/iranzamin.html', iban=iban)


@app.route('/acnttoiban/pasargad')
def pasargad():
    return render_template('/acnttoiban/pasargad.html')


@app.route("/acnttoiban/pasargad", methods=["POST"])
def pasargadconvert():
    an = request.form['accountnumber']
    # Bank identify number for pasargad
    an = an.split('-')
    anfull = "".join(an)

    bi = "057"
    # Iran code
    cc = "IR"
    if len(anfull) == 12:
        bban = bi + "00" + str(an[0]) + "0" + str(an[1]) + \
            "00" + str(an[2]) + "00" + str(an[-1])
    else:
        bban = bi + "00" + str(an[0]) + str(an[1]) + \
            str(an[2]) + "00" + str(an[-1])
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/pasargad.html', iban=iban)


@app.route('/acnttoiban/tosetavon')
def tosetavon():
    return render_template('/acnttoiban/tosetavon.html')


@app.route("/acnttoiban/tosetavon", methods=["POST"])
def tosetavonconvert():
    an = request.form['accountnumber']
    # Bank identify number for tosetavon
    bi = "022"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)[0:5] + "0" + str(an)[5:-1] + "00" + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/tosetavon.html', iban=iban)


@app.route('/acnttoiban/tosesaderat')
def tosesaderat():
    return render_template('/acnttoiban/tosesaderat.html')


@app.route("/acnttoiban/tosesaderat", methods=["POST"])
def tosesaderatconvert():
    an = request.form['accountnumber']
    # Bank identify number for tosesaderat
    bi = "020"
    # Iran code
    cc = "IR"
    bban = bi + "000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/tosesaderat.html', iban=iban)


@app.route('/acnttoiban/sarmayeh')
def sarmayeh():
    return render_template('/acnttoiban/sarmayeh.html')


@app.route("/acnttoiban/sarmayeh", methods=["POST"])
def sarmayehconvert():
    an = request.form['accountnumber']
    # Bank identify number for sarmayeh
    bi = "058"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)[0:8] + "00" + str(an)[8:-1] + "00" + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/sarmayeh.html', iban=iban)


@app.route('/acnttoiban/sanatmadan')
def sanatmadan():
    return render_template('/acnttoiban/sanatmadan.html')


@app.route("/acnttoiban/sanatmadan", methods=["POST"])
def sanatmadanconvert():
    an = request.form['accountnumber']
    # Bank identify number for sanatmadan
    bi = "011"
    # Iran code
    cc = "IR"
    bban = bi + "000000" + str(an)
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/sanatmadan.html', iban=iban)


@app.route('/acnttoiban/gardeshgari')
def gardeshgari():
    return render_template('/acnttoiban/gardeshgari.html')


@app.route("/acnttoiban/gardeshgari", methods=["POST"])
def gardeshgariconvert():
    an = request.form['accountnumber']
    # Bank identify number for gardeshgari
    bi = "064"
    # Iran code
    cc = "IR"
    bban = bi + "00" + str(an)[0:3] + "00" + str(an)[3:5] + \
        "0" + str(an)[5:-1] + '00' + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/gardeshgari.html', iban=iban)


@app.route('/acnttoiban/resalat')
def resalat():
    return render_template('/acnttoiban/resalat.html')


@app.route("/acnttoiban/resalat", methods=["POST"])
def resalatconvert():
    an = request.form['accountnumber']
    # Bank identify number for resalat
    bi = "070"
    # Iran code
    cc = "IR"
    bban = bi + "000" + str(an)[0:2] + "0022" + \
        str(an)[2:-1] + '00' + str(an)[-1]
    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/resalat.html', iban=iban)


@app.route('/acnttoiban/sina')
def sina():
    return render_template('/acnttoiban/sina.html')


@app.route("/acnttoiban/sina", methods=["POST"])
def sinaconvert():
    an = request.form['accountnumber']
    # Bank identify number for sina
    bi = "059"
    # Iran code
    cc = "IR"
    bban = bi + "00" + str(an)[:3] + \
        '00' + str(an)[3:-1] + '00' + str(an)[-1]

    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/sina.html', iban=iban)


@app.route('/acnttoiban/markazi')
def markazi():
    return render_template('/acnttoiban/markazi.html')


@app.route("/acnttoiban/markazi", methods=["POST"])
def markaziconvert():
    an = request.form['accountnumber']
    # Bank identify number for markazi
    bi = "010"
    # Iran code
    cc = "IR"
    bban = bi + "000" + str(an)

    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/markazi.html', iban=iban)


@app.route('/acnttoiban/ghavamin')
def ghavamin():
    return render_template('/acnttoiban/ghavamin.html')


@app.route("/acnttoiban/ghavamin", methods=["POST"])
def ghavaminconvert():
    an = request.form['accountnumber']
    # Bank identify number for ghavamin
    bi = "052"
    # Iran code
    cc = "IR"
    bban = bi + "0000" + str(an)

    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/ghavamin.html', iban=iban)


@app.route('/acnttoiban/mehreqtesad')
def mehreqtesad():
    return render_template('/acnttoiban/mehreeghtesad.html')


@app.route("/acnttoiban/mehreqtesad", methods=["POST"])
def mehreqtesadconvert():
    an = request.form['accountnumber']
    # Bank identify number for mehreqtesad
    bi = "079"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)[:-1] + "00" + str(an)[-1]

    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/mehreqtesad.html', iban=iban)


@app.route('/acnttoiban/mehriran')
def mehriran():
    return render_template('/acnttoiban/mehriran.html')


@app.route("/acnttoiban/mehriran", methods=["POST"])
def mehriranconvert():
    an = request.form['accountnumber']
    # Bank identify number for mehriran
    bi = "060"
    # Iran code
    cc = "IR"
    bban = bi + "0" + str(an)[:-1] + "00" + str(an)[-1]

    # check digits
    cd = str(98 - int(bban + "182700") % 97)
    if len(cd) < 2:
        cd = "0" + str(cd)
    iban = cc + cd + bban
    return render_template('/acnttoiban/mehriran.html', iban=iban)
