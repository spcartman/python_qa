import random
import string
import os.path
import json
from model.contact import Contact


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

test_data = [Contact()] + [Contact(fname=rand_string("fname", 10), lname=rand_string("lname", 10),
                                   address1=rand_string("address", 30), hphone=rand_string("homeph", 10),
                                   mphone=rand_string("mobileph", 10), email1=rand_string("email1", 15))
                           for i in range(2)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contact.json")

with open(data_file, "w") as f:
    f.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
