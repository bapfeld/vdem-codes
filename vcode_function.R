# script to assign country codes based on various possible country names


vcode <- function(df, country_column = "Country", vcode_csv_path = "vdem-codes/vcode-names.csv"){
  cnamefoo <- rio::import(vcode_csv_path)
  master_country_list <- cnamefoo$V2
  c_column <- grep(country_column, names(df))
  if(length(c_column) == 0){
    warning("Execution halted. The country_column you specified was not found in this dataframe.")
    return(df)
    }else if(length(c_column) > 1){
      warning("Execution halted. More than one column found with the specified country_column.")
      return(df)
    }else{
      df_country <- df[[c_column]]
      df_country <- as.character(df_country)
      # check that the countries are actually in our master list
      country_check <- df_country %in% master_country_list
      if(sum(country_check) == length(country_check)){
        vc <- lapply(df_country, function(x) match(x, master_country_list))
        vc <- unlist(vc)
        df$country_id <- cnamefoo$V1[vc]
        df <- as.data.frame(df)
        return(df)
      }else{
        boo <- df_country[which(country_check == F)]
        boo <- boo[!duplicated(boo)]
        warning("Execution halted. The following countries were not found in the master country file: ")
        warning(cat(boo, sep = ", "))
        return(df)
      }
    }
}