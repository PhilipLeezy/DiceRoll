import csv

with open('test.csv', 'rt') as input:
        with open('test_output.csv', 'wt') as output:
                for line in input:
                        output.write(line.replace(',', ''))
