from flask import Flask, render_template


app = Flask(__name__)  
app.secret_key = '^$hgj%^#^4#5&%34$#&%$w2H*5n3'


@app.route('/')
def main():
    return render_template('home.html')








if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')