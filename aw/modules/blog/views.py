import json
from os.path import join as join_path

from flask import abort, render_template, request

from aw.config import BLOG_PAGE_SIZE
from aw.lib import parse_date_string, Pagination
from aw.modules.blog import blog


def handle_post_date(post):
    post['date'] = parse_date_string(post['date'])
    return post

def get_posts_to_show():
    if 'show_all' in request.args:
        return all_posts
    else:
        return [p for p in all_posts if p['status'] == 'published']

all_posts = json.load(open(join_path(blog.root_path, 'posts.json'), 'r'))
all_posts = map(handle_post_date, all_posts)


@blog.route('/')
@blog.route('/page/<int:page_num>')
def index(page_num=1):
    posts = get_posts_to_show()
    return show_paginated_posts(posts, page_num)

@blog.route('/tags/<tag_name>')
@blog.route('/tags/<tag_name>/page/<int:page_num>')
def tag_index(tag_name, page_num=1):
    posts = [p for p in get_posts_to_show() if tag_name in p["tags"]]
    return show_paginated_posts(posts, page_num)


def show_paginated_posts(posts, page_num):
    pagination = Pagination(posts, page_num, BLOG_PAGE_SIZE)
    if not pagination.current_page_exists:
        abort(404)
    return render_template('blog/index.html', posts=pagination.page_objects,
            pagination=pagination)
