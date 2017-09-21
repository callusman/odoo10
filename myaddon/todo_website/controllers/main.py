# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from odoo import exceptions
import odoo
from odoo.exceptions import UserError, ValidationError, QWebException


class Todo(http.Controller):

    @http.route('/helloworld', auth='public')
    def hello_world(self):
        """
        Basic Hello World example
        """
        return '<h1>Hello World!</h1>'

    @http.route('/hello', auth='public')
    def hello(self, **kwargs):
        """
        Hello World using a QWeb template
        Also used for the controller extension example
        """
        return request.render('todo_website.hello')

    @http.route('/hellocms/<page>', auth='public')
    def hellocms(self, page, **kwargs):
        """
        Very simple CMS example
        """
        return request.render(page)

    @http.route('/todo', auth='public', website=True)
    def index(self, **kwargs):
        """
        Todo list page
        """
        TodoTask = request.env['todo.task']
        tasks =  TodoTask.sudo().search([])
        print('tasks debug:')
        print(tasks)
        return request.render(
            'todo_website.index', {'tasks': tasks})

    @http.route('/todo/<model("todo.task"):task>', auth='public', website=True)
    def detail(self, task, **kwargs):
        """
        Todo detail page
        """
        return request.render(
            'todo_website.detail', {'task': task})

    @http.route('/todo/add', auth='public', website=True)
    def add(self, **kwargs):
        """
        Form to add a new Todo Task
        """
        if request.env.ref('base.public_user').id == request.uid:
            ##request.render('website.404')
            ##raise exceptions.Warning('You %s must login.' % 'public')
            return request.render('website.http_error', {'status_code': 'Forbidden', 'status_message': 'You must login.'})
        users = request.env['res.users'].search([])
        return request.render(
            'todo_website.add', {'users': users})
