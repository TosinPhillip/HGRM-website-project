from flask import Flask, render_template, jsonify
from database import load_articles_from_airtable, load_article_from_airtable

app = Flask(__name__)




@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/articles')
def article_list_page():
    return render_template('article_list.html')


@app.route('/api/articles')
def article_api_page():
    blogs = load_articles_from_airtable()
    return jsonify(blogs)

@app.route('/articles/<id>')
def each_article_page(id):
    """Takes in the record ID and loads the dictionary as blog"""
    blog = load_article_from_airtable(id)
    return render_template('article_page.html', blog=blog)


if __name__ == '__main__':
    app.run(debug=True)