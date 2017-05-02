# Code to make a stata do file version of the vcode function

# import data
vcodes <- read.csv("vcode-names.csv", header = F, stringsAsFactors = F)

# get function
source("vcode_in_stata.R")

# Run the function
vcode_in_stata(vcodes)
