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
kegiatan_blueprint = Blueprint('kegiatan', __name__)


# Kegiatan
@kegiatan_blueprint.route('/kegiatan', methods=['GET', 'POST'])
def kegiatan():
    # Database Gambar
    file_carousel = []
    file_image3 = ['jpg', 'png', 'bmp', 'gif', 'ico']
    file_image4 = ['jpeg', 'webp']

    result = db_connection()
    result = result.show_activity_carousel(coloumn_names=['*'], table_name='tabel_galeri_kegiatan')
    
    db_path = []
    for i in range(len(result)):
        db_path.append(result[i][1])

    for f in db_path:
        if (f[-3:] in file_image3) or (f[-4:] in file_image4):
            file_carousel.append(f)
        else:
            print('not found')

    # Database Jadwal
    result = db_connection()
    result = result.show_activity_schedule(coloumn_names=['*'],table_name='tabel_jadwal_kegiatan')

    return render_template('kegiatan.html', carousel=file_carousel, jadwal=result, title='kegiatan')