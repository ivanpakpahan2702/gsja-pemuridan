from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from flask_paginate import Pagination
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os
from connection_db.class_connection import db_connection
import math
from __main__ import *
from rank_bm25 import BM25Okapi
from backend.all_functions import *
blog_cari_blueprint = Blueprint('blog_cari', __name__)


# Blog Filter
@blog_cari_blueprint.route('/blog/cari', defaults={'slug': '','bagian': '' })
@blog_cari_blueprint.route('/blog/cari/<slug>', defaults={'bagian': 1 })
@blog_cari_blueprint.route("/blog/cari/<slug>/<int:bagian>")
def blog_cari(slug,bagian):

    result   = db_connection()
    category = result.show_category(coloumn_names=['*'], table_name='tabel_kategori')

    # BM25 Rank 
    result = db_connection()
    data_corpus = result.show_post(coloumn_names=['*'], table_name='tabel_postingan')
    id  = []
    corpus=[]
    for i in data_corpus:
        corpus.append(i[3])
        id.append(i[0])

    tokenized_corpus = [doc.split(" ") for doc in corpus]

    bm25 = BM25Okapi(tokenized_corpus)
    query = str(slug)
    print("=================================================")
    print(query)
    tokenized_query = query.split(" ")
    #doc_scores = bm25.get_scores(tokenized_query)
    new_list = bm25.get_top_n(tokenized_query, corpus, n=10)
    list_index = []
    tuple_index = ()
    for i in new_list:
        _index = int(corpus.index(i))
        list_index.append(_index)
    # Get Id
    real_id = []
    for i in list_index:
        real_id.append(id[i])
    print('Real Id',real_id)
    
    for j in real_id:
        tuple_index = tuple_index+(j,)
    # BM25 Rank

    result = db_connection()
    result = result.search_post(coloumn_names=['*'], table_name='tabel_postingan',statement={"id_postingan":tuple_index})

    total = len(list_index)

    # Parameter Page Using Default Params
    page_ = bagian
    per_page_ = 9
    offset_ = (page_ - 1) * per_page_
    total_page_ = (math.ceil(float(total)/per_page_))

    pagination_blog = get_post(result, offset=offset_, per_page=per_page_)
    return render_template('blog_cari.html', title='blog', result = pagination_blog, page=page_,
                           per_page=per_page_,
                           category=category,
                           offset=offset_,
                           total_page = total_page_,
                           part = bagian,
                           total_records = total,
                           slug=slug)