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
            cleaned_row = []
            for i in range(len(row)):
                # Check the data type of the column based on the header name
                column_name = header[i]
                if column_name.startswith('Date'):
                    # If the column starts with 'date', use '1900-01-01' as missing value
                    cleaned_value = row[i].strip() if row[i].strip() != '' else '1900-01-01'
                elif column_name.startswith('Decimal'):
                    # If the column starts with 'numeric', round to 2 decimal places
                    if row[i].strip() != '':
                        cleaned_value = round(float(row[i]), 2) if row[i].strip() != '' else '0.00'
                    else:
                        cleaned_value = 0
                else:
                    # For all other columns, use '-' as missing value
                    cleaned_value = row[i].strip() if row[i].strip() != '' else '-'
                cleaned_row.append(cleaned_value)

            # Append the cleaned row to the cleaned data list
            cleaned_data.append(cleaned_row)

        #remove duplicates
        unique_rows = set()
        for row in cleaned_data:
            # Convert the row to a tuple and add it to the set
            unique_rows.add(tuple(row))

        print(unique_rows)

        cleaned_data = [list(row) for row in unique_rows]
        cleaned_data.sort()
        # Print the cleaned data



        #print(cleaned_data)
        
