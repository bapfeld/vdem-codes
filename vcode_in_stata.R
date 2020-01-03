vcode_in_stata <- function(vcode_csv){
  sink("vcode-function.do")
  cat("gen vcode = .")
  cat("\n")
  for (i in 1:nrow(vcode_csv)){
    cat(paste0("replace vcode = ", vcode_csv$V1[i], " if country == ", "\"", vcode_csv$V2[i], "\""))
    cat("\n")
  }
  sink()
}

vcode_to_country_in_stata <- function(vcode_csv, country_var_name){
  new_var <- paste0("gen ", country_var_name, " = .")
  new_replace <- paste0("replace ", country_var_name, " = ")
  sink("vcode_to_country.do")
  cat(new_var)
  cat("\n")
  for (i in seq_along(vcode_csv[[1]])){
    cat(paste0(new_replace, "\"", vcode_csv$V2[i], "\"", " if country_id == ", vcode_csv$V1[i]))
    cat("\n")
  }
  sink()
}
