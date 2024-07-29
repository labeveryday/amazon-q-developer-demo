from flask import Flask, request, redirect


app = Flask(__name__)

@app.route('/redirect')
def redirect_url_noncompliant():
    endpoint = request.args['url']
    return redirect(endpoint)


if __name__ == '__main__':
    app.run(debug=True)
