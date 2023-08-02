from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from flask_paginate import Pagination
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os
from connection_db.class_connection import db_connection
import math
from __main__ import *
from datetime import datetime
from backend.all_functions import *
kirim_komen_blueprint = Blueprint('kirim_komen', __name__)


@kirim_komen_blueprint.route('/komen/kirim', methods=['POST', 'GET'])
def kirim_komen():
    comment_author = request.args.get('comment-author')
    comment_status = 'Hide'
    comment_date   = datetime.now()
    comment_editor = request.args.get('comment-editor')
    comment_post   = request.args.get('posting-id')
    print(comment_author)
    print(comment_status)
    print(comment_date)
    print(comment_editor)
    print(comment_post)        
    comment_date = comment_date.strftime("%Y-%m-%d %H:%M:%S")
    try:
        result = db_connection()
        result = result.send_comment(table_name='tabel_komentar',data=('',comment_author,comment_status,comment_date,comment_editor,Id_Decoder(25,comment_post)))
        msg    = ['Menunggu Peninjauan','Komentar anda telah masuk kedalam database. Komentar akan ditampilkan setelah ditinjau oleh Administrator']
        return jsonify(msg)
    except:
        msg    = ['Gagal','Komentar tidak terkirim. Silahkan coba lagi']
        return jsonify(msg)