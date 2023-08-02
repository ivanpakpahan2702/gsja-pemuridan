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
pengakuan_iman_rasuli_blueprint = Blueprint('pengakuan_iman_rasuli', __name__)


# Pengakuan Iman Rasuli
@pengakuan_iman_rasuli_blueprint.route('/pengakuan_iman_rasuli', methods=['GET', 'POST'])
def pengakuan_iman_rasuli():
    return render_template('pengakuan_iman_rasuli.html', title='pengakuan_iman_rasuli')