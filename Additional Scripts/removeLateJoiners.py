import pandas as pd


def remove_participant_columns(input_file, output_file, participant_names):
    # Load the Excel file
    xls = pd.ExcelFile(input_file)

    # Dictionary to store DataFrames for each sheet
    sheet_data = {}

    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)

        # Track removed participant names for this sheet
        removed_names = []

        # Iterate through each participant name
        for participant_name in participant_names:
            # Check if the participant name is in the first row
            if any(df.iloc[0] == participant_name):
                # Remove the column if found
                df = df.loc[:, df.iloc[0] != participant_name]
                removed_names.append(participant_name)

        # Store the DataFrame for this sheet
        sheet_data[sheet_name] = df

        # Print removed participant names for this sheet
        if removed_names:
            print(f"Removed participant names '{', '.join(removed_names)}' from sheet '{sheet_name}'")

    # Save the adjusted DataFrames to a new Excel file
    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, df in sheet_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Adjusted data saved to:", output_file)


# Example usage
input_file = "dateShiftedData5.xlsx"
output_file = "dateShiftedData6.xlsx"
participant_names = ["30726", "31003", "31235", "31236", "31237"] #example, manually input late joiners
remove_participant_columns(input_file, output_file, participant_names)
