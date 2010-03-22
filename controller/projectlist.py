import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class ProjectList(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))

        template_values = {
            'user':user.nickname()
        }

        path = os.path.join(os.path.dirname(__file__), '../template/index')
        self.response.out.write(template.render(path, template_values))
