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
