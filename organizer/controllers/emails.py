from organizer.controllers.base_controller import BaseController
from organizer.models.emails import Email
from organizer.models.threads import Thread
import yaml


class Emails(BaseController):

    def __init__(self, engine, config):
        BaseController.__init__(self, engine)
        with open(config, 'r') as f:
            self.config = yaml.load(f.read())

    def create(self):
        self.create_all(Email.__table__, Thread.__table__)

    def drop(self):
        self.drop_all(Email.__table__, Thread.__table__)

    def scrape(self):
        from organizer.scrapers.emails import fetch
        for mailbox in self.config['mailboxes']:
            fetch(self.session, mailbox)





