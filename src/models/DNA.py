class DNA:
    def __init__(self, date, dna, blood_sugar_level, emotion_level):
        self.date = date
        self.dna = dna
        self.blood_sugar_level = blood_sugar_level
        self.emotion_level = emotion_level

    def serialize(self):
        return {
            'Date': self.date,
            'DNA': self.dna,
            'Blood sugar level': self.blood_sugar_level,
            'Emotion level': self.emotion_level
        }
