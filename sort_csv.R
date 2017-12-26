# Keep the master csv sorted alphanumerically
country_csv <- read.csv("vcode-names.csv", header = F, stringsAsFactors = F)
country_csv <- country_csv[with(country_csv, order(V1, V2)), ]
write.table(country_csv, file = "vcode-names.csv", sep = ",", row.names = F, col.names = F)
