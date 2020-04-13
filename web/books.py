from flask import Flask,Blueprint,render_template

bp = Blueprint('books', __name__)
@bp.route('/')

def index():
    return render_template('index.html',books = get_testdata())

def get_testdata():
    return[
        {'id':1,'title':'プリンキピア','author':'ニュートン','genre':'物理'},
        {'id':2,'title':'科学言論','author':'ラボジュア','genre':'化学'},
        {'id':3,'title':'整数論','author':'ガウス','genre':'数学'}
    ]