import flask

app = flask.Flask(__name__)
@app.route('/')
def home():
    return flask.render_template('Главная страница.html')

if __name__=='__main__':
    app.run()