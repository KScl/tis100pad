from app import app
app.config.from_object('config')

app.run(app.config["IP"],debug=app.config["DEBUG"])
