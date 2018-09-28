#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import current_app
from flask_script import Manager

from app import create_app
# from app import db
from zenpy import Zenpy
from dateutil.parser import parse

if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
logger = app.logger
creds = {
    'email': app.config.get('ZENDESK_EMAIL', None),
    'token': app.config.get('ZENDESK_TOKEN', None),
    'subdomain': app.config.get('ZENDESK_SUBDOMAIN', None)
}


def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60) % 60


@manager.command
def zdviewtest(view_title):
    zd_client = Zenpy(**creds)
    view = next(iter(zd_client.views.search(query=view_title) or []), None)
    print(view.title)
    for ticket in zd_client.views.tickets(view):
        metrics = zd_client.tickets.metrics(ticket.id)
        dd, hh, mm = days_hours_minutes(
            parse(metrics.status_updated_at) - parse(metrics.created_at))
        print(u"{0};{1};{2};{3};{4};{5};{6};{7}".format(
            ticket.id,
            ticket.subject,
            ticket.status,
            metrics.created_at,
            metrics.status_updated_at,
            dd, hh, mm
        ))


if __name__ == '__main__':
    manager.run()

