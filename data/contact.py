import random
import string
from model.contact import Contact


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

const = [Contact(fname="test_name", lname="test_lastname", hphone="+375 (29) 882-74-15", email1="foo@mail.kom"),
         Contact()]

test_data = [Contact()] + [Contact(fname=rand_string("fname", 10), lname=rand_string("lname", 10),
                                   address1=rand_string("address", 30), hphone=rand_string("homeph", 10),
                                   mphone=rand_string("mobileph", 10), email1=rand_string("email1", 15))
                           for i in range(2)]
