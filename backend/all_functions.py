from re import template
from flask import Flask, url_for, render_template, jsonify, request, Blueprint, redirect
from flask_paginate import Pagination
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
import os
from connection_db.class_connection import db_connection
import math
from random import randint

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