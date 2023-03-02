from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/717da56649b7e14ef21b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<id>')
def post(id):
    blog_url = "https://api.npoint.io/717da56649b7e14ef21b"
    response = requests.get(blog_url)
    all_posts = response.json()
    for post in all_posts:
        if post["id"] == int(id):
            title = post["title"]
            subtitle = post["subtitle"]
            body = post["body"]
            break
    return render_template("post.html", post_title=title, post_subtitle=subtitle, post_body=body)


if __name__ == "__main__":
    app.run(debug=True)
