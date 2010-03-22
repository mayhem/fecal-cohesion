import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from controller import newproject, projectlist

application = webapp.WSGIApplication( 
[
    ('/', projectlist.ProjectList),
    ('/p/new', newproject.NewProject),
#    ('/p/', projectlist.ViewProjectPage)
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
