from models.jiratasks import JiraTask
import feedparser
import base64
from time import mktime
from datetime import datetime



def fetch(session, url, auth_string='', user='', password=''):
    if not auth_string:
        auth_string = base64.b64encode('%s:%s' % user, password)
    feed = feedparser.parse(url, request_headers={'Authorization':'Basic %s' % auth_string})
    url += '&os_authType=basic'
    for entry in feed['entries']:
        try:
            task = JiraTask()
            task.key = int(entry['key']['id'])
            task.assignee = entry['assignee']['username']
            if 'component' in entry:
                task.component = entry['component']
            task.created =datetime.fromtimestamp(mktime(entry['created_parsed']))
            if 'fixversion' in entry:
                task.fixversion = entry['fixversion']
            task.link = entry['link']
            if 'parent' in entry and 'id' in entry['parent']:
                task.parent = int(entry['parent']['id'])
            task.priority = int(entry['priority']['id'])
            task.project = entry['project']['key']
            task.reporter = entry['reporter']['username']
            task.status = entry['status']['id']
            task.summary = entry['summary']
            task.title = entry['title']
            task.task_type = int(entry['type']['id'])
            task.updated = datetime.fromtimestamp(mktime(entry['updated_parsed']))

            session.add(task)
        except Exception as e:
            print e
            continue

