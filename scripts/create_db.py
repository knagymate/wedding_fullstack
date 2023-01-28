import os

from app.app import app, db

with app.app_context():
    if os.path.exists("instance/project.db"):
        os.remove("instance/project.db")
    db.create_all()
    os.chmod("instance/project.db", 0o0777)
