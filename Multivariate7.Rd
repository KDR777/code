stock <- read.csv("http://tiny.cc/isqs6350_stockReturn")
mydata<-stock*100
head(mydata)
#A) Perform confirmatory factor analysis based on two factors: manufacturing and service. 
efa <- factanal(mydata, 2)

print(efa$loadings, cut = 0.5)
# We go with 2 factors: manufacturing and service. 

#For CFA, we first need a model
library(sem)

stock_model <-specifyModel(file ="stock_model.txt")

stock_sem <- sem(stock_model, cor(mydata), nrow(mydata))

summary(stock_sem) # pvalue = 7.097049e-20, thus we reject the null hypothesis. Not enough evidence to say the two matrices are equal. The data does not support our model. 

#B) Report the path diagram that shows coefficient estimates. 
library(semPlot)
semPaths(stock_sem, "est")

#C) Report SRMR, GFI and AGFI. What do you conclude? Is the model you made in part a approved? Two out of the three returned as false, and the null hypothesis was rejected, meaning the two models are not equal. 
options(fit.indices = c("GFI", "AGFI", "SRMR")) #some fit indices
criteria = summary(stock_sem)
criteria$SRMR
criteria$GFI
criteria$AGFI

criteria$SRMR < 0.05 #FALSE
criteria$GFI > 0.95 #TRUE
criteria$AGFI > 0.95 #FALSE, but close at 0.942




#D) Find the 95% confidence interval for the correlation between the two factors: manufacturing and service returns. Confidence interval is between 0.315 and 0.489.
parameters = summary(stock_sem)
parameters$coeff

#Lets focus on Rho, the correlation between factors.
parameters$coeff[8,]$Estimate # Rho

conf.L = parameters$coeff[8,]$Estimate - 1.96 * parameters$coeff[8,]$'Std Error' # 95% confidence intervalfor lower bound

conf.U = parameters$coeff[8,]$Estimate + 1.96 * parameters$coeff[8,]$'Std Error' # 95% confidence interval for upper bound.

conf.L
conf.U