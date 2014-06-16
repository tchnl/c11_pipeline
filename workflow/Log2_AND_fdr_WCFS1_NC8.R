
###
# Tom Marieke Thierry
###

###############################
# Filteren bestand op FDR en log 2 ratio's 
###############################

# AANPASSEN DIRECTORIES
fname <- "C:/Users/Tom Linssen/Dropbox/Course 11/Weektaak 4/Zip bestand/LP_DEG_glc.txt"
DEG <- read.table(fname, header=TRUE)
#ratio <- DEG$WCFS1.glc.over.NC8.glc
#print(ratio)
newdata <- subset(DEG, WCFS1.glc.over.NC8.glc >= -1 )
newdata2 <- subset(newdata, WCFS1.glc.over.NC8.glc <= 1 )
newdata3 <- subset (newdata2, fdr.WCFS1.glc.over.NC8.glc <0.05)
#print(newdata3)

write.table (newdata3[1:3], "C:/Users/Tom Linssen/Dropbox/Course 11/Weektaak 4/Zip bestand/data.txt", sep = "\t", row.names = FALSE, col.name = TRUE)






