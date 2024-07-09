import pandas as pd


def process_excel_file(input_file, output_file):
    # Load the Excel file
    xls = pd.ExcelFile(input_file)

    # Dictionary to store DataFrames for each sheet
    sheet_data = {}

    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Load the data into a pandas DataFrame
        df = pd.read_excel(xls, sheet_name)

        # Store Participant IDs
        participant_ids = df.iloc[0, :]

        # Count non-empty values per column
        non_empty_counts = df.count()

        # Find columns with less than 35 non-empty values
        columns_to_remove = non_empty_counts[non_empty_counts < 35].index

        # Print removed Participant IDs
        removed_participant_ids = participant_ids[columns_to_remove]
        print(f"Removed Participant IDs for sheet '{sheet_name}':")
        print(removed_participant_ids)

        # Drop columns with less than 35 non-empty values
        df = df.drop(columns=columns_to_remove)

        # Store the processed DataFrame for this sheet
        sheet_data[sheet_name] = df

    # Save the adjusted DataFrames to a new Excel file
    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, df in sheet_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Adjustments completed and saved to", output_file)


# Example usage
input_file = "input.xlsx"
output_file = "output.xlsx"
process_excel_file(input_file, output_file)
