# email parsing flow

# imports
import poplib, time, webbrowser, re
from decouple import config

EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")


# first we get the messages from our email server


def get_messages(user, password, server="pop.gmail.com"):
    """
    returns a tuple object containing an email messages in field 1
    """

    # define our connection
    pop_conn = poplib.POP3_SSL(server)
    pop_conn.user(user)
    pop_conn.pass_(password)

    # Get message tuples from server:
    tuples = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    pop_conn.quit()

    # returns the message objects in a list, discarding the other fields
    return [msg[1] for msg in tuples]


def get_clean_text(message_list):
    """
    returns a list of email body
    """
    return [" ".join([str(line).strip('b').strip("'") for line in msg]) for msg in message_list]


def get_urls(clean_text):
    """
    returns a link of potentially clickable emails
    """
    for text in clean_text:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
             text)
        return urls


def find_target_urls(url_list):
    """
    Funct to filter out 33mail links and return everything else.
    """
    candidate_urls = []
    
    #iterate through urls
    for url in get_urls(get_clean_text(message_list)):
        #skip any urls from our 33mail mask domain
        if re.findall('33mail', url):
            pass
        #return everything else
        else:
            candidate_urls.append(url)
    return candidate_urls

def click_link(candidate_urls):
    """
    Click all the links.
    """
    for url in candidate_urls:
        webbrowser.open(url)


# simple implementation that runs our code every 10 seconds



starttime = time.time()

while True:

    message_list = get_messages(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print('got messages! ', time.time())
    
    urls = get_urls(get_clean_text(message_list))
    targets = find_target_urls(urls)
    click_link(targets)
    del urls, targets

    print('clicked! ', time.time())
    print('\n')
    time.sleep(((time.time() - starttime) % 10.0))


