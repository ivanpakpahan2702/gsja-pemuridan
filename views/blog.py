from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from flask_paginate import Pagination
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os
from connection_db.class_connection import db_connection
import math
from __main__ import *
from backend.all_functions import *
blog_blueprint = Blueprint('blog', __name__)


# Blog
@blog_blueprint.route('/blog', defaults={ 'bagian': 1 }, methods=['GET', 'POST'])
@blog_blueprint.route("/blog/<int:bagian>")
def blog(bagian):
    result   = db_connection()
    category = result.show_category(coloumn_names=['*'], table_name='tabel_kategori')
    result = db_connection()
    result = result.show_post(coloumn_names=['*'], table_name='tabel_postingan')
    
    total = len(result)

    # Parameter Page Using Default Params
    page_ = bagian
    per_page_ = 9
    offset_ = (page_ - 1) * per_page_
    total_page_ = (math.ceil(float(total)/per_page_))

    pagination_blog = get_post(result, offset=offset_, per_page=per_page_)
    return render_template('blog.html', title='blog', category=category, result = pagination_blog, page=page_,
                           per_page=per_page_,
                           offset=offset_,
                           total_page = total_page_,
                           part = bagian,
                           total_records = total)