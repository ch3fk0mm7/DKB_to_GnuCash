import argparse, csv, os

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Give Name/Path of the Input File.")
parser.add_argument("--output", help="Give Name/Path of the Input File.")
args = parser.parse_args()

outputFile = ''
inputFile = ''

if args.output:
    outputFile = args.output
else:
    outputFile = "GnuCash_Import.csv"

print ('Input File is: ' + os.path.dirname(os.path.realpath(__file__)) + '/' + args.input)
print ('You will find the Result in ' + os.path.dirname(os.path.realpath(__file__)) + '/' + outputFile)



with open(os.path.dirname(os.path.realpath(__file__)) + '/' + args.input, encoding='iso-8859-15') as CsvInputfile:
    inputData = csv.reader(CsvInputfile, delimiter=';')

    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + outputFile, 'w+', encoding='iso-8859-15') as CsvOutputfile:
        outputData = csv.writer(CsvOutputfile, delimiter=';')
        outputData.writerow(['Datum', 'Beschreibung', 'Betrag'])
        row_cnt = 0
        for row in inputData:
            if (row_cnt > 6): #The first 6 lines do not contain transfer details.
                outputData.writerow([row[1], row[2] + ' ' + row[3] + ' ' + row[4], row[7]])
            row_cnt += 1

print ('FINISHED')