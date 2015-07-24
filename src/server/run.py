from app import app as application
application.config.from_object('config')

application.run(app.config["IP"],debug=app.config["DEBUG"])
