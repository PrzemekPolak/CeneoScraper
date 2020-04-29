#import bibliotek
from flask import Flask

#utworzenie obiektu (instacji) klasy Flask reprezentującego aplikację
app = Flask(__name__)

#import widoków/routingów z aplikacji
from app import views

#uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)


