
# 5 Methods of building a model

 - All-n
 - Backward Elimination
 - Formward Selections
 - Bidirectional Elimination
 - Score comparision


## All in

Use all indipendent variables (Predictors) and create a model

## Backward Elimination

Step-1: Select a significance level for your model (eg: SL = 0.05 (5%))

Step-2: Createa a model with all the varibles

Step-3: Consider the predictor with the highest P-value, and ```if``` its greater than significance ```,``` goto step4 ```else``` goto FIN

Step-4: Remove the variable

Step-5: create a model without this variable, repeat step-3

## Forward Selection

Step-1: Select a significance level to enter the model

Step-2: Fit all simple regression models y ~ x<sub>n</sub>, Select one with the lowest P-value

Step-3: Kepp this variable and fit all possible models with one extra predictor added to the one(s) you already have

Step-4: Consider predictor with the lowest P-value, ```if``` P < SL ```,``` goto  step-3 ```else``` goto FIN

FIN: Keep the previous model

