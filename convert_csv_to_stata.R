# Code to make a stata do file version of the vcode function

# import data
vcodes <- read.csv("vcode-names.csv", header = F, stringsAsFactors = F)
vcodes_simple <- read.csv("vnames.csv", header = F, stringsAsFactors = F)

# get function
source("vcode_in_stata.R")

# Run the functions
vcode_in_stata(vcodes)
vcode_to_country_in_stata(vcodes_simple, "vdem_country_name")
