EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
from decouple import config

import poplib
from email import parser

pop_conn = poplib.POP3_SSL("pop.gmail.com")
pop_conn.user(EMAIL_HOST_USER)
pop_conn.pass_(EMAIL_HOST_PASSWORD)
# Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

print(type(messages))
print(len(messages))
print((messages[0]))

# Concat message pieces:
messages = ["\n".join(mssg[1]) for mssg in messages]
# Parse message intom an email object:
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    # print message.keys()
    print(message["subject"])
    print(message["body"])
pop_conn.quit()

# import poplib
# import string, random
# import io, emails
# import logging

# SERVER = "pop.gmail.com"
# USER  = "loganon000"
# PASSWORD = "42lambda"

# # connect to server
# logging.debug('connecting to ' + SERVER)
# server = poplib.POP3_SSL(SERVER)
# #server = poplib.POP3(SERVER)

# # log in
# logging.debug('log in')
# server.user(USER)
# server.pass_(PASSWORD)

# # list items on server
# logging.debug('listing emails')
# resp, items, octets = server.list()

# # download the first message in the list
# id, size = string.split(items[0])
# resp, text, octets = server.retr(id)

# # convert list to Message object
# text = string.join(text, "\n")
# file = io.StringIO(text)
# # message = rfc822.Message(file)

# # output message
# print(text)
# # print(message['From']),
# # print(message['Subject']),
# # print(message['Date']),
# #print(message.fp.read())
