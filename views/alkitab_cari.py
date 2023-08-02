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
alkitab_cari_blueprint = Blueprint('alkitab_cari', __name__)


# Cari Alkitab
@alkitab_cari_blueprint.route('/alkitab/cari')
def alkitab_cari():
    main_input = request.args.get('search_verse')
    print("input : ", main_input)
    main_input = main_input.replace("-"," ").replace(":", " ")
    search_input = main_input.split()

    try:
        int(search_input[1])
    except ValueError :
        search_input[0] = f"{search_input[0]}_{search_input[1]}"
        search_input.pop(1)
    finally:
        bible_title = search_input[0]

        if len(search_input) == 1:
            search_input.append("1")
        bible_chapter = search_input[1]

        if len(search_input) == 2:
            for i in os.listdir('static/assets/alkitab'):
                if (i[:len(bible_title)].lower() == bible_title.lower()):
                    with open(f"static/assets/alkitab/{i}/{i}_{bible_chapter}.txt") as open_bible:
                        book = (f"{i.replace('_',' ')} {bible_chapter}:")
                        book = book.replace("Raja Raja", "Raja-Raja").replace("Hakim Hakim", "Hakim-Hakim")
                        verses = open_bible.readlines()
                        book += f"1-{len(verses)}"
                        verse = ""
                        for j in verses:
                            verse += j.replace("\n","")
                            verse += "\n"
                        result = [book,verse]
                        return jsonify(result)

                        
        first_verse = int(search_input[2])

        if len(search_input) == 3:
            search_input.append(first_verse)
        second_verse = int(search_input[3])

        for i in os.listdir('static/assets/alkitab'):
            if (i[:len(bible_title)].lower() == bible_title.lower()) :
                try:
                    with open(f"static/assets/alkitab/{i}/{i}_{bible_chapter}.txt") as open_bible:
                        read_body = open_bible.readlines()
                        read_body[first_verse-1] 
                        read_body[second_verse-1]
                        book = (f"{i.replace('_',' ')} {bible_chapter}:")
                        book = book.replace("Raja Raja", "Raja-Raja").replace("Hakim Hakim", "Hakim-Hakim")
                        if (first_verse == second_verse):
                            book += str(first_verse)
                        else:
                            book += f"{first_verse}-{second_verse}"
                        verse = ""
                        for j in read_body[first_verse-1:second_verse]:
                            verse += j.replace("\n","")
                            verse += "\n"
                        result = [book, verse]
                        return jsonify(result)
                except Exception:
                    return jsonify(['Tidak Ditemukan','Ayat tidak ditemukan'])
        return jsonify(['Tidak Ditemukan','Kitab tidak ditemukan'])
