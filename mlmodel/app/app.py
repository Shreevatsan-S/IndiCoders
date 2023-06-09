from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
         return render_template('intro.html')

@app.route('/login')
def login():
         return render_template('login.html')


@app.route('/signup')
def signup():
         return render_template('signup.html')

@app.route('/input.html',methods=['POST','GET'])
def input():
        if request.method=='POST':
                a=float(request.form['a'])
                b=float(request.form['b'])
                c=float(request.form['c'])
                d=float(request.form['d'])
                e=float(request.form['e'])
                f=float(request.form['f'])
                g=float(request.form['g'])
                h=float(request.form['h'])
                i=float(request.form['i'])
                j=float(request.form['j'])
        return render_template('input.html')
        

if __name__ == "__main__":
    app.run(debug=True)

