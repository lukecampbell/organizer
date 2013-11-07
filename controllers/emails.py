from controllers.base_controller import BaseController
from models.emails import Email
from models.threads import Thread


class Emails(BaseController):

    def create(self):
        self.create_all(Email.__table__, Thread.__table__)

    def drop(self):
        self.drop_all(Email.__table__, Thread.__table__)

    def scrape(self):
        from scrapers.emails import inbox_path, fetch
        fetch(self.session, inbox_path)





