from organizer.models.wunderlists import WunderTask, WunderList
from wunderpy import Wunderlist
import dateutil.parser
import base64

def fetch(session, auth_string):
    s = base64.b64decode(auth_string)
    u, p = s.split(':')
    w = Wunderlist()
    w.login(u,p)
    w.update_lists()

    for wunderlist, listinfo in w.lists.iteritems():
        try:
            wl = WunderList()
            wl.id = listinfo['id']
            wl.title = listinfo['title']
            session.add(wl)
        except:
            continue

        for taskname, task in listinfo['tasks'].iteritems():
            try:
                wt = WunderTask()
                wt.id = task['id']
                wt.title = task['title']

                wt.completed_at = dateutil.parser.parse(task['completed_at'])
                wt.note = task['note']
                # TODO: add parsing and line linking here!
                session.add(wt)
                wl.tasks.append(wt)
            except:
                continue
    session.commit()




