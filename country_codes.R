# script for dealing with country codes

library(tidyverse)

# current_codes <- rio::import("Data/Country_Codes/Countries_long_newcodes.xlsx")
# current_codes_long <- rio::import("Data/Country_Codes/country_table.csv")
# codes <- full_join(current_codes_long, current_codes, by = c("country_id", "name")) %>%
#   select(country_id, name)

load("Data/Country_Codes/codes.Rdata")

# Time to create some new variables
new_codes <- data.frame(country_id = c(401:414), name = c("Anguilla", "Aruba", "Bermuda", "Cayman Islands", "French Guiana", "French Polynesia", "Greenland", "Guadeloupe", "Guam", "Netherlands Antilles", "New Caledonia", "Puerto Rico", "Reunion", "Virgin Islands - US"))
codes <- rbind(codes, new_codes)
codes <- codes[!duplicated(codes),]
rm(new_codes)

save(codes, file = "Data/Country_Codes/codes.Rdata")
