from sys import maxsize


class Contact:

    def __init__(self, id=None, fname=None, mname=None, lname=None, nick=None, title=None, company=None, address1=None,
                 hphone=None, mphone=None, wphone=None, fax=None, email1=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, group=None, address2=None,
                 hphone2=None, notes=None, phones=None, emails=None):
        # TODO: add photo support
        self.id = id
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nick = nick
        self.title = title
        self.company = company
        self.address1 = address1
        self.hphone = hphone
        self.mphone = mphone
        self.wphone = wphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.hphone2 = hphone2
        self.notes = notes
        self.phones = phones
        self.emails = emails

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s' % (self.id, self.fname, self.lname, self.address1, self.emails, self.phones)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.fname is None or other.fname is None or self.fname == other.fname) and \
               (self.lname is None or other.lname is None or self.lname == other.lname) and \
               (self.address1 is None or other.address1 is None or self.address1 == other.address1) and \
               (self.emails is None or other.emails is None or self.emails == other.emails) and \
               (self.phones is None or other.phones is None or self.phones == other.phones)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
