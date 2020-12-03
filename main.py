from modules.builder import ObjectBuilder
from modules.reporter import create_report

# Искомое количество Q и N в процентах
options = {'Q': 10, 'N': 7}

if __name__ == '__main__':
    proteins = ObjectBuilder('data/data_s1.txt')
    proteins.build_proteins(out='A0A1X7R4H5', options=options)

    create_report(proteins, options)
