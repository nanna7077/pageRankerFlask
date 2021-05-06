from flask import Flask, render_template, request
from os import urandom, getenv
import validators
import pageranker

app=Flask(__name__)
app.secret_key=urandom(12)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="GET":
        return render_template('home.html', error=None)
    vaild=validators.url(request.form["userUrl"])
    if not vaild:
        return render_template('home.html', error="Invalid Address. Check the address and try again!")
    pagerankerObject=pageranker.SimplePageRank(request.form['userUrl'])
    pagerankerObject.startPageRank()
    result=pagerankerObject.getPageRankInfo()
    return render_template("result.html", result=result, url=request.form["userUrl"])

if __name__=="__main__":
    app.run(threaded=True, host='0.0.0.0', port=getenv("PORT"))
    #app.run(threaded=True, host='0.0.0.0')
