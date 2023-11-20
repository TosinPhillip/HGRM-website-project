from flask import Flask, render_template, jsonify
from database import load_articles_from_airtable, load_article_from_airtable, load_media

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

@app.route('/doctrine')
def doctrine():
    return render_template('doctrine.html')

@app.route('/photos')
def photos():
    medias = load_media()
    return render_template('photos.html', medias=medias)

@app.route('/audios')
def audios():
    medias = load_media()
    return render_template('audios.html', medias=medias)

@app.route('/videos')
def videos():
    medias = load_media()   
    return render_template('videos.html', medias=medias)


@app.route('/staff_advisers')
def staff_adviser():
    return render_template('staff_advisers.html')

@app.route('/executives')
def executivess():
    return render_template('execs.html')




if __name__ == '__main__':
    app.run(debug=True)