# script to automatically add new country-codes to the vnames file

library(dplyr)
vcodes_master <- read.csv("vcode-names.csv", header = F, stringsAsFactors = F)
vnames <- read.csv("vnames.csv", header = F, stringsAsFactors = F)

vc <- as.numeric(levels(as.factor(vcodes_master$V1)))
vn <- as.numeric(levels(as.factor(vnames$V1)))

new_vc <- vc[which(! vc %in% vn)]

v <- vcodes_master %>%
  filter(V1 %in% new_vc) %>%
  group_by(V1) %>%
  do(slice(., 1)) %>%
  data.frame

vnames <- rbind(vnames, v)
vnames$V1 <- as.numeric(vnames$V1)
vnames <- vnames[with(vnames, order(V1)), ]

write.table(vnames, file = "vnames.csv", row.names = F, col.names = F, sep = ",")
