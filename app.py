from flask import Flask, render_template, request, redirect
import search
import json

search_attraction = search.Search()

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET']) # 1번째 페이지
def home():
    return render_template('index.html')

@app.route('/main', methods=['POST', 'GET']) # 2번째 페이지
def main():
    return render_template('search.html')


@app.route('/map', methods=['POST', 'GET']) # 3번째 페이지
def map():
    if request.method == 'POST':
        res = request.get_json()
        return render_template('map.html', data = res)
    elif request.method == 'GET':

        return render_template('map.html')

@app.route('/api/search', methods=['POST'])
def post():
    keyword = request.form['searchKeyword']
    suggestions = search_attraction.suggest(keyword)
    return suggestions

@app.route('/result', methods=['POST', 'GET']) # 4번째 페이지
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
