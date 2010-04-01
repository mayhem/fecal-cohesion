import os
import logging
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import model

class ProjectList(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        projects = db.GqlQuery("SELECT * FROM Project ORDER BY due") 
        template_values = {
            'user':user.nickname(),
            'projects':projects,
        }

        path = os.path.join(os.path.dirname(__file__), '../template/index')
        self.response.out.write(template.render(path, template_values))
