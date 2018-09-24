library(jsonlite)
library(dplyr)

if (file.exists("dict.json")) {
  dat <- fromJSON("dict.json")  
} else {
  url <- "https://liao961120.github.io/PTT-scrapy/dict.json"
  download.file(url, "dict.json")
  dat <- fromJSON("dict.json")  
}




# Simplify data structure ----
idx <- which(colnames(dat) %in% c("title", "url", "date"))
dat[, idx] <- vapply(dat[, idx], unlist, rep("", nrow(dat)))

# Extract title
title <- as.data.frame(cbind(dat$title, "title"),
                       stringsAsFactors = F)
colnames(title) <- c('term', 'source')

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
dict <- lst %>%
  bind_rows(title) %>%
  distinct(term, .keep_all = T) %>% 
  arrange(desc(term), nchar(term), source)

saveRDS(dict, "dict.rds")
readr::write_csv(dict, "dict.csv")
