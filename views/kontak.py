from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from flask_paginate import Pagination
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os
from connection_db.class_connection import db_connection
import math
from __main__ import *
from flask_mail import Mail, Message
from backend.all_functions import *
kontak_blueprint = Blueprint('kontak', __name__)
kirim_email_blueprint = Blueprint('kirim_email', __name__)


@kontak_blueprint.route('/kontak', methods=['GET', 'POST'])
def kontak():
    return render_template('kontak.html', title='kontak')

@kirim_email_blueprint.route('/kontak/kirim')
def kirim_email():
    gmail_username = 'tester.gsja.pemuridan@gmail.com'
    gmail_password = 'ufwsuxroeqsrpaec'
    to = 'gsja.pemuridan.bengkulu.utara@gmail.com'
    nama_lengkap = request.args.get('nama')
    email = request.args.get('email')
    message = request.args.get('message')
    subject = 'Kontak Web GSJA Pemuridan'
    
    message = 'Nama : '+str(nama_lengkap)+'\n'+'Email : '+str(email)+'\n\n'+ message


    app.config['MAIL_USERNAME'] = gmail_username
    app.config['MAIL_PASSWORD'] = gmail_password
    
    msg = Message(subject, 
        sender=gmail_username, recipients=[to])
    msg.body = message
    
    try:
        mail = Mail(app)
        mail.connect()
        mail.send(msg)
        result = ['Pengiriman Sukses', 'Pesan yang anda kirim telah masuk kedalam inbox email kami. Kami akan segera merespon pesan anda ke email yang telah anda masukkan']
        return jsonify(result)
    except:
        result = ['Pengiriman Gagal', 'Pesan tidak terkirim, pastikan koneksi internet lancar']
        return jsonify(result)
    
    result = 'Kirim Gagal'
    return jsonify(result)
