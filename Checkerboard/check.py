from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/')
def fun1 ():
    return render_template("check.html")
@app.route('/<num>')
def fun2 (num):
    num=num
    return render_template("check4.html",n=int(num))
@app.route('/<col>/<row>')
def fun3 (col,row):
    return render_template("checknum.html",c=int(col),r=int(row))
@app.route('/<col>/<row>/<color1>/<color2>')
def fun4 (col,row ,color1 ,color2):
    return render_template("checkcol.html",c=int(col),r=int(row),cl1=color1,cl2=color2)
if __name__=="__main__":
    app.run(debug=True)
