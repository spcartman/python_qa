import random
import string
import os.path
import jsonpickle
from model.group import Group


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

test_data = [Group(name=name, header=header, footer=footer)
             for name in ("", rand_string("name", 10))
             for header in ("", rand_string("header", 20))
             for footer in ("", rand_string("footer", 20))]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(data_file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(test_data))
