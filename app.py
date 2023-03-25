from flask import Flask

from operations.view import operations_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(operations_blueprint)


@app.errorhandler(404)
def page_404(error):
    return "404 NOT FOUND"


@app.errorhandler(500)
def page_500(error):
    return "500 Internal Server Error"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)