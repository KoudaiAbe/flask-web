from flask import (Blueprint, render_template)

bp = Blueprint('authors', __name__)

@bp.route('/authors/<author>')
def show(author):
    return render_template('authors.html', data=search_author(author))

def get_authors():
    return [
        {'author':'ニュートン', 
        'bio':'「なぜリンゴが木から落ちるのかという疑問から万有引力の法則を発見した」という伝説がある' },
        {'author':'ラボアジェ',
        'bio': '質量保存則を発見、フロギストン説を打破、フランス革命で命を落とす'},
        {'author':'ガウス',
         'bio':'最小二乗法、ガウス分布、ガウスの定理など代数幾何・電磁気学など多岐にわたり活躍した'},
        {'author':'コペルニクス', 
        'bio':'地動説を提唱し、良貨が悪貨を駆逐するとも言った。「コペルニクス的転回」という言葉で有名'},
        {'author':'フーリエ',
        'bio':'フーリエ級数、フーリエ変換は熱伝導、波動解析などの分野で多大な貢献'},
        {'author':'関孝和',
         'bio':'鎖国の日本で独自に和算を研究し、解析学や円周率の計算を行った'},

    ]

def search_author(author):
    alldata = get_authors()
    for data in alldata:
        if author==data['author']:
           return data

