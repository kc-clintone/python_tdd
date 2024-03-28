import unittest
from client import NamedEntityClient

class TestClient(unittest.TestCase):

    def test_if_get_entity_returns_dict_given_string(self):
        nec = NamedEntityClient()
        entity = nec.get_entity("")
        self.assertIsInstance(entity, dict)
