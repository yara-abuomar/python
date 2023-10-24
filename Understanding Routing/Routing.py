from flask import Flask
app= Flask(__name__)
@app.route('/')
def hello():
    return "hello world!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/<name>')
def user(name):
    return "Hi "+name
@app.route('/<name>/<time>')
def repeat(name,time):
    return name *int(time)

if __name__=="__main__":
    app.run(debug=True)

