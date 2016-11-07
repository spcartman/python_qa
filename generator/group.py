import random
import string
from model.group import Group
from data.groups import test_data as const_groups


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])


def generate_group_data(n):
    if n == "f":
        return const_groups
    if n == "a":
        return [Group(name=name, header=header, footer=footer)
                for name in ("", rand_string("name", 10))
                for header in ("", rand_string("header", 20))
                for footer in ("", rand_string("footer", 20))]
    return [Group()] + [Group(name=rand_string("na", 10), header=rand_string("he", 20), footer=rand_string("fo", 20))
                        for i in range(int(n))]
