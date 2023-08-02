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
download_blueprint = Blueprint('download', __name__)


# Download
@download_blueprint.route('/download', defaults={ 'bagian': 1 }, methods=['GET', 'POST'])
@download_blueprint.route("/download/<int:bagian>")
def download(bagian):
    list_file_size = []
    result = db_connection()
    result = result.show_download(coloumn_names=['*'], table_name='tabel_download')
    # get file size in python
    directory_file_name = "static/downloads/"
    for i in result:
        filename   = directory_file_name + i[2]
        file_stats = os.stat(filename)
        filesize   = file_stats.st_size / 1024
        filesize   = float("{:.2f}".format(filesize))
        list_file_size.append(filesize)
    
    total = len(result)

    # Parameter Page Using Default Params
    page_ = bagian
    per_page_ = 9
    offset_ = (page_ - 1) * per_page_
    total_page_ = (math.ceil(float(total)/per_page_))

    pagination_download = get_download(result, offset=offset_, per_page=per_page_)
    
    return render_template('download.html', 
                           title='download',
                           list_file_size = list_file_size,
                           result = pagination_download,
                           page=page_,
                           per_page=per_page_,
                           offset=offset_,
                           total_page = total_page_,
                           part = bagian,
                           total_records = total)