from google.appengine.ext import db

STATUS_NOT_STARTED = 0
STATUS_IN_PROGRESS = 1 
STATUS_WAITING_ON  = 2
STATUS_DONE        = 3

class Project(db.Model):
    owner = db.UserProperty()
    assignee = db.UserProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    due = db.DateTimeProperty(required=True)
    last_updated = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty(required=True)
    notes = db.TextProperty()
    status = db.IntegerProperty()

class Task(db.Model):
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
