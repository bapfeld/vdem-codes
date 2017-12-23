# Script to assign country codes based on various possible country names
import csv

def vcode(df,
          country_column="Country",
          vcode_csv_path="/Users/bapfeld/Documents/UT/V-Dem/vdem-codes/vcode-names.csv"):
    cnames = {}
    with open(vcode_csv_path) as codefile:
        reader = csv.reader(codefile)
        for row in reader:
            cnames[row[1]] = row[0]
    # identify the country column in the df and run some checks
    if country_column in df.columns:
        if list(df.columns).count(country_column) > 1:
            print("Execution halted. More than one column found with the specified country_column.")
            return df
    else:
        print("Execution halted. The country_column you specified was not found in this dataframe.")
        return df
    if df[country_column].isnull().sum() > 0:
        print("Execution halted. You have missing values in the country column.")
        return df
    # make sure country names exist in csv list and assign codes if they do
    if all(c in cnames for c in set(df[country_column])):
        df['country_id'] = df[country_column].map(cnames)
        df['country_id'] = df['country_id'].astype(str).astype(int)
        return df
    else:
        bad = set(df[country_column]) - cnames.keys()
        print("Execution halted. The following countries were not found in the master country file: ")
        print(bad)
        return df
        
