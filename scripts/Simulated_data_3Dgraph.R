# Author: Sidra Sohail
library(vegan)
library(plotly)
library(dplyr)
datatab <- data.frame(rnorm(100,1,1),rnorm(100,1,1),rnorm(100,1,1))
datatab$type <- c(rep("M",14),rep("F",30),rep("MF",56))
colnames(datatab) <- c("column1","column2","column3","type")
# pco1,pco2,pco3 would be extracted from the eigenvalues after running pcoa on a distance matrix
pco2 <- paste("PCo2",paste(paste("( ",threepercents[2],sep=''),'%',sep=''),sep = ' ', " )")
pco1 <- paste("PCo1",paste(paste("( ",threepercents[1],sep=''),'%',sep=''),sep = ' ', " )")
pco3 <- paste("PCo3",paste(paste("( ",threepercents[3],sep=''),'%',sep=''),sep = ' ', " )")
symbolslist <- c('circle','circle-open','square','square-open','diamond','diamond-open','cross')
fig <- plot_ly(datatab, x = ~column1, y = ~column2, z = ~column3, symbol = datatab[,ncol(datatab)],symbols = symbolslist, text = ~paste('Sample: ', rownames(datatab)))%>%
     add_markers(type="scatter")%>%
     layout(scene = list(xaxis = list(title = pco1),
                         yaxis = list(title = pco2),
                         zaxis = list(title = pco3)))
 
fig
