from flask import Flask ,render_template ,session ,redirect ,request
app=Flask(__name__)
app.secret_key=('scret')
@app.route('/show')
def fun1():
    if 'count' not in session :
        session['count']=1
    else:
        session['count']+=1
    return render_template('count.html')
@app.route('/destroy_session',methods=['POST'])
def fun2():
    session.clear()
    return redirect('/show')

if __name__=='__main__':
    app.run(debug=True)
