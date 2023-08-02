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
struktur_organisasi_blueprint = Blueprint('struktur_organisasi', __name__)


# Struktur Organisasi
@struktur_organisasi_blueprint.route('/struktur_organisasi', methods=['GET', 'POST'])
def struktur_organisasi():
    return render_template('struktur_organisasi.html', title='struktur_organisasi')