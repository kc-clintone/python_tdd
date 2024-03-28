import unittest
from client import NamedEntityClient
from test_doubles import NecModelTestDouble

class TestClient(unittest.TestCase):

    def test_if_get_entity_returns_dict_given_empty_string_returns_empty_spacy(self):
        model = NecModelTestDouble("eng")
        model = returns_doc_ents[()]
        nec = NamedEntityClient(model)
        entity = nec.get_entity("")
        self.assertIsInstance(entity, dict)

    def test_if_get_entity_returns_list_given_non_empty_string_returns_non_empty_spacy(self):
        nec = NamedEntityClient(model)
        model = NecModelTestDouble("eng")
        model = returns_doc_ents[()]
        entity = nec.get_entity("Non-empty string")
        self.assertIsInstance(entity, dict)

    def test_get_ents_given_spacy_PERSON_is_returned(self):
        model = NecModelTestDouble("eng")
        doc_ents = [{'text':'Beyonce', 'label_':'PERSON'}]
        model.returns_doc_ents(doc_ents)
        nec = NamedEntityClient(model)
        entity = nec.get_entity("...")
        results = {'ents': ['ent':'Beyonce', 'label':'person'], html: ""}
        self.assertListEqual(ents['ents'], results['ents'])
