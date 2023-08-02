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
pengakuan_iman_blueprint = Blueprint('pengakuan_iman', __name__)


# Pengakuan Iman
@pengakuan_iman_blueprint.route('/pengakuan_iman', methods=['GET', 'POST'])
def pengakuan_iman():
    return render_template('pengakuan_iman.html', title='pengakuan_iman')