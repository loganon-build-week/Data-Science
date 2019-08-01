# email parsing flow

# imports
from bs4 import BeautifulSoup, SoupStrainer
from requests import Session
from email import message_from_bytes
import poplib
import time
from decouple import config


EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# first we get the messages from our email server

def get_messages(user, password, server = 'pop.gmail.com'):
    """
    returns a tuple object containing an email messages in field 1
    """
    
    #define our connection
    pop_conn = poplib.POP3_SSL(server)
    pop_conn.user(user)
    pop_conn.pass_(password)
    
    #Get message tuples from server:
    tuples = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    pop_conn.quit()
    
    #returns the message objects in a list, discarding the other fields
    return [msg[1] for msg in tuples]



def get_body(message):
    """
    Uses the email library to get the body of a message and return it.
    """
    em = message_from_bytes(b'\n'.join(message))
    if em.is_multipart():
        return [part.get_payload(decode=True) for part in em.get_payload()]
    else:
        return (em.get_payload(decode=True))


def click_links(message_list):
    """
    Receives a list of poplib message objects and filters out links
    using Beautiful Soup. Then 'clicks' the link using requests.
    """
    
    #get's the body of each message in the message_list
    for message in message_list:
        target = get_body(message)[0]
        
        #BS pulls out all links in the target text and we iterate through them
        for link in BeautifulSoup(target, parse_only=SoupStrainer('a')):
            
            #if the link is clickable we start a requests session and click it
            if link.has_attr('href'):
                s = Session()
                s.get(str(link['href']))
                s.close()
                
                #some bug checking
                print(link['href'])
    
# simple implementation that runs our code every 10 seconds



starttime=time.time()

while True:
    
    message_list = get_messages(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    click_links(message_list)
    time.sleep(60.0 - ((time.time() - starttime) % 10.0))