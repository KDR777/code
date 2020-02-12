The goal is to use these data to build a model that will classify auction as competitive or non-competitive. A competitive auction is defined as an auction with at least two bids placed on the time auctioned. The data include variables that describe the item (auction category), the seller (his/her eBay rating), and the auction terms that the seller selected (auction duration, opening price, currency, day-of-week of auction close). The price at which the auction closed is also included.
Your task is to predict whether or not the auction will be competitive.

# Import and Review data.
eBay<- read.csv("/Users/kris/Documents/eBay.csv")

# Snapshot of data. 
str(eBay) # 1972 obs, 8 vars.



# Convert variable 'Duration' to a factor:
eBay$Duration <- as.factor(eBay$Duration)
#str(eBay) # Verify it converted to a factor.


# Predictor Variable; Competitive.


# Partition data into training and testing data sets (70/30)
library(caret)
set.seed(123)
eBayPart <- createDataPartition(y=eBay$Competitive, p=0.7, list=FALSE)
train <- eBay[eBayPart, ]
test<- eBay[-eBayPart, ]


# Find the best classification tree: C5.0, tree, or party.

## C5.0 Decision Tree Results: 521 correct predictions for Competitive (88.12 percent accurate), 70 error rate (11.84 percent error) when calculating Competitiveness. 

# Create model w/ train data set.
library(C50)
class(train$Competitive) # character
train$Competitive <- as.factor(train$Competitive)
# Remove target variable 
c5Mod<-C5.0(train[-8], train$Competitive)
plot(c5Mod)
text(c5Mod)


Evaluate C5.0 Model using Predict Function:
c5Predict <-predict(c5Mod, test)
library(gmodels)

CrossTable(test$Competitive, c5Predict, prop.chisq=FALSE, dnn=c('Actual Competitiveness', 'Predicited Competitiveness'))



## Pruning with Tree Package Results: 87.14 accuracy.  515 predicted Competitiveness correctly, 76 incorrectly predicted. I chose 14 as the 'best' fit due to the plot which showed lower misclassificaton around that level. 


library(tree)
eBayTreeMod<-tree(Competitive~., data=train)
plot(eBayTreeMod)
text(eBayTreeMod)

# Prune
eBay.cv.tree<-cv.tree(eBayTreeMod, FUN=prune.misclass)
plot(eBay.cv.tree)


prune.eBaytrees <- prune.misclass(eBayTreeMod, best=14)

plot(prune.eBaytrees)
text(prune.eBaytrees, pretty=0)


# Looks like predictor variables for competitivenes are: 'OpenPrice, ClosePrice, currency, and sellerRating'

# Predict and Evaluate
library(e1071)
eBayTreePred<-predict(prune.eBaytrees, test, type="class")

#Use the prediction and actual results to compare

test$Competitive <- as.factor(test$Competitive)
confusionMatrix(eBayTreePred, test$Competitive)













