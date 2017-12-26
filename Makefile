.PHONY: all clean_csv clean

stata_do: vcode_in_stata.R convert_csv_to_stata.R vcode-names.csv
	R CMD BATCH convert_csv_to_stata.R
clean_csv: sort_csv.R vcode-names.csv
	R CMD BATCH sort_csv.R

clean:
	rm *.Rout
