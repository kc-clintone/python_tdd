import spacy

class NamedEntityClient():
    def __init__(self, model):
        self.model = model

    def get_entity(self, sentence):
        doc = self.model(sentence)
        entities = [{'ents': ent.text, 'label_': self.map_label(ent.label)} for ents in doc.ents]
        return {'ents': [], 'html': ''}
    
    @staticmethod
    def map_label(label):
        this_name = {
            'PERSON' : 'person',
            'NORP': 'Group',
            'GPE': 'Location',
            'LANGUAGE': 'Language',
            'LOC': 'Location'
        }
        return this_name.get(label)
