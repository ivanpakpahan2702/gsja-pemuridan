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
blog_detail_blueprint = Blueprint('blog_detail', __name__)


# Blog
@blog_detail_blueprint.route('/blog/detail', defaults={ 'slug': '' }, methods=['GET', 'POST'])
@blog_detail_blueprint.route("/blog/detail/<slug>")
def blog_detail(slug):
    result = db_connection()
    blog   = result.show_post(coloumn_names=['*'], table_name='tabel_postingan', statement={'slug': str(slug)})
    blog_  = []
    b = ()
    for i in blog:
        need_encoded_id = i[0]
        encoded_id      = Id_Encoder(25,25,need_encoded_id)
        for j in range(len(i)):
            if (j==0):
                b = b + (encoded_id,) 
            else:
                b = b + (i[j],)
        blog_.append(b)
        b = ()
    
    id_category = blog[0][7]
    result   = db_connection()
    category = result.show_category(coloumn_names=['*'], table_name='tabel_kategori', statement={'id_kategori':id_category})

    id_postingan = blog[0][0]
    result   = db_connection()
    comments = result.show_comment(coloumn_names=['*'], table_name='tabel_komentar', statement={'postingan':id_postingan,'status_komentar':'Show'})
    count_comment = len(comments)
    
    return render_template('blog_detail.html', title='blog', category=category, result = blog_, comments=comments, count_comment = count_comment)