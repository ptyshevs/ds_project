from unittest import TestCase
from form_mapper import map_params


class TestMap_params(TestCase):
    def test_map_params(self):
        mapped = map_params(
            age="20-22",
            country="US",
            industry="Tech",
            role="DataScientist",
            experience="10",
            q11="Some answer")

        self.assertFalse(mapped.empty)
