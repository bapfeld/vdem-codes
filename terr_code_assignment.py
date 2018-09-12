#!/usr/local/bin/python3
# -*- mode: python -*-

# Script to assign country codes based on various possible country names
import os.path, re, argparse, sys
import pandas as pd

def terr_name_cleaner(df,
                      territory_column,
                      terr_clean_column):
    tc = territory_column
    tcc = terr_clean_column
    # begin cleaning
    df[tcc] = df[tc]
    df[tcc] = df[tcc].str.lower()
    df[tcc] = df[tcc].str.replace(',', '')
    df[tcc] = df[tcc].str.replace('’', '\'')
    df[tcc] = df[tcc].str.replace('&', 'and')
    df[tcc] = df[tcc].str.replace('á', 'a')
    df[tcc] = df[tcc].str.replace('é', 'e')
    df[tcc] = df[tcc].str.replace('è', 'e')
    df[tcc] = df[tcc].str.replace('í', 'i')
    df[tcc] = df[tcc].str.replace('ó', 'o')
    df[tcc] = df[tcc].str.replace('ú', 'u')
    df[tcc] = df[tcc].str.replace('ã', 'a')
    df[tcc] = df[tcc].str.replace('õ', 'o')
    df[tcc] = df[tcc].str.replace('ñ', 'n')
    df[tcc] = df[tcc].str.replace('ï', 'i')
    df[tcc] = df[tcc].str.replace('ö', 'o')
    df[tcc] = df[tcc].str.replace('ü', 'u')
    df[tcc] = df[tcc].str.replace('ô', 'o')
    df[tcc] = df[tcc].str.replace('ç', 'c')
    df[tcc] = df[tcc].str.replace('_', ' ')
    df[tcc] = df[tcc].str.replace(r'\s+', ' ')
    df[tcc] = df[tcc].str.replace(' is\.', 'island')
    df[tcc] = df[tcc].str.replace('islands', 'island')
    df[tcc] = df[tcc].str.replace('(?:^|\s)st\s', 'saint')
    df[tcc] = df[tcc].str.replace('(?:^|\s)st\.\s', 'saint')
    df[tcc] = df[tcc].str.replace('/ ', '/')
    df[tcc] = df[tcc].str.replace('rep\.', 'republic')
    df[tcc] = df[tcc].str.replace('rep ', 'republic')
    df[tcc] = df[tcc].str.replace('republica', 'republic')
    df[tcc] = df[tcc].str.replace('dem ', 'democratic')
    df[tcc] = df[tcc].str.replace('dem\.', 'democratic')
    df[tcc] = df[tcc].str.replace('afr\.', 'african')
    df[tcc] = df[tcc].str.replace('\s+', ' ')
    df[tcc] = df[tcc].str.strip()
    return df

