import csv

def delete_columns(input_file, output_file):
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.reader(csv_in)
        writer = csv.writer(csv_out)
        for row in reader:
            del row[4]  # Delete fifth column (index 4)
            del row[1]  # Delete second column (index 1)
            writer.writerow(row)

# Replace 'input.csv' and 'output.csv' with your file names
delete_columns('30secondSleepStages_merged.csv', '30secondSleepStages_merged2.csv')
