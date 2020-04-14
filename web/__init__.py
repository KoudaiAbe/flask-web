from flask import Flask
import os

#アプリケーションを作成して与える関数
def create_app():
    app = Flask(__name__)
    
    #books.pyの内容を利用する
    #同じフォルダ内にあるモジュールbooksを参照
    from . import books,authors
    app.register_blueprint(books.bp)
    app.register_blueprint(authors.bp)

    app.config.form_mapping(
        SECRET_KEY='temp',
        DATABASE=os.path.join(app.instance_path,'bookdb.sqlite3')
    )

    from . import bookdb
    bookdb.init_app(app)

    @app.route('/test')
    
    def apptest():
        return 'アプリケーションセットアップ完了'
    return app

#おまじない
if __name__ == "__main__":
    app.run(debug=True)