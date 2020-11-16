from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/search')
def search_results():
    search = request.args.get('s')
    print(search)
    return render_template('search.htm', search=search)