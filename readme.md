__init__.py

🔁 Summary of What This Does
Functionality	Purpose
Flask(__name__)	Creates the app instance
app.config.from_object	Loads config values (DB URI, secret key) from a Python class
db.init_app(app)	Connects SQLAlchemy to this Flask app
register_blueprint()	Adds all the routes from app/routes.py to the app
return app	Makes the app ready to be run or tested


