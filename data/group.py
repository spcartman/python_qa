from model.group import Group
import random
import string


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])

const = [Group(name="test_name", header="test_header", footer="test_footer"),
         Group()]

test_data = [Group(name=name, header=header, footer=footer)
             for name in ("", rand_string("name", 10))
             for header in ("", rand_string("header", 20))
             for footer in ("", rand_string("footer", 20))]
