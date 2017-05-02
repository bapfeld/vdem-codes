.PHONY: all

stata_do: vcode_in_stata.R convert_csv_to_stata.R vcode-names.csv
	R CMD BATCH convert_csv_to_stata.R
