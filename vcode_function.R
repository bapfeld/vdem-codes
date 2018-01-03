# script to assign country codes based on various possible country names


vcode <- function(df, country_column = "Country", vcode_csv_path = "vdem-codes/vcode-names.csv"){
  cnamefoo <- read.csv(vcode_csv_path, header = F, stringsAsFactors = F)
  master_country_list <- cnamefoo$V2
  c_column <- match(country_column, names(df))
  if(is.na(c_column)){
    stop("Execution halted. The country_column you specified was not found in this dataframe.")
  }else if(length(c_column) > 1){
    stop("Execution halted. More than one column found with the specified country_column.") 
  }else{
    df[[c_column]] <- as.character(df[[c_column]])
    # check for NA or "" country names
    if((sum(is.na(df[[c_column]])) > 0) | (sum(df[[c_column]] == "") > 0)){
      stop("Execution halted. NA or blank country names detected.") 
    }
    # check that the countries are actually in our master list
    country_check <- df[[c_column]] %in% master_country_list
    if(sum(country_check) == length(country_check)){
      df$country_id <- cnamefoo$V1[match(df[[c_column]], master_country_list)]
      df <- as.data.frame(df)
      return(df)
    }else{
      boo <- df[[c_column]][which(country_check == F)]
      boo <- boo[!duplicated(boo)] 
      stop(paste0("Execution halted. The following countries were not found in the master country file:\n", paste(boo, collapse = "\n")))
    }
  }
}
