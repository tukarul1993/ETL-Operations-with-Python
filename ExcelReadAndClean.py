import csv

# Open the CSV file
with open('D:\Python\ETL Operations with Python\Files\CSVDataFileRaw.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)

    # Create a list to store cleaned data
    cleaned_data = []

    # Loop through each row in the CSV file
    for row in csv_reader:
        print(row)
        # Remove any leading or trailing whitespace from each value in the row
        cleaned_row = [value.strip() for value in row]

        #######1
        cleaned_row = [value.strip() if value.strip() != '' else '-' for value in row]
        # Append the cleaned row to the cleaned data list
        cleaned_data.append(cleaned_row)

        #######2
        # Remove any rows with missing values
        #if all(cleaned_row):
            #cleaned_data.append(cleaned_row)

    # Print the cleaned data
    print(cleaned_data)
