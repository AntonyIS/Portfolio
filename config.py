import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'portfolio_db')
	DATABASE_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'area-51-top-secret'
