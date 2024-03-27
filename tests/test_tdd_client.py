import unittest


class TestTddClient(unittest.TestCase):

    def test_if_get_entity_returns_dict_given_string(self):
        ne = NamedEntityClient()
        entity = ne.get_entity("")
        self.assertIsInstance(entity, dict)
