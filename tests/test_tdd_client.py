import unittest
from client import NamedEntityClient

class TestClient(unittest.TestCase):

    def test_if_get_entity_returns_dict_given_string(self):
        model = NecModelTestable("eng")
        nec = NamedEntityClient(model)
        entity = nec.get_entity("")
        self.assertIsInstance(entity, dict)

    def test_if_get_entity_returns_list_given_non_empty_string_given_string(self):
        nec = NamedEntityClient(model)
        entity = nec.get_entity("Non-empty string")
        self.assertIsInstance(entity, dict)
