from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/')
    def index():
        return render_template('home.html')

    return app