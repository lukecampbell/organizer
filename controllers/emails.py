from models.emails import Email
import os
import dateutil.parser
import calendar
inbox_path = '/Users/luke/Library/Mail/V2/EWS-lcampbell@mail.asascience.com/Inbox.mbox'
def parse_subject(session,filepath):
    with open(filepath, 'r') as f:
        date        = None
        subjectline = ''
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
                    
            if date and subjectline:
                email = Email(filepath,subjectline,date)
                session.add(email)
                break
                        

                
            
def fetch(session,path):
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.emlx'):
                parse_subject(session,os.path.join(dirpath,f))
                
    session.commit()
