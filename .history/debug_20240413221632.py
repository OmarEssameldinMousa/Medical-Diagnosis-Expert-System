from main import *
category, diseases_list = disease_categories[5]
for dis in diseases_list:
    for symp in self.disease_symptoms[dis]:
        query = input(f"Do you have - {symp}?: ").strip()
        if query in ["Yes", "yes", "y", "Y"]:
            possibilities[dis] = 1 + possibilities.get(dis, 0)
