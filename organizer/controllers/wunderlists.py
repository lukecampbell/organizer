from controllers.base_controller import BaseController
from models.wunderlists import WunderList, WunderTask
import yaml

class WunderLists(BaseController):
    def __init__(self, engine, config):
        BaseController.__init__(self, engine)
        with open(config, 'r') as f:
            self.config = yaml.load(f.read())

    def create(self):
        self.create_all(WunderList.__table__, WunderTask.__table__)

    def drop(self):
        self.drop_all(WunderList.__table__, WunderTask.__table__)

    def scrape(self):
        from scrapers.wunderlists import fetch
        fetch(self.session, self.config['auth_string'])


