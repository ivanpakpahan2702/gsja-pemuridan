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
galeri_blueprint = Blueprint('galeri', __name__)


# Galeri
@galeri_blueprint.route('/galeri', defaults={ 'bagian': 1 }, methods=['GET', 'POST'])
@galeri_blueprint.route("/galeri/<int:bagian>")
def galeri(bagian):

    result = db_connection()
    result = result.show_gallery(coloumn_names=['*'], table_name='tabel_galeri')
    
    total = len(result)

    # Parameter Page Using Default Params
    page_ = bagian
    per_page_ = 9
    offset_ = (page_ - 1) * per_page_
    total_page_ = (math.ceil(float(total)/per_page_))

    pagination_gallery = get_gallery(result, offset=offset_, per_page=per_page_)
    
    return render_template('galeri.html', title='galeri', result = pagination_gallery, page=page_,
                           per_page=per_page_,
                           offset=offset_,
                           total_page = total_page_,
                           part = bagian,
                           total_records = total,
                           )