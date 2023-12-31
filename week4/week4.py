import flask

app = flask.Flask( __name__)
app.secret_key = "4169256be8d33cc483c43dca55b3d8079383b0023e284694241cb8004dee05fd"
users = { "hank@pig.com": { "password" : "123"}}

@app.route("/")
def index():
    return flask.render_template( "home.html")

@app.route("/signin", methods=["GET","POST"])
def login():
    flask.session["SIGNED-IN"] = False
    email = flask.request.form["email"]
    password = flask.request.form["password"]
    if email in users and password == users[email]["password"]:
        flask.session["username"] = email
        flask.session["SIGNED-IN"] = True
        return flask.redirect( flask.url_for("member"))
    if email == "" or password == "":
        return flask.redirect( flask.url_for("errorMessage", message = "empty"))
    return flask.redirect( flask.url_for("errorMessage", message = "invalid"))

@app.route("/member")
def member():
    if flask.session["SIGNED-IN"] == False:
        return flask.redirect("/")
    return flask.render_template( "message.html", page="member")

@app.route("/signout", methods=["GET"])
def signout():
    flask.session["SIGNED-IN"] = False
    return flask.redirect( flask.url_for("index"))

@app.route("/error", methods=["GET"])
def errorMessage():    
    message=flask.request.args.get("message")
    return flask.render_template("message.html", page=error,message=message)

@app.route("/square/<number>")
def squareNum(number):
    answer=int(number)*int(number)
    return flask.render_template("message.html", page="square", answer=answer)

if __name__ == "__main__":
    # app.debug=True
    app.run(port=3000)
