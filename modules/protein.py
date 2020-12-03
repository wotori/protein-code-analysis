from collections import Counter


class Protein:
    q_number_of_repetitions = None
    q_percent = None
    n_number_of_repetitions = None
    n_percent = None

    def __init__(self, name, sequence):
        self.name = name
        self.amino_acid_sequence = sequence

    def self_analysis(self):
        for n, letter in enumerate(self.amino_acid_sequence):
            if letter == 'Q':
                if self.amino_acid_sequence[n + 1] == 'Q' and self.amino_acid_sequence[n + 2] == 'Q':
                    self.get_usage_percent('Q')
                    break
                else:
                    self.q_number_of_repetitions = 'unsuitable'
                    self.q_percent = 'unsuitable'

        for n, letter in enumerate(self.amino_acid_sequence):
            if letter == 'N':
                if self.amino_acid_sequence[n + 1] == 'N' and self.amino_acid_sequence[n + 2] == 'N':
                    self.get_usage_percent('N')
                    break
                else:
                    self.n_number_of_repetitions = 'unsuitable'
                    self.n_percent = 'unsuitable'

    def get_usage_percent(self, letter):
        counted = Counter(self.amino_acid_sequence)
        if letter == 'Q':
            self.q_number_of_repetitions = counted[letter]
            self.q_percent = self.q_number_of_repetitions / (len(self.amino_acid_sequence) / 100)
        if letter == 'N':
            self.n_number_of_repetitions = counted[letter]
            self.n_percent = self.n_number_of_repetitions / (len(self.amino_acid_sequence) / 100)
