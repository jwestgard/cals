import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


config = {
    "development": "cals.config.DevelopmentConfig",
    "testing": "cals.config.TestingConfig",
    "default": "cals.config.DevelopmentConfig"
}


def load_config_for(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
