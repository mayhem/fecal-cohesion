import os
from datetime import datetime
import cgi
import logging
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import model

class UpdateProject(webapp.RequestHandler):
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
        stash['due_date'] = self.request.get('due_date')
        stash['due_time'] = self.request.get('due_time')
        stash['notes'] = self.request.get('notes')

        logging.error("'%s' - '%s'" % (stash['due_date'] + " " + stash['due_time'], "%m/%d/%Y %H:%M"))
        try:
            due = datetime.strptime(stash['due_date'] + " " + stash['due_time'], "%m/%d/%Y %H:%M")
        except ValueError:
            due = None

        if not due:
            stash['error'] = u"Invalid date/time format. Please use MM/DD/YYYY and HH:MM"
        elif not self.request.get('name'):
            stash['error'] = u"Please fill in the project name."
        elif not self.request.get('due_date'):
            stash['error'] = u"Please select a due date."
        elif not self.request.get('due_time'):
            stash['error'] = u"Please select a due time."
        else:
            proj = model.Project(name = stash['name'], due = due)
            proj.notes = stash['notes']
            proj.status = model.STATUS_NOT_STARTED
            proj.owner = user;
            proj.assignee = user;
            if proj.put():
                proj.id = proj.key().id()
                proj.put()
                stash = {}
                stash['notice'] = u'Project saved.'
            else:
                stash['error'] = u'Saving the project failed. :-('

        path = os.path.join(os.path.dirname(__file__), '../template/p/update')
        self.response.out.write(template.render(path, stash))
