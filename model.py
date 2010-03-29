import time
import datetime
from google.appengine.ext import db
from lib import age

STATUS_NOT_STARTED = 0
STATUS_IN_PROGRESS = 1 
STATUS_WAITING_ON  = 2
STATUS_DONE        = 3
status_text = ('not started', 'in progress', 'waiting on', 'done')

class Project(db.Model):
    id = db.IntegerProperty()
    owner = db.UserProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    due = db.DateTimeProperty(required=True)
    last_updated = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty(required=True)
    notes = db.TextProperty()
    status = db.IntegerProperty()

    def status_text(self):
        return status_text[self.status]

    def last_updated_text(self):
        return age.age(int(time.time()) - time.mktime(self.last_updated.timetuple()))

class Task(db.Model):
    id = db.IntegerProperty()
    project = db.ReferenceProperty(Project)  # may be None
    owner = db.UserProperty()
    assignee = db.UserProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    due = db.DateTimeProperty()
    last_updated = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    notes = db.TextProperty()
    status = db.IntegerProperty(required=True)
    ancestor = db.SelfReferenceProperty(collection_name="ancestor_set")
    dependent = db.SelfReferenceProperty(collection_name="dependent_set")
