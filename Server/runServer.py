from app import make_app

app = make_app()

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
