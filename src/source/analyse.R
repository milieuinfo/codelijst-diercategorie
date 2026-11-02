#!/usr/bin/Rscript
# library(tidyr)
 library(dplyr)
# library(jsonlite)



setwd('/home/gehau/svn/rdf_tools/netkernel_bevraging/zendantennes_detail_sites')
df <- read.csv(file = 'results/antenne.csv', sep=",", na.strings=c("","NA")) %>% unique()






# 
# 
# 
# csv_0 = 'results/antenne_0.csv'
# csv_1 = 'results/antenne_1.csv'
# csv_2 = 'results/antenne_2.csv'
# csv_3 = 'results/antenne_3.csv'
# csv_4 = 'results/antenne_4.csv'
# csv_5 = 'results/antenne_5.csv'
# csv_6 = 'results/antenne_6.csv'
# csv_7 = 'results/antenne_7.csv'
# json_target_pad = 'results/antenne.json'
# csv_target_pad = 'results/antenne.csv'
# 
# 
# # read fragments
# df <- read.csv(file = csv_0, sep=",", na.strings=c("","NA")) %>% unique()
# df1 <- read.csv(file = csv_1, sep=",", na.strings=c("","NA")) %>% unique()
# df2 <- read.csv(file = csv_2, sep=",", na.strings=c("","NA")) %>% unique()
# df3 <- read.csv(file = csv_3, sep=",", na.strings=c("","NA")) %>% unique()
# df4 <- read.csv(file = csv_4, sep=",", na.strings=c("","NA")) %>% unique()
# df5 <- read.csv(file = csv_5, sep=",", na.strings=c("","NA")) %>% unique()
# df6 <- read.csv(file = csv_6, sep=",", na.strings=c("","NA")) %>% unique()
# df7 <- read.csv(file = csv_7, sep=",", na.strings=c("","NA")) %>% unique()
# 
# #merge fragments
# df <- merge(x = df, y = df1, by = "antenne", all.x = TRUE)
# df <- merge(x = df, y = df2, by = "antenne", all.x = TRUE)
# df <- merge(x = df, y = df3, by = "antenne", all.x = TRUE)
# df <- merge(x = df, y = df4, by = "antenne", all.x = TRUE)
# df <- merge(x = df, y = df5, by = "antenne", all.x = TRUE)
# df <- merge(x = df, y = df6, by = "antenne", all.x = TRUE)
# df <- merge(x = df, y = df7, by = "antenne", all.x = TRUE)
# df <- df[-1,]
# df <- df  %>% unique()
# 
# # write csv
# write.csv(df,csv_target_pad, row.names = FALSE, na='', fileEncoding='UTF-8')
# 
# # write json
# df_in_json <- toJSON(df, auto_unbox=TRUE)
# write(df_in_json, json_target_pad)





