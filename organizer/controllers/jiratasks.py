from organizer.controllers.base_controller import BaseController
from organizer.models.jiratasks import JiraTask
import yaml

class JiraTasks(BaseController):
    def __init__(self, engine, config):
        BaseController.__init__(self, engine)
        with open(config, 'r') as f:
            self.config = yaml.load(f.read())

    def create(self):
        self.create_all(JiraTask.__table__)

    def drop(self):
        self.drop_all(JiraTask.__table__)

    def scrape(self):
        from organizer.scrapers.jiratasks import fetch
        fetch(self.session, self.config['feed'], self.config['auth_string'])

