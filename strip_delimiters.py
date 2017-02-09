import csv
import glob

for file in glob.glob('*.csv'):
        with open(file, 'rt') as input:
                with open(file + '_output.csv', 'wt') as output:
                        for line in input:
                                output.write(line.replace(',', ''))
