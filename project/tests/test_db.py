import unittest
import os
import sys

p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)

from project.db import _setup_db, _teardown_db


def setUpModule():
    _setup_db()


def tearDownModule():
    _teardown_db()


class TestDBView(unittest.TestCase):
    def setUp(self):
        from project.models import DBSession
        self.session = DBSession

    def _setup_entry(self, **kwargs):
        from project.models import Entry
        entry = Entry(**kwargs)
        self.session.add(entry)
        return entry

    def _callFUT(self, entry_id):
        pass

    def test_it(self):
        e = self._setup_entry(name=u"this-is-test")
        result = self._callFUT(entry_id=e.id)
        self.assertEqual(result["name"], e.name)

