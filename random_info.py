"""
Module for generating random passwords and emails
"""
import random, string

def generate_address(length=16):
    """
    Generates a random prefix and attaches it to a loganon email address
    """
    tail = '@loganon.33mail.com'

    prefix = ''.join(random.choice(string.ascii_uppercase + 
                    string.ascii_lowercase + string.digits) for _ in range(length))
    return prefix + tail

def generate_password(length=16):
    """
    Generates a random password, default length 16
    """
    password = ''.join(random.choice(string.ascii_uppercase + string.punctuation + 
                    string.ascii_lowercase + string.digits) for _ in range(length))
    return password