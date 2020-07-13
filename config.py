import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'portfolio_db')
	DATABASE_TRACK_MODIFICATIONS = False
	print('BASECONFIGS')
