import imp
from django.test import SimpleTestCase
from . import calc


class AddTest(SimpleTestCase):
    def test_sum(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