def terr_code(df,
              terr_df,
              territory_column="country",
              territory_code_column="territory_id", 
              dry_run=None, 
              dry_run_file_out=None,
              custom_matches=None):
    if dry_run is True and dry_run_file_out is not None:
        drfo = os.path.expanduser(dry_run_file_out)
    elif dry_run is True and dry_run_file_out is None:
        print("Execution halted. dry-run=True but no dry-run-file-out has been specified.")
        return df
    tc = territory_column
    tcc = territory_code_column
    cc = "territory_name_cleaned_by_function"
    # identify the territory column in the df and run some checks
    if tc not in df.columns:
        print("Execution halted. The territory_column you specified was not found in this dataframe.")
        return df
    elif list(df.columns).count(tc) > 1:
        print("Execution halted. More than one column found with the specified territory_column.")
        return df
    if df[tc].isnull().sum() > 0:
        print("Warning: You have missing values in the given territory_column. Code will execute, but it is strongly encouraged that you discard the results, fix this problem, and rerun.")
    if custom_matches:
        if list(custom_matches) != ['name', 'code']:
            print("Execution halted. Custom matches dataframe incompatible with the terr_df.")
            return df
        check_set = set(terr_df['name']) - set(custom_matches['name'])
        if check_set:
            print("Execution halted. The following names are duplicated in the custom_matches.")
            print(*check_set, sep="\n")
        else:
            terr_df = terr_df.append(custom_matches, ignore_index=True)
    # need to run the territory name cleaner here
    df = terr_name_cleaner(df, tc, cc)
    if dry_run is True:
        tdf = df.groupby(tc).head(1)
        tdf = tdf[tdf[tc].notnull()]
        tdf = tdf[[tc, cc]]
        test_df = tdf.merge(terr_df, left_on=cc, right_on='name_foobarbaz', how='left')
        test_df['code_foobarbaz'] = test_df['code_foobarbaz'].astype(object)
        test_df = test_df.rename(index=str, columns={'code_foobarbaz': tcc, 'super_foobarbaz': 'super_code'})
        test_df = test_df.drop(['name_foobarbaz'], axis=1)
        test_df = test_df.sort_values(by=['code', tc])
        test_f_type = os.path.splitext(drfo)[1]
        try:
            if t_f_type == ".xlsx":
                test_df.to_excel(drfo, index=False)
            elif t_f_type == ".csv":
                test_df.to_csv(drfo, index=False)
            else:
                sys.exit("Error: input file is not xlsx or csv")
        except FileNotFoundError:
            sys.exit("Error: unable to write to the specified test-run-file-out.")
    else:
        # make sure country names exist in csv list and assign codes if they do
        missing_set = set(df[df[tc].notnull()][cc]) - set(terr_df['name_foobarbaz'])
        if not missing_set:
            df = df.merge(terr_df, left_on=cc, right_on='name_foobarbaz', how='left')
            df = df.rename(index=str, columns={'code_foobarbaz': tcc})
            df[tcc] = df[tcc].astype(object)
            df = df.drop(columns=[cc, 'name_foobarbaz', 'super_foobarbaz'])
            return df
        else:
            print("Execution halted. The following countries were not found in the master country file: ")
            print(*missing_set, sep="\n")
            return df
        
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
### Define args, main, and run
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
def initialize_params(args_parser):
    args_parser.add_argument(
        '--file-path',
        help='Path to the file to add new codes to',
        required=True
    )
    args_parser.add_argument(
        '--territory-column',
        help='Name of the column that contains territory names to be coded',
        required=True
    )
    args_parser.add_argument(
        '--territory-code-file',
        help='Path to the territory codes file',
        required=True
    )
    args_parser.add_argument(
        '--territory-id-column',
        help='Name of the new column to create with the ids. Default is "territory_id"',
        default='territory_id', 
        required=False
    )
    args_parser.add_argument(
        '--custom-matches',
        help='Path to a file containing custom matches. Should be a csv with two columns: "name" and "code".',
        required=False
    )
    args_parser.add_argument(
        '--dry-run',
        help='Boolean indicating if this is a dry run. Default is true.',
        default=True, 
        required=True
    )
    args_parser.add_argument(
        '--dry-run-out',
        help='If doing a dry run, path to where the test match file should be written. Must specify an excel file extension.',
        required=False
    )
    return args_parser.parse_args()

def main():
    df_path = os.path.expanduser(p.file_path)
    t_path = os.path.expanduser(p.territory_code_file)
    df_f_type = os.path.splitext(df_path)[1]
    t_f_type = os.path.splitext(t_path)[1]
    tdf_code_col = 'code_foobarbaz'
    tdf_name_col = 'name_foobarbaz'
    tdf_super_col = 'super_foobarbaz'
    try:
        if df_f_type == ".xlsx":
            df = pd.read_excel(df_path)
        elif df_f_type == ".csv":
            df = pd.read_csv(df_path)
        else:
            sys.exit("Error: input file is not xlsx or csv.")
    except:
        sys.exit("Error: unable to open specified file path")
    try:
        if t_f_type == ".xlsx":
            terr_df = pd.read_excel(t_path)
        elif t_f_type == ".csv":
            terr_df = pd.read_csv(t_path)
        else:
            sys.exit("Error: input file is not xlsx or csv")
    except FileNotFoundError:
        sys.exit("Error: unable to open specified territory code file.")
    terr_df = terr_df.rename(index=str,
                             columns={'code': tdf_code_col,
                                      'name': tdf_name_col,
                                      'super_code': tdf_super_col})
    if p.territory_id_column:
        territory_id_new = p.territory_id_column
    else:
        territory_id_new = "territory_id"
    if p.dry_run_out:
        dry_run_file_out = p.dry_run_out
    else:
        dry_run_file_out = None
    if p.custom_matches:
        custom_matches = p.custom_matches
    else:
        custom_matches = None
    if p.dry_run == 'True':
        dry_run = True
    else:
        dry_run = False
    out_df = terr_code(df=df, terr_df=terr_df, 
          territory_column=p.territory_column,
          territory_code_column=territory_id_new,
          dry_run=dry_run,
          dry_run_file_out=dry_run_file_out,
          custom_matches=custom_matches)
    if not dry_run:
        if df_f_type == ".xlsx":
            out_df.to_excel(df_path, index=False)
        elif df_f_type == ".csv":
            out_df.to_csv(df_path, index=False)

args_parser = argparse.ArgumentParser()
p = initialize_params(args_parser)

if __name__ == "__main__":
    main()
