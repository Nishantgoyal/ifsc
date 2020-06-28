from app import app


@app.route('/')
def home():
    return "Hello To The world!"
