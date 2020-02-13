
	a.	Fit a classification tree using all predictors using CART analysis. Display the leaf report, and interpret the outcomes in the leaf report in terms of rules. Report the accuracy and the confidence interval. 
	b.	Is this model practical for predicting the quality of a new wine? Why or why not? 
	c.	Fit another classification tree by modifying the predictors that can be used to predict the outcome of a new wine. Describe the resulting tree, and compare the new tree to the previous one built in (a). 


wine<-read.csv("/Users/kris/Documents/whitewines.csv")
str(wine)

# Partition data into training and testing data sets (70/30)
library(caret)
set.seed(123)
winePart <- createDataPartition(y=wine$quality, p=0.7, list=FALSE)
train <- wine[winePart, ]
test<- wine[-winePart, ]



# Find the best classification tree: C5.0, tree, or party.

# Create model w/ train data set.
library(C50)
class(train$quality) # integer
train$quality <- as.factor(train$quality)
# Remove target variable 
c5Mod<-C5.0(train[-12], train$quality)
#plot(c5Mod)
#text(c5Mod)


Evaluate C5.0 Model using Predict Function:
c5Predict <-predict(c5Mod, test)
library(gmodels)

CrossTable(test$quality, c5Predict, prop.chisq=FALSE, dnn=c('Actual Quality', 'Predicited Quality'))
# Prediction for 3: 0 correctly predicted out of 1 
# Prediction for 4: 11 correctly predicted out of 48
# Prediction for 5: 250 correctly predicted out of 429
# Prediction for 6: 403 correctly predicted out of 671
# Prediction for 7: 143 correctly predicted out of 283
# Prediction for 8: 19 correctly predicted out of 37
# After reviewing the cross table, this does not seem to be an appropriate model for this example due to the number of quality options. Row totals and column totals do not accuratly tell us the number of actual values. 


# SAME DATA, new decision tree: tree package.  
library(tree)
WineTreeMod<-tree(quality~., data=train)
plot(WineTreeMod)
text(WineTreeMod)
# Outout does not show a reason  to prune as it does not have a large amount of trees, but for the sake of the function, we will see what the determined best split is. 
# Prune
Wine.cv.tree<-cv.tree(WineTreeMod, FUN=prune.misclass)
plot(Wine.cv.tree)
# Due to the output, I will choose best split at 3.
prune.Winetrees <- prune.misclass(WineTreeMod, best=3)


plot(prune.Winetrees)
text(prune.Winetrees, pretty=0)

# Looks like the predictor variables for 'quality' are: alcohol, and volatile.acidity.

# Predict and Evaluate
library(e1071)
WineTreePred<-predict(prune.Winetrees, test, type="class")

#Use the prediction and actual results to compare

test$quality <- as.factor(test$quality)
confusionMatrix(WineTreePred, test$quality)
# Results show 51.26 percent accuracy of the model, with many incorrect predictions. Model mostly correctly predicted quality scores of 5 and 6. 

# SAME DATA, new decision tree: rpart package.

library(rpart)
rpartMod<-rpart(quality~., data= train, method= "class")
plot(rpartMod)
text(rpartMod) #RUN BOTH TOGETHER

###Best split at 2, determined by looking at lowest xerror
printcp(rpartMod)

ptree<-prune(rpartMod, cp= rpartMod$cptable[which.min(rpartMod$cptable[,"xerror"]),"CP"])
plot(ptree)
text(ptree) # RUN BOTH TO SEE OUR BEST TREE.
# Same output. 

# Prediction and Evaluate
rpartPred<-predict(ptree, test, type="class")
# Review our prediction, compared to actual 
confusionMatrix(rpartPred, test$quality)
# 50.99 percent accuracy. Not a technique due to number of quality classifications available.







# Modify predictors:
newWinedf<-read.csv("/Users/kris/Documents/whitewines.csv")
str(wine)
table(newWinedf$quality) # 1640 High Q, and 3258 Low Q.
newWinedf$quality <- ifelse(newWinedf$quality==""| newWinedf$quality=="8"|newWinedf$quality=="9", "High Q", "Low Q")
newWinedf$quality<- as.factor(newWinedf$quality)

str(newWinedf)

# Partition data into training and testing data sets (70/30)
library(caret)
set.seed(123)
winePart2 <- createDataPartition(y=newWinedf$quality, p=0.7, list=FALSE)
train2 <- newWinedf[winePart2, ]
test2 <- newWinedf[-winePart2, ]

# Use new model with C50 package.


library(C50)
class(train2$quality) # integer
train2$quality <- as.factor(train2$quality)
# Remove target variable 
str(train2)
c5Mod2<-C5.0(train2[-12], train2$quality)
#plot(c5Mod2)
#text(c5Mod2)


#Evaluate C5.0 Model using Predict Function:
c5Predict <-predict(c5Mod2, test2)
library(gmodels)

CrossTable(test2$quality, c5Predict, prop.chisq=FALSE, dnn=c('Actual Quality', 'Predicited Quality'))

# After dividing quality into smaller partitions, the model accuratly predicted 1413 of 1469 or 96.2 percent.
