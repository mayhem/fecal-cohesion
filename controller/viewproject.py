import os
import logging
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db
import model

class ViewProject(webapp.RequestHandler):
    def get(self, id):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        projects = db.GqlQuery("SELECT * FROM Project WHERE id = :id", id = int(id)) 
        project = projects[0]

        template_values = {
            'user':user.nickname(),
            'project':project
        }

        path = os.path.join(os.path.dirname(__file__), '../template/p/view')
        self.response.out.write(template.render(path, template_values))
