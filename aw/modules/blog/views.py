import json
from os.path import join as join_path

from flask import abort, render_template

from aw.lib import parse_date_string
from aw.modules.blog import blog


def handle_post_date(post):
    post['date'] = parse_date_string(post['date'])
    return post

posts = json.load(open(join_path(blog.root_path, 'posts.json'), 'r'))
posts = map(handle_post_date, posts)


@blog.route('/')
def index():
    newest_posts = posts[:5]
    return render_template('blog/index.html', posts=newest_posts)
