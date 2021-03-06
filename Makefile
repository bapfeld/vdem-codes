.PHONY: all clean_csv clean names_csv_update

all: stata_do clean_csv names_csv_update

stata_do: vcode_in_stata.R convert_csv_to_stata.R vcode-names.csv
	R CMD BATCH --no-save --no-restore convert_csv_to_stata.R
clean_csv: sort_csv.R vcode-names.csv
	R CMD BATCH --no-save --no-restore sort_csv.R
names_csv_update: update_vnames_csv.R vcode-names.csv
	R CMD BATCH --no-save --no-restore update_vnames_csv.R

clean:
	rm *.Rout
