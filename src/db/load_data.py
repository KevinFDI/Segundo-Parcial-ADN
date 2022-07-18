import csv
from src.models.DNA import DNA

def load_data():
    data = []

    with open(r'C:/Users/khtat/PycharmProjects/Examen_FDI_CapsuleCorp/src/db/statistics.csv', 'r') as file:
        rows = csv.DictReader(file)
        for row in rows:
            data.append(DNA(
                row['date'],
                row['dna'],
                row['blood_sugar_level'],
                row['emotion_level']
                )
            )
        return data


