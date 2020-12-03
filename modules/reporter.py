from modules.builder import ObjectBuilder
from modules.protein import Protein


def create_report(objects: ObjectBuilder, settings):
    with open('report.txt', 'w') as report:
        report.write(f'текущие параметры поиска - {settings}\n')
        report.write(f'параметрам соответствуют по N - {len(objects.objects_n)}, по Q - {len(objects.objects_q)}\n\n')

        report.write(f'Список белков по соответствию параметра N \n\n')
        for n, object_n in enumerate(objects.objects_n):
            object_n: Protein
            report.write(f'Белок №: {n + 1} \n')
            report.write(f'Name: \n{object_n.name} \n')
            report.write(f'Sequence: \n{object_n.amino_acid_sequence} \n')
            report.write(f'Процентное отношение символа N ко всем остальным \n{object_n.n_percent} \n')
            report.write(f'Количество повторений символа N: \n{object_n.n_number_of_repetitions} \n')
            for i in range(3):
                report.write('\n')

        for i in range(10):
            report.write('\n')

        report.write(f'Список белков по соответствию параметра Q\n\n')
        for n, object_q in enumerate(objects.objects_q):
            object_q: Protein
            report.write(f'Белок №: {n + 1} \n')
            report.write(f'Name: \n{object_q.name} \n')
            report.write(f'Sequence: \n{object_q.amino_acid_sequence} \n')
            report.write(f'Процентное отношение символа Q ко всем остальным \n{object_q.q_percent} \n')
            report.write(f'Количество повторений символа Q: \n{object_q.q_number_of_repetitions} \n')
            for i in range(3):
                report.write('\n')
