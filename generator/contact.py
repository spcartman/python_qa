import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as error:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

test_data = [Contact()] + [Contact(fname=rand_string("fname", 10), lname=rand_string("lname", 10),
                                   address1=rand_string("address", 30), hphone=rand_string("homeph", 10),
                                   mphone=rand_string("mobileph", 10), email1=rand_string("email1", 15))
                           for i in range(n)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(data_file, "w") as output:
    jsonpickle.set_encoder_options("json", indent=2)
    output.write(jsonpickle.encode(test_data))
