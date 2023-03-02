from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/717da56649b7e14ef21b"
response = requests.get(blog_url)
posts = response.json()

all_posts = []
for post in posts:
    new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(new_post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def post(id):
    for post in all_posts:
        if post.id == id:
            blog_post = post

    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
