import csv

def save_data(blood_data):
    with open(r'C:/Users/khtat/PycharmProjects/Examen_FDI_CapsuleCorp/src/db/statistics.csv', 'a') as file:
        header = ['date', 'dna', 'blood_sugar_level', 'emotion_level']
        writer = csv.DictWriter(file, fieldnames=header)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(blood_data)
