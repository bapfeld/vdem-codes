# function to take vcodes and assign a country name

country_from_vcode <- function(df, country_id_column = "country_id", vnames_path = "vdem-codes/vnames.csv"){
  vnames <- read.csv(vnames_path, header = F, stringsAsFactors = F)
  id_column <- match(country_id_column, names(df))
  if(is.na(id_column)){
    stop("Execution halted. The country_id_column you specified was not found in this dataframe.")
  }else if(length(id_column) > 1){
    stop("Execution halted. More than one column found with the specified country_id_column.")
  }else{
    if(is(tryCatch(as.numeric(df[[id_column]]),
                   warning = function(w) w),
          "warning")){
      stop("Execution halted. country_id_column cannot be converted to numeric.")
    }else{
      df[[id_column]] <- as.numeric(df[[id_column]])
      if((sum(is.na(df[[id_column]])) > 0) | (sum(df[[id_column]] == "") > 0)){
        stop("Execution halted. NA or blank country names detected.")
      }
      id_check <- df[[id_column]] %in% vnames$V1
    if(sum(id_check) == length(id_check)){
      df$vdem_country_name <- vnames$V2[match(df[[id_column]], vnames$V1)]
      # is it possible to take a variable in the function call to determine what to call the new variable?
      return(df)
      }else{
        bad_codes <- df[[id_column]][which(id_check == F)]
        bad_codes <- bad_codes[!duplicated(bad_codes)]
        stop(paste0("Execution halted. The following country codes were not found in the master country file: ", paste(bad_codes, collapse = ", ")))
      }
    } 
  }
}
