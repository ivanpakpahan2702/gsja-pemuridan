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
alkitab_blueprint = Blueprint('alkitab', __name__)


# Alkitab
@alkitab_blueprint.route('/alkitab', methods=['GET', 'POST'])
def alkitab():
    data_bible = [('Kejadian', 'Kejad'), ('Keluaran', 'Kelua'), ('Imamat', 'Imama'), ('Bilangan', 'Bilan'), ('Ulangan', 'Ulang'), 
              ('Yosua', 'Yosua'), ('Hakim-hakim', 'Hakim'), ('Rut', 'Rut'), ('1 Samuel', '1 Sam'), ('2 Samuel', '2 Sam'), 
              ('1 Raja-raja', '1 Raj'), ('2 Raja-raja', '2 Raj'), ('1 Tawarikh', '1 Taw'), ('2 Tawarikh', '2 Taw'), ('Ezra', 'Ezra'), 
              ('Nehemia', 'Nehem'), ('Ester', 'Ester'), ('Ayub', 'Ayub'), ('Mazmur', 'Mazmu'), ('Amsal', 'Amsal'), ('Pengkhotbah', 'Pengk'), 
              ('Kidung Agung', 'Kidun'), ('Yesaya', 'Yesay'), ('Yeremia', 'Yerem'), ('Ratapan', 'Ratap'), ('Yehezkiel', 'Yehez'), 
              ('Daniel', 'Danie'), ('Hosea', 'Hosea'), ('Yoel', 'Yoel'), ('Amos', 'Amos'), ('Obaja', 'Obaja'), ('Yunus', 'Yunus'), 
              ('Mikha', 'Mikha'), ('Nahum', 'Nahum'), ('Habakuk', 'Habak'), ('Zefanya', 'Zefan'), ('Hagai', 'Hagai'), ('Zakharia', 'Zakha'), 
              ('Maleakhi', 'Malea'), ('Matius', 'Matiu'), ('Markus', 'Marku'), ('Lukas', 'Lukas'), ('Yohanes', 'Yohan'), ('Kisah Para Rasul', 'Kisah'), 
              ('Roma', 'Roma'), ('1 Korintus', '1 Kor'), ('2 Korintus', '2 Kor'), ('Galatia', 'Galat'), ('Efesus', 'Efesu'), ('Filipi', 'Filip'), 
              ('Kolose', 'Kolos'), ('1 Tesalonika', '1 Tes'), ('2 Tesalonika', '2 Tes'), ('1 Timotius', '1 Tim'), ('2 Timotius', '2 Tim'), 
              ('Titus', 'Titus'), ('Filemon', 'Filem'), ('Ibrani', 'Ibran'), ('Yakobus', 'Yakob'), ('1 Petrus', '1 Pet'), ('2 Petrus', '2 Pet'), 
              ('1 Yohanes', '1 Yoh'), ('2 Yohanes', '2 Yoh'), ('3 Yohanes', '3 Yoh'), ('Yudas', 'Yudas'), ('Wahyu', 'Wahyu')]
    return render_template('alkitab.html', title='alkitab', data_bible=data_bible)
