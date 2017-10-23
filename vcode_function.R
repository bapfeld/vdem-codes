# script to assign country codes based on various possible country names


vcode <- function(df, country_column = "Country", vcode_csv_path = "vdem-codes/vcode-names.csv"){
  cnamefoo <- read.csv(vcode_csv_path, header = F, stringsAsFactors = F)
  master_country_list <- cnamefoo$V2
  country_column <- paste0(country_column, "$")
  c_column <- grep(country_column, names(df))
  if(length(c_column) == 0){
    warning("Execution halted. The country_column you specified was not found in this dataframe.")
    return(df)
    }else if(length(c_column) > 1){
      warning("Execution halted. More than one column found with the specified country_column.")
      return(df)
    }else{
      df[[c_column]] <- as.character(df[[c_column]])
      # check that the countries are actually in our master list
      country_check <- df[[c_column]] %in% master_country_list
      if(sum(country_check) == length(country_check)){
        df$country_id <- cnamefoo$V1[match(df[[c_column]], master_country_list)]
        df <- as.data.frame(df)
        return(df)
      }else{
        boo <- df[[c_column]][which(country_check == F)]
        boo <- boo[!duplicated(boo)]
        warning("Execution halted. The following countries were not found in the master country file: ")
        warning(cat(boo, sep = ", "))
        return(df)
      }
    }
}
