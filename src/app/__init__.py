from flask import Flask


def create_app(config_name):
    # import here or else manage.py cant update os.environ inside config
    from config import config
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    if not app.config['DEBUG'] and not app.config['TESTING']:
        # configure logging for production
        import logging
        from logging.handlers import SysLogHandler
        handler = SysLogHandler()
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)
    else:
        import logging
        from logging.handlers import RotatingFileHandler
        import os
        handler = RotatingFileHandler(
            os.path.join(app.config['LOG_ROOT'], 'app.log'),
            maxBytes=10000,
            backupCount=1)
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    # module.init_app(app)
    # db.init_app(app)
    # migrate.init_app(app, db)

    # @app.route('/')
    # def index():
    #     return redirect(url_for('mybp.index'))

    return app

