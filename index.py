import flask
web=flask.Flask('my page')

@web.route('/')
def homepage():
    resp = flask.Response()
    resp.headers['refresh'] = '1; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    resp.data=flask.render_template("Google.html")
    return resp

web.run(port=80)