from experta import *


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms):
        self.disease_categories = disease_categories
        self.disease_symptoms = disease_symptoms
        super().__init__()

    @DefFacts
    def _initial_action(self):
        yield Fact(action="start")
