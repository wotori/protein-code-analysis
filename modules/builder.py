from modules.protein import Protein


class ObjectBuilder:
    doc = None

    def __init__(self, doc):
        self.doc = doc
        self.objects_n = []
        self.objects_q = []

    def build_proteins(self, out, options):
        with open(self.doc, 'r') as data:
            lines = data.readlines()
        for n, stroke in enumerate(lines):
            if stroke[0] == '>':
                if stroke[4:14] == out:
                    break
                cur_protein = Protein(name=lines[n][:-1], sequence=lines[n + 1])
                cur_protein.self_analysis()
                self.check_options(cur_protein, options)

    def check_options(self, cur_protein, options):
        if cur_protein.n_percent != 'unsuitable':
            if cur_protein.n_percent >= options['N']:
                self.objects_n.append(cur_protein)
        if cur_protein.q_percent != 'unsuitable':
            if cur_protein.q_percent >= options['Q']:
                self.objects_q.append(cur_protein)
