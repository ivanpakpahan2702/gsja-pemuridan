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
sejarah_gereja_blueprint = Blueprint('sejarah_gereja', __name__)


# Sejarah Gereja
@sejarah_gereja_blueprint.route('/sejarah_gereja', methods=['GET', 'POST'])
def sejarah_gereja():
    return render_template('sejarah_gereja.html', title='sejarah_gereja')