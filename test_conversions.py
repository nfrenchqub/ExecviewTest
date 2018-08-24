from unittest import TestCase
from .Conversions import Conversions


class TestConversions(TestCase):
    def test_ft_in_to_in(self):
        self.assertEqual(Conversions.ft_in_to_in('1 ft 0 in'), 12)
        self.assertEqual(Conversions.ft_in_to_in('6 ft 2 in'), 74)
        self.assertRaises(ValueError, lambda: Conversions.ft_in_to_in('5 ft'))
        self.assertRaises(ValueError, lambda: Conversions.ft_in_to_in('24 in'))
        self.assertRaises(ValueError, lambda: Conversions.ft_in_to_in('230'))

    def test_lbs_value(self):
        self.assertEqual(Conversions.lbs_value('1 lb'), 1)
        self.assertEqual(Conversions.lbs_value('600 lb'), 600)
        self.assertRaises(ValueError, lambda: Conversions.lbs_value('5 lb 1 oz'))
        self.assertRaises(ValueError, lambda: Conversions.lbs_value('230'))
