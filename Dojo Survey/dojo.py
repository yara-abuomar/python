from flask import Flask ,render_template, request, redirect
app=Flask(__name__)
@app.route('/')
def fun1 ():
    return render_template('index.html')
@app.route('/result',methods=['POST'])
def fun2():
    return render_template('result.html',Name=request.form['name'],loc=request.form['location'],lan=request.form['languge'],comm=request.form['Comment'])
if __name__=="__main__":
    app.run(debug=True)
