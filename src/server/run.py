from app import app
app.config.from_object('config')

if __name__ == "__main__":
 app.run(app.config["IP"],debug=app.config["DEBUG"])
