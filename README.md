# HTV_DataManipulations README

This repository contains code files for data cleaning and analysis related to Happy Teacher Study.

**ADJUST PATHS IN SCRIPTS**

**ADJUST PATHS IN SCRIPTS**

**ADJUST PATHS IN SCRIPTS**



Preliminary documentation (work in progress): https://docs.google.com/document/d/1BB6k-0zNwT7P7-6zY3-PADZHw_7UPci7GkWkgi--fG8/edit?usp=sharing

## Data Cleaning Scripts

### 1. Data_Cleaning_v03_RC(1).ipynb

- **Purpose:** Designed to turn raw files into usable clean datasets.
- **Usage:**
  - Use raw datasets directly exported from fitabase.
  - In the second box, uncomment to filter and produce a new weartime file with 0s allocated to invalid datapoints. 
    - Use cleaned weartime dataset generated from normal running and file generating made using this script.

### 2. compareConsentDates.py

- **Purpose:** Optional tool to compare consent dates between raw consent date and raw dataset to identify potential inequivalencies.
- **Usage:**
  - Use consent date file and the raw dataset.

### 3. findConsentDates.py

- **Purpose:** Optional tool to identify and make a consent date file for beta testing.

### 4. zeroAllocate.py

- **Purpose:** Based on Wear Time threshold 10-hour invalid limit, allocate zeros to another dataset.
- **Usage:**
  - Use cleaned and filtered threshold weartime dataset as the base to allocate 0s to another non-weartime dataset.

## Weekday and Weekend Scripts

### 1. DATESHIFTERfinal.py

- **Purpose:** Using the earliest consent date as the reference date, this is designed to alter the cleaned data sets in a way where constant dates are established instead of numbered days for the first row and every data point aligns with its corresponding date for each participant.
- **Usage:**
  - Use clean and filtered threshold datasets.

### 2. aligner.py

- **Purpose:** Optional tool to print out differences between reference date and first dates of each participant.

### 3. daytimesubtract.py

- **Purpose:** Create another variable and Excel sheet called TotalDayTimeWearTime.
- **Usage:**
  - Takes the difference between TotalMinutesWearTime and TotalTimeInBed.

### 4. weekendHighlights.py

- **Purpose:** Optional tool to highlight data points that align on weekend dates.

### 5. weeklyaverages.py

- **Purpose:** Generate a new file consisting of weekday and weekend averages for each participant.
- **Usage:**
  - Use file generated from DATESHIFTERfinal.py script.

## Data Analysis Scripts

### 1. Data_Cleaning_Analysis.py

- **Purpose:** Generate average and standard deviations of first and last consecutive 5-day spans with inclusion of number of days statistics related to study.
- **Usage:**
  - Use clean and filtered threshold datasets.

## Sleep Latency Scripts

### 1. deleteCols.py

- **Purpose:** Simple script to delete unused variables in 30 second sleep stage datasets.
- **Usage:**
  - Use fitabase 30 second sleep stage datasets.

### 2. sleepLatency.py

- **Purpose:** Identify available sleep latency per day for each participant as well as the first wake time before light sleep and last wake time before light sleep as well.
- **Usage:**
  - Use 30 second sleep stage datasets (after runnning deleteCols.py).
 
### 3. sleepLatency(text).py

- **Purpose:** Optional tool to test sleep latency and visually see them in CLI.
- **Usage:**
  - Use fitabase 30 second sleep stage datasets (after runnning deleteCols.py).

 
  
## Additional Scripts (Optional)

### 1. FullMeanImputer.py

- **Purpose:** Impute missing values in each column with the overall mean of the participant.
- **Usage:**
  - Use clean dataset and if missing values are 0, adjust to warrant that.
 
### 2. adjust.py
- **Purpose:** Optional tool to adjust values in dataset so the earliest non-empty value is day 1.
- **Usage:**
  - Make sure empty values are empty cells (not 0) and use clean formatted dataset

### 3. remove50percent.py
- **Purpose:** Optional tool to remove participant columns that have less than half (35) days of viable data
- **Usage:**
  - Make sure empty values are empty cells (not 0) and use clean formatted dataset

 ### 4. removeLateJoiners.py
- **Purpose:** Optional tool to remove late joiners manually
- **Usage:**
  - Use clean datasets and manually input participant IDs considered late joiners

### 5. testKNNfinal.py
- **Purpose:** Optional tool to perform KNN imputation on datasets
- **Usage:**
  - Make sure empty values are empty cells (not 0) and use clean formatted dataset, manually decide how many neighbors and adjust that accordingly
  
