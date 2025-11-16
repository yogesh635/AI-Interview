from flask import Flask
from database.db import db
from routes.session_routes import session_bp

def create_app():
    app = Flask(__name__)

    # Using SQLite for easy local setup. Change SQLALCHEMY_DATABASE_URI as needed.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sessions.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev-secret-key"

    db.init_app(app)

    app.register_blueprint(session_bp, url_prefix="/session")

    @app.route("/")
    def home():
        return {"message": "Session Management API Running!"}

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
