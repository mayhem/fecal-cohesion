import os
import datetime
import cgi
import logging
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import model

class NewProject(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))

        path = os.path.join(os.path.dirname(__file__), '../template/p/new')
        self.response.out.write(template.render(path, None))

    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))

        stash = {} 
        stash['name'] = self.request.get('name')
        stash['due'] = self.request.get('due')
        stash['notes'] = self.request.get('notes')
        if not self.request.get('name'):
            stash['error'] = u"Please fill in the project name."
        elif not self.request.get('due'):
            stash['error'] = u"Please select a due date."
        elif not self.request.get('notes'):
            stash['error'] = u"Notes are empty!."
        else:
            proj = model.Project(name = stash['name'], due = stash['due'])
            proj.notes = stash['notes']
            if proj.put():
                stash = {}
                stash['notice'] = u'Project saved.'
            else:
                stash['error'] = u'Saving the project failed. :-('

        path = os.path.join(os.path.dirname(__file__), '../template/p/new')
        self.response.out.write(template.render(path, stash))


