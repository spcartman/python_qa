import random
import string
from datetime import datetime
from model.contact import Contact
from data.contacts import test_data as const_contacts


def rand_string(prefix, maxlen):
    chars = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(chars) for i in range(random.randrange(maxlen))])


def generate_contact_data(n):
    if n == "f":
        return const_contacts
    if n == "a":
        return [Contact(fname=fname, lname=lname, address1=address1, hphone=hphone, mphone=mphone, wphone=wphone,
                        email1=email1, email2=email2, email3=email3, byear=byear, hphone2=hphone2)
                for fname in ("", rand_string("fname", 10))
                for lname in ("", rand_string("lname", 10))
                for address1 in ("", rand_string("address1", 30))
                for hphone in ("", rand_string("hphone", 10))
                for mphone in ("", rand_string("mphone", 10))
                for wphone in ("", rand_string("wphone", 10))
                for email1 in ("", rand_string("email1", 15))
                for email2 in ("", rand_string("email2", 15))
                for email3 in ("", rand_string("email3", 15))
                for byear in ("", random.choice([x for x in range(datetime.now().year + 1)]))
                for hphone2 in ("", rand_string("hphone2", 10))]
    return [Contact()] + [Contact(fname=rand_string("fname", 10), lname=rand_string("lname", 10),
                                  address1=rand_string("address", 30), hphone=rand_string("homeph", 10),
                                  mphone=rand_string("mobileph", 10), email1=rand_string("email1", 15))
                          for i in range(int(n))]


# months = ["January", "February", "March", "April", "May", "June", "July",
#           "August", "September", "October", "November", "December"]
#
# Contact(fname=fname, mname=mname, lname=lname, nick=nick, title=title, company=company,
#                         address1=address1, hphone=hphone, mphone=mphone, wphone=wphone, fax=fax, email1=email1,
#                         email2=email2, email3=email3, homepage=homepage, bday=bday, bmonth=random.choice(months),
#                         byear=byear, aday=aday, amonth=random.choice(months), ayear=ayear, group=None,
#                         address2=address2, hphone2=hphone2, notes=notes)
#                 for fname in ("", rand_string("fname", 10))
#                 for mname in ("", rand_string("mname", 10))
#                 for lname in ("", rand_string("lname", 10))
#                 for nick in ("", rand_string("nick", 10))
#                 for title in ("", rand_string("title", 5))
#                 for company in ("", rand_string("company", 10))
#                 for address1 in ("", rand_string("address1", 30))
#                 for hphone in ("", rand_string("hphone", 10))
#                 for mphone in ("", rand_string("mphone", 10))
#                 for wphone in ("", rand_string("wphone", 10))
#                 for fax in ("", rand_string("fax", 10))
#                 for email1 in ("", rand_string("email1", 15))
#                 for email2 in ("", rand_string("email2", 15))
#                 for email3 in ("", rand_string("email3", 15))
#                 for homepage in ("", rand_string("homepage", 20))
#                 for bday in ("", random.choice([x for x in range(1, 32)]))
#                 for byear in ("", random.choice([x for x in range(datetime.now().year + 1)]))
#                 for aday in ("", random.choice([x for x in range(1, 32)]))
#                 for ayear in ("", random.choice([x for x in range(datetime.now().year + 1)]))
#                 for address2 in ("", rand_string("address2", 30))
#                 for hphone2 in ("", rand_string("hphone2", 10))
#                 for notes in ("", rand_string("notes", 50))
