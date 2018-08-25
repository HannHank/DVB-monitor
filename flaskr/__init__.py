import os

from flask import Flask
import requests
import json
from flask import render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # a simple page that says hello
    @app.route('/DVB')
    def hello(): 
       url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?ort=Freital&hst=Burgker"

       response = requests.get(url)

       HTL = json.loads(response.content)
 
       

       linie = HTL[0]
       linie2 = HTL[1]
       linie3 = HTL[2]
       linie4 = HTL[3]

      # HTL = HTL['list'][0]['main']['humidity']

       

    #weather_Temp.round(2)

    #weather_Temp = math.ceil(weather_Temp)

    
       return render_template('base.html', linie = linie,linie2 = linie2,linie3 = linie3,linie4 = linie4)

    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    return app