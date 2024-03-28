import unittest
from client import NamedEntityClient
from tests.test_doubles import NecModelTestDouble

class TestClient(unittest.TestCase):

    def test_if_get_entity_returns_dict_given_empty_string_returns_empty_spacy(self):
        model = NecModelTestDouble("eng")
        model = returns_doc_ents[()]
        nec = NamedEntityClient(model)
        entity = nec.get_entity("")
        self.assertIsInstance(entity, dict)

    def test_if_get_entity_returns_list_given_non_empty_string_given_string(self):
        nec = NamedEntityClient(model)
        model = NecModelTestDouble("eng")
        entity = nec.get_entity("Non-empty string")
        self.assertIsInstance(entity, dict)
