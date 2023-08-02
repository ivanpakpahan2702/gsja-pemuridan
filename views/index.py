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
index_blueprint = Blueprint('index', __name__)

# Beranda
@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    file_carousel = []
    directory = 'static/images/carousel/'

    file_image3 = ['jpg', 'png', 'bmp', 'gif', 'ico']
    file_image4 = ['jpeg', 'webp']

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            if (f[-3:] in file_image3) or (f[-4:] in file_image4):
                file_carousel.append(f)
            else:
                print('not found')
    
    # for i in range(int(len(file_carousel))):
    #     file_carousel[i] = file_carousel[i][15:]

    return render_template('beranda.html', carousel=file_carousel, title='beranda')