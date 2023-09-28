from flask import Flask, render_template, jsonify
from database import load_articles_from_airtable, load_article_from_airtable

app = Flask(__name__)




@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/admin')
def admin_page():
    return render_template('admin_profile.html')


@app.route('/articles/<int:page>')
def article_list_page(page):
    blogs = load_articles_from_airtable(page)
    return render_template('article_list.html', blogs=blogs)


@app.route('/api/article/<id>')
def article_api_page(id):
    blogs = load_article_from_airtable(id)
    return jsonify(blogs)

@app.route('/article/<id>')
def each_article_page(id):
    """Takes in the record ID and loads the dictionary as blog"""
    blog = load_article_from_airtable(id)
    return render_template('article_page.html', blog=blog)

# @app.route('/about')
# def about_us:
#     return render_template('about_us.html')





if __name__ == '__main__':
    app.run(debug=True)