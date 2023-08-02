from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from flask_paginate import Pagination
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os
from connection_db.class_connection import db_connection
import math
from rank_bm25 import BM25Okapi
from datetime import datetime
from random import randint


app = Flask(__name__)
########################################################################################
# Functions
def get_gallery(gallery, offset=0, per_page=9):
    return gallery[offset: offset + per_page]

def get_download(download, offset=0, per_page=9):
    return download[offset: offset + per_page]

def get_post(post, offset=0, per_page=9):
    return post[offset: offset + per_page]

def Id_Encoder(First_Digits,Second_Digits,Key):
    First_range_start = 10**(First_Digits-1)
    First_range_end   = (10**First_Digits)-1
    First_key         = randint(First_range_start, First_range_end)
    
    Second_range_start = 10**(Second_Digits-1)
    Second_range_end   = (10**Second_Digits)-1
    Second_key         = randint(Second_range_start, Second_range_end)
    
    code_              = str(First_key) + str(Key) + str(Second_key)
    return(code_)

def Id_Decoder(First_Digits,_code):
    real_id            = _code[(First_Digits)]
    return int(real_id)
########################################################################################
# Beranda
from views.index import index_blueprint
app.register_blueprint(index_blueprint)
########################################################################################
# Pengakuan Iman Rasuli
from views.pengakuan_iman_rasuli import pengakuan_iman_rasuli_blueprint
app.register_blueprint(pengakuan_iman_rasuli_blueprint)
########################################################################################
# Pengakuan Iman
from views.pengakuan_iman import pengakuan_iman_blueprint
app.register_blueprint(pengakuan_iman_blueprint)
########################################################################################
# Struktur Organisasi
from views.struktur_organisasi import struktur_organisasi_blueprint
app.register_blueprint(struktur_organisasi_blueprint)
########################################################################################
# Sejarah Gereja
from views.sejarah_gereja import sejarah_gereja_blueprint
app.register_blueprint(sejarah_gereja_blueprint)
########################################################################################
# Blog
from views.blog import blog_blueprint
from views.blog_filter import blog_filter_blueprint
from views.blog_detail import blog_detail_blueprint
from views.blog_cari import blog_cari_blueprint
from views.komentar import kirim_komen_blueprint
app.register_blueprint(blog_blueprint)
app.register_blueprint(blog_filter_blueprint)
app.register_blueprint(blog_detail_blueprint)
app.register_blueprint(blog_cari_blueprint)
app.register_blueprint(kirim_komen_blueprint)
########################################################################################
# Kegiatan
from views.kegiatan import kegiatan_blueprint
app.register_blueprint(kegiatan_blueprint)
########################################################################################
# Galeri
from views.galeri import galeri_blueprint
app.register_blueprint(galeri_blueprint)
########################################################################################
# Download
from views.download import download_blueprint
app.register_blueprint(download_blueprint)
########################################################################################
# Alkitab
from views.alkitab import alkitab_blueprint
from views.alkitab_cari import alkitab_cari_blueprint
app.register_blueprint(alkitab_blueprint)
app.register_blueprint(alkitab_cari_blueprint)
########################################################################################
# Kontak
from views.kontak import kontak_blueprint
from views.kontak import kirim_email_blueprint
# Kontak
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.register_blueprint(kontak_blueprint)
app.register_blueprint(kirim_email_blueprint)
########################################################################################
# 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

########################################################################################
########################################################################################
########################################################################################
if __name__ == '__main__':
    app.run(debug=True)
