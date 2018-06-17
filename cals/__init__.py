from flask import Flask
from cals.main.routes import main
# from cals.add.routes import add
from cals.config import load_config_for
from cals.utils import get_instance_folder_path

# specifies the main template folder for the application
app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates') 

# enable jinja2 extensions - i.e. continue in for loops
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# apply configuration settings
load_config_for(app)

# register application blueprints
app.register_blueprint(main, url_prefix='/')
# app.register_blueprint(add, url_prefix='/add')
