from flask import Flask , render_template
app=Flask(__name__)
@app.route("/play")
def playfun():
    return render_template("index.html",)
@app.route("/play/<time>")
def playfun2(time):
    return render_template("index2.html",time=int(time))
@app.route("/play/<time>/<colo>")
def playfun3(time,colo):
    return render_template("index3.html",time=int(time),colo=colo)
if __name__=="__main__":
    app.run(debug=True)
