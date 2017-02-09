import csv
import glob

filenames = glob.glob('*.txt')

for file in filenames:
        file = file.replace('.txt', '')
        with open(file + '.txt', 'rt') as input:
                with open(file + '_output.txt', 'wt') as output:
                        for line in input:
                                output.write(line.replace(',', ''))
