from flask import Flask , render_template, redirect,url_for,request, make_response,session

from.session_interface import MySessionInterface,SessionInterface
# flask import edildi. Ardından da HTMLiçin render_template import edildi.
# redirect admin isim kontrolü için import edildi.

app=Flask(__name__)             # burada flask adımız verildi.
app.secret_key =b"?039eruif3__"
app.session_interface= MySessionInterface()

@app.route("/")                 # bu anasayfamız için yapıldı.

def Definition ():

    if "name" in session:
        print( "name",session["name"])
    session["name"]="Ahmet"
    session["lastname"]="Ahmetoğlu"
    session["username"]="ahmet123"
    return (" <html><body><h1> İLK FLASK DENEMESİ</h1></body></html>")

@app.route("/index",methods=["GET","POST"])

def Index ():
    isim="Dilara Çelik"
    sayı=5
    liste=[ "ankara","adana", "istanbul","izmir","bursa"]

    if request.method=="POST":
        iller = ["ankara", "adana", "istanbul", "izmir", "bursa"]
        kelime=request.form.get("arama")
        if kelime in iller:
            mesaj=" aranan il iller listesinin içinde bulunmaktadır."
            return render_template("index.html", isim=isim, sayı=sayı, liste=liste,mesaj=mesaj )

        else:
            mesaj=" aranan il iller listesinde bulunmamaktadır."
            return render_template("index.html", isim=isim, sayı=sayı, liste=liste,mesaj=mesaj )

    return render_template("index.html", isim=isim, sayı=sayı, liste=liste, )


@app.route("/hello")
def Hello():
    return render_template("hello.html")

@app.route("/hello-admin")
def HelloAdmin():
    return render_template("hello-admin.html")

@app.route("/hello-user/<name>")
def HelloUser(name):
    if name.lower()== "admin":
        return redirect(url_for("HelloAdmin"))

    return render_template("hello-user.html", user_name=name)

@app.route("/add/<int:number1>/<int:number2>")

def Add(number1, number2):
    calculation_result=number1+number2
    return render_template("add.html",number1=number1, number2=number2, result=calculation_result)

@app.route("/login", methods=['POST' ,'GET' ])
def Login():
    if request.method=='POST':
        #if "username"in request.form
        username = request.form["username"]
        return redirect(url_for("HelloUser", name=username))

    else:
        return render_template("login.html")

@app.route("/student")
def Student():
    return render_template("student.html")

@app.route("/result", methods=["POST"])
def Result():
    name =request.form["name"]
    physics =request.form["physics"]
    matematics =request.form["matematics"]
    chemistry =request.form["chemistry"]
    return render_template("student_result.html",name=name,physics=physics,matematics=matematics,chemistry=chemistry)

#COOKIE TANIMLAMSI YAPILMIŞTI:
    #signer = Signer("secret key")
    #signer_name=request.cookies.get("key")
    #try:
    #    name=signer.unsign(signer_name).decode()
    #   print(name)
    #except BadSignature:
    #   print("badsignature")


    #signer_name=signer.sign("ahmet")
    #response=make_response(" <html><body><h1> İLK FLASK DENEMESİ</h1></body></html>")
    #response.set_cookie("key",signer_name)
    #return response     # her işlem yapıldıktan sonra CRTL+C ile kapatacağız.
                                                                         #FLASK_ENV=development ile sürekli açıp kapatma olayına çözüm bulmuş olacağız.
                                                                            # html kodu ile de yazım yapabiliriz.






