from flask import Flask

#アプリケーションを作成して与える関数
def create_app():
    app = Flask(__name__)
    
    #books.pyの内容を利用する
    from.import books
    app.register_blueprint(books.bp)

    @app.route('/test')
    
    def apptest():
        return 'アプリケーションセットアップ完了'
    return app

#おまじない
if __name__ == "__main__":
    app.run(debug=True)