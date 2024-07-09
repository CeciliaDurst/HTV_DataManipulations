import pandas as pd


def impute_missing_values_for_each_sheet(input_file, output_file):
    # Load the dataset
    xls = pd.ExcelFile(input_file)

    # Dictionary to store DataFrames for each sheet
    sheet_data = {}

    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)

        # Function to impute missing values with mean for each participant
        def impute_missing_values(df):
            participants = df.columns[1:]  # Exclude the first column which is Participant ID
            for participant in participants:
                # Check if participant has any missing values
                if df[participant].isnull().any():
                    # Find the index of the last non-null value
                    last_non_empty_index = df[participant].last_valid_index()
                    if last_non_empty_index is not None:
                        # Calculate mean for values before the last non-null value
                        mean_value = df.loc[:last_non_empty_index, participant].mean()
                        # Impute missing values with mean for that participant
                        df.loc[:last_non_empty_index, participant].fillna(mean_value, inplace=True)
            return df

        # Impute missing values for this sheet
        df_imputed = impute_missing_values(df)

        # Store the imputed DataFrame for this sheet
        sheet_data[sheet_name] = df_imputed

    # Save the adjusted DataFrames to a new Excel file
    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, df in sheet_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Imputed data saved to:", output_file)


input_file = "cleaned_dataset-path"
output_file = "mean imputed file"
impute_missing_values_for_each_sheet(input_file, output_file)
