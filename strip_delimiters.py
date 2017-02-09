import csv
import glob
import os

filenames = [f.replace('.txt', '') for f in [os.path.basename(x) for x in glob.glob('*.txt')]]

for file in filenames:
        with open(file + '.txt', 'rt') as input:
                with open(file + '_output.txt', 'wt') as output:
                        for line in input:
                                output.write(line.replace(',', ''))
