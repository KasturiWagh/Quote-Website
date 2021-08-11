from flask import Flask,render_template , redirect, url_for, request,make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')          
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///quote.db"   #database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Quote(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Qquote = db.Column(db.String(900), nullable=False)
    Aauther = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Aauther}"

@app.route('/del')
def dele():

    allquote = Quote.query.all()
    print(allquote)
    return render_template('del.html', allquote=allquote)


@app.route('/delete/<int:sno>')
def delete(sno):
    quote = Quote.query.filter_by(sno=sno).first()
    db.session.delete(quote)
    db.session.commit()
    return redirect('/')

@app.route('/main')
def main():
    allquote = Quote.query.all()
    print(allquote)
    return render_template('main.html', allquote=allquote)

@app.route('/', methods=['POST' , 'GET'])
def PUTQuotes():
    if request.method == 'POST':
        user = request.form['Quotee']
        user2 = request.form['Authorr']
        quote = Quote( Qquote = user, Aauther = user2)
        db.session.add(quote)
        db.session.commit()
    allquote = Quote.query.all() 
    return render_template('firstPage.html', allquote=allquote)


@app.route('/show')
def show():
    allquote = Quote.query.all()
    print(allquote)
    return render_template('firstPage.html')


if __name__ == '__main__':
   app.run(debug = True, port = 8000)