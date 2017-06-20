# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SRC_ROOT = os.path.dirname(os.path.abspath(__file__))   # application_top
    APP_ROOT = os.path.join(SRC_ROOT, 'app')
    APP_STATIC = os.path.join(APP_ROOT, 'static')

    LOG_ROOT = os.environ.get('LOG_ROOT') or os.path.join(SRC_ROOT, 'log')
    UPLOADS_ROOT = os.environ.get('UPLOADS_ROOT') or os.path.join(SRC_ROOT, 'uploads')
    DOCS_ROOT = os.environ.get('DOCS_ROOT') or os.path.join(SRC_ROOT, 'docs')

    SECRET_KEY = os.environ.get('SECRET_KEY', 'CHANGETHISSTRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_ENABLED = os.environ.get('DEBUG_TB_ENABLED', False)
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    LANGUAGES = {
        'en': 'English',
        'es': 'Español'
    }
    ITEMS_PER_PAGE = 10
    ZENDESK_SUBDOMAIN = os.environ.get('ZENDESK_SUBDOMAIN', None)
    ZENDESK_EMAIL = os.environ.get('ZENDESK_EMAIL', None)
    ZENDESK_TOKEN = os.environ.get('ZENDESK_TOKEN', None)
    ZENDESK_OAUTH_TOKEN = os.environ.get('ZENDESK_OAUTH_TOKEN', None)


class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG') or True
    TESTING = os.environ.get('TESTING') or False
    DEBUG_TB_ENABLED = os.environ.get('DEBUG_TB_ENABLED', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    DEBUG = os.environ.get('DEBUG') or False
    TESTING = os.environ.get('TESTING') or True
    DEBUG_TB_ENABLED = os.environ.get('DEBUG_TB_ENABLED', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    DEBUG = os.environ.get('DEBUG') or False
    TESTING = os.environ.get('DEBUG') or False
    DEBUG_TB_ENABLED = os.environ.get('DEBUG_TB_ENABLED', False)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
