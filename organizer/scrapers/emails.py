from organizer.models.emails import Email
from organizer.models.threads import Thread
import os
import dateutil.parser
inbox_path = '/Users/luke/Library/Mail/V2/EWS-lcampbell@mail.asascience.com/Inbox.mbox'

thread_cache = {}

def parse(session,filepath):
    with open(filepath, 'r') as f:
        date        = None
        subjectline = ''
        threadtopic = ''
        for line in f:
            if line.startswith('Subject:'):
                try:
                    subjectline = line.split('Subject: ')[1].strip()
                except IndexError:
                    subjectline = 'None'
                        
            if line.startswith('Date:'):
                try:
                    dateline = line.split('Date: ')[1].strip()
                    date = dateutil.parser.parse(dateline)
                except IndexError:
                    continue # Don't know what to do about the date yet
                except ValueError:
                    print line
                    continue

            if line.startswith('Thread-Topic:'):
                try:
                    threadtopic = line.split('Thread-Topic: ')[1].strip()
                except IndexError:
                    continue

                    
            if line.startswith('Content-Language:'):

                email = Email(filepath,subjectline,date)
                session.add(email)
                
                if threadtopic:
                    # Can build a thread
                    if threadtopic in thread_cache:
                        thread = thread_cache[threadtopic]
                        thread.emails.append(email)
                    else:
                        thread = Thread(threadtopic)
                        session.add(thread)
                        thread.emails = [email]
                        thread_cache[threadtopic] = thread

                break
                        

                
            
def fetch(session,path):
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.emlx'):
                parse(session,os.path.join(dirpath,f))
                
    session.commit()
