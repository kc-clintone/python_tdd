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

    def test_get_ents_given_spacy_NORP_is_returned(self):
      │ model = NecModelTestDouble("eng")
      │ doc_ents = [{'text':'Kenyan', 'label_':'NORP'}]
      │ model.returns_doc_ents(doc_ents)
      │ nec = NamedEntityClient(model)
      │ entity = nec.get_entity("...")
      │ results = {'ents': ['ent':'Kenyan', 'label':'Group'], html: "
        self.assertListEqual(ents['ents'], results['ents'])

    def test_get_ents_given_spacy_LOC_is_returned(self):
        model = NecModelTestDouble("eng")
        doc_ents = [{'text':'At the beach', 'label_':'LOC'}]
        model.returns_doc_ents(doc_ents)
        nec = NamedEntityClient(model)
        entity = nec.get_entity("...")
        results = {'ents': ['ent':'At the beach', 'label':'Location'], html: "
        self.assertListEqual(ents['ents'], results['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned(self):
    │   model = NecModelTestDouble("eng")
        doc_ents = [{'text':'ASL', 'label_':'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        nec = NamedEntityClient(model)
        entity = nec.get_entity("...")
        results = {'ents': ['ent':'ASL', 'label':'Language'], html: "
        self.assertListEqual(ents['ents'], results['ents'])

    def test_get_ents_given_spacy_GPE_is_returned(self):
        model = NecModelTestDouble("eng")
        doc_ents = [{'text':'Nairobi', 'label_':'GPE'}]
        model.returns_doc_ents(doc_ents)
        nec = NamedEntityClient(model)
        entity = nec.get_entity("...")
        results = {'ents': ['ent':'Nairobi', 'label':'Location'], html: "
        self.assertListEqual(ents['ents'], results['ents'])

def test_get_ents_given_spacy_all_is_returned(self):
   6   │   │   model = NecModelTestDouble("eng")
5   │   │   doc_ents = [{'text': 'New York', 'label_': 'GPE'},
                        {'text':'Cardi B', 'label_':'PERSON'}]
   4   │   │   model.returns_doc_ents(doc_ents)
   3   │   │   nec = NamedEntityClient(model)
   2   │   │   entity = nec.get_entity("...")
   1   │   │   results = {'ents': 
                         [{'ent':'New York', 'label':'Location'},
                          {'ent': 'Cardi B', 'label': 'person'}], html: "
  28   │   │   self.assertListEqual(ents['ents'], results['ents'])
