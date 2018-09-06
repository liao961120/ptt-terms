library(jsonlite)
library(dplyr)

dat <- fromJSON("dict.json")
 
# Simplify data structure ----
idx <- which(colnames(dat) %in% c("title", "url", "date"))
dat[, idx] <- vapply(dat[, idx], unlist, rep("", nrow(dat)))

# Extract terms from list columns in 'dat' ----
lst <- vector("list", 3L)
k <- 1
for (i in c("bold", "bracket", "link_new")) {
  lst[[k]] <- data.frame(term = unlist(dat[[i]]),
                         source = i,
                         stringsAsFactors = F)
  k <- k + 1
}
lst <- bind_rows(lst)

# Construct dictionary ----
dict <- filter(lst, nchar(term) <= 15) %>%
  distinct(term, .keep_all = T)
