from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FIO = db.Column(db.String(100))
    YON = db.Column(db.Integer)
    dateofa = db.Column(db.Integer)
    dateofd = db.Column(db.Integer)
    wtkk = db.Column(db.String(100))
    kol = db.Column(db.Integer)
    transport = db.Column(db.Text)

    def __repr__(self):
        return '<Article %r>' % self.id

class hardcore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.Text)
    psw = db.Column(db.Text)

    def __repr__(self):
        return '<hardcore %r>' % self.id


@app.route('/g')
def index():
    return render_template("index.html")

@app.route('/l')
def l():
    return render_template("tp.html")


@app.route('/post')
def post():
    articles = Article.query.order_by(Article.id).all()
    return render_template("post.html", articles=articles)


@app.route('/', methods=['POST', 'GET'])
def j():
    if request.method == "POST":
        uname = request.form['uname']
        psw = request.form['psw']

        ewen = hardcore(uname=uname, psw=psw)
        try:
            db.session.add(ewen)
            db.session.commit()
            return redirect('/g')
        except:
            return "ЛОХ"
    return render_template("j.html")

@app.route('/j')
def g():
    if request.method == "POST":
        return redirect('/g')

    return render_template("g.html")

@app.route('/gtt', methods=['POST', 'GET'])
def gtt():
    if request.method == "POST":
        FIO = request.form['FIO']
        YON = request.form['YON']
        dateofa = request.form['dateofa']
        dateofd = request.form['dateofd']
        wtkk = request.form['wtkk']
        kol = request.form['kol']
        transport = request.form['transport']

        newe = Article(FIO=FIO, YON=YON, dateofa=dateofa, dateofd=dateofd, wtkk=wtkk, kol=kol, transport=transport)

        try:
            db.session.add(newe)
            db.session.commit()
            return redirect('/g')
        except:
            return redirect('/')
    else:
        return render_template("gtt.html")

@app.route('/gft')
def gft():
    return render_template("gft.html")

if __name__ == "__main__":
    app.run(debug=True)