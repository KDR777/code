# KDR
# Simulization & optimization problems:


# The Whitt Window Company, a company with only three employees, makes two 
# different types of hand-crafted windowns: a wood-framed and an aluminum framed window.
# The comapny earms $300 profit for each wood-framed window and $180 profit for each 
# aluminum-framed window. 

# Doug makes the wood frame and can make 6 per day.
# Linda makes the aluminum frames and can make 5 per day.
# Bod forms and cuts the glass and can make 48 square feet of glass per day.

# Each wood-framed window uses 6 square feet of glass and 
# each aluminum-framed window uses 8 square feet of glass. 

# The company wishes to determine how many windows of each type to produce per day
# to maximize total profit. 


# Formulate a linear programming model for the problem above:

# Max: Z = 300x1 +180x2  (profit for wood-framed and aluminum-framed)
# 6x1 <= 6  wood-frames per day
# 8x2 <= 5 aluminum-frames oer day
# 6x1 + 8x2 <= 48 ft glass per day
# x1 AND x2 >= 0


# Solve the problem:


from pulp import * 
# Define the Model
prob = LpProblem("Whitt Window Company", LpMaximize) 
x1 = LpVariable('x1', lowBound = 0) 
x2 = LpVariable('x2', lowBound = 0) 
# Objective function 
prob += 300*x1 + 180*x2, "Obj" 
# Constraints 
prob += x1 <= 6
prob += x2 <= 5 
prob += 6*x1 + 8*x2 <=48
print(prob)

prob.solve() 
print("status: " + LpStatus[prob.status]) 

for variable in prob.variables():
     print("{}* = {}".format(variable.name, variable.varValue)) 
     
print(value(prob.objective))

# Shadow pricing for constrains above:
for name, c in prob.constraints.items():
    print("\n", name, ":", c , ", Slack =" ,c.slack, ", Shadow Price= ", c.pi)
 
# Output shows we should produce 6 wood-frames and 1.5 (practically 1) aluminum-frame.
# If we produced 6 wfs and 1 afs, that would equal 44 square feet of glass.
# Profit = $2070 according to the output, but in reality, we would likely not make 0.5 of a product, 
# thus profit would actually = $1980.00   
    
# 
# The above output shows:
# Constraint 1 is binding b/c it has a slack of 0. 
# Constraint 2 has a shadow price of 0, meaning it is non-binding
# Constraint 3 is binding b/c it has a slack of 0.
    
    
# Constraint 1 has a Shadow Price of 165.0
# Meaning, if we can increase the amount of wood-frames produced by 1 unit,
# we can increase profit by $165 
    
# Constraint 3 also has a shadow price, which is equal to 22.5, meaning if we
# could increase production of the glass we are able to make by 1 unit per day,
# we could then increase profits by $22.5.
    
  
# 
# How would the optimal solution (the number of windows of each type) change (is at all)
# if the profit per wood-framed window decreases from $300 to $200?
from pulp import * 
# Define the Model
prob = LpProblem("Whitt Window Company", LpMaximize) 
x1 = LpVariable('x1', lowBound = 0) 
x2 = LpVariable('x2', lowBound = 0) 
# Objective function 
prob += 200*x1 + 180*x2, "Obj" 
# Constraints 
prob += x1 <= 6
prob += x2 <= 5 
prob += 6*x1 + 8*x2 <=48
print(prob)

prob.solve() 
print("status: " + LpStatus[prob.status]) 

for variable in prob.variables():
     print("{}* = {}".format(variable.name, variable.varValue)) 
     
print(value(prob.objective))


# Shadow pricing for constrains above:
for name, c in prob.constraints.items():
    print("\n", name, ":", c , ", Slack =" ,c.slack, ", Shadow Price= ", c.pi)

# According to the output, after decreasing profit for wooden-frames from $300 to $200, 
# the optimal solution would remain the same; procude 6 wood-frames and 1.5 aluminum-frames. 
# Practically, we would produce 1 aluminum frame and not 1.5 of a product. 
# This would decrease profit to 1470, but realistically to 1380 (since again, we are not
# producing half of a product.)
  
    
#  
# How would the optimal solution (number of windows of each type) change if Doug makes only
# 5 wooden frames per day?
    
from pulp import * 
# Define the Model
prob = LpProblem("Whitt Window Company", LpMaximize) 
x1 = LpVariable('x1', lowBound = 0) 
x2 = LpVariable('x2', lowBound = 0) 
# Objective function 
prob += 300*x1 + 180*x2, "Obj" 
# Constraints 
prob += x1 <= 5
prob += x2 <= 5 
prob += 6*x1 + 8*x2 <=48
print(prob)

prob.solve() 
print("status: " + LpStatus[prob.status]) 

for variable in prob.variables():
     print("{}* = {}".format(variable.name, variable.varValue)) 
     
print(value(prob.objective))


# Shadow pricing for constrains above:
for name, c in prob.constraints.items():
    print("\n", name, ":", c , ", Slack =" ,c.slack, ", Shadow Price= ", c.pi)
    
# The output shows a new optimal solution, and we should now produce 5 wooden-frames
# and 2.25 aluminum-frames (realistically, 2 aluminum frames.) if Doug cuts his production 
# of wooden-frames from 6 to 5 per day. 
# This change would decrease profits to $1905.00 per day (but realistically $1860.00, since
# we will only produce 2 aluminum-frames and not 2.25)
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Implement the following LP Minimization model:
    
# Min 
#Z = 3x_1 + 3x_2 + 5x_3
    
# St. 
# 2x_1 +       x_3 >= 8
#        x_2 + x_3 >= 6
# 6x_1 + 8x_2      >= 48
#  x_1, x_2, x_3 >= 0

from pulp import *
# Define the Model
prob = LpProblem("LP Minimization model", LpMinimize)
x1 = LpVariable('x_1', lowBound = 0)
x2 = LpVariable('x_2', lowBound = 0)
x3 = LpVariable('x_3', lowBound = 0)
# Objective function
prob += 3*x1 + 3*x2 + 5*x3, "Obj"
# Constraints:
prob += 2*x1 + x3 >= 8
prob += x2 + x3 >= 6
prob += 6*x1 + 8*x2 >= 48

print(prob)

prob.solve()
print("status: " + LpStatus[prob.status])

for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))
    
print(value(prob.objective))

# We add these lines for sensitivity analysis
print("\n Sensitivity Analysis: ")

for name, c in prob.constraints.items():
    print("\n", name, ":", c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

for v in prob.variables():
  print ("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)

# Problem 2 a) 
# The optimal solution: we should produce 4 of x1, 6 of x2, and 0 of x3, for an objective value of 30. 

# 
# Lets look at x_3: If we reduce x_3 by 0.05:
# prob += 3*x1 + 3*x2 + (5 - 0.05)*x3, "Obj"
# Then the reduced cost would turn to 0, and we'd have a value for x_3
# Let's demonstrate:

from pulp import *
# Define the Model
prob = LpProblem("LP Minimization model", LpMinimize)
x1 = LpVariable('x_1', lowBound = 0)
x2 = LpVariable('x_2', lowBound = 0)
x3 = LpVariable('x_3', lowBound = 0)
# Objective function
prob += 3*x1 + 3*x2 + (5-0.5)*x3, "Obj"
# Constraints:
prob += 2*x1 + x3 >= 8
prob += x2 + x3 >= 6
prob += 6*x1 + 8*x2 >= 48

print(prob)

prob.solve()
print("status: " + LpStatus[prob.status])

for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))
    
print(value(prob.objective))

# We add these lines for sensitivity analysis
print("\n Sensitivity Analysis: ")

for name, c in prob.constraints.items():
    print("\n", name, ":", c, ", Slack=", c.slack, ", Shadow Price=", c.pi)

for v in prob.variables():
  print ("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)

# After reducing x_3 by 0.05 in the objective function, we now have a x_3 value of 2.18
# along w/ changed values for x_1 and x_2; 2.90 and 3.81.




# A trust officer at the Blackburg National Bank need to determine how to invest $500,000
# in the following collection of bonds to maximize the annual return:

# Bond    Annual    Maturity    Risk    Tax-Free
#         Return
#  A       9.5%      Long       High     Yes
#  B       8.0%      Short      Low      Yes
#  C       9.0%      Long       Low      No 
#  D       9.0%      Long       High     Yes
#  E       9.0%      Short      High     No 

# The officer wants to invest in at least 50% of the money in short-term issues
# and no more than 50% in high-risk issues. 
# Also, at least 30% of the funds should go into tax-free investments.
 
    
# Formulate an LP model and implement in Python:
  
# Max
# Z = 0.095x1 + 0.08x2 + 0.09x3 + 0.09x4 + 0.09x5
# x1 + x2 + x3 + x4 + x5 = 500000
#      x2           + x5 >= 250000
# x1          + x4  + x5 <=250000
# x1 + x2     + x4       >= 150000
  
from pulp import *

# Create the problem:
prob = LpProblem("National Bank Stock Returns", pulp.LpMaximize)


x1 = LpVariable('BondA', lowBound = 0)
x2 = LpVariable('BondB', lowBound = 0)
x3 = LpVariable('BondC', lowBound = 0)
x4 = LpVariable('BondD', lowBound = 0)
x5 = LpVariable('BondE', lowBound = 0)

# Objective function to maximize return
prob += 0.095*x1 + 0.08*x2 + 0.09*x3 + 0.09*x4 + 0.09*x5, "Obj"

# Constraints
prob += x1 + x2 + x3 + x4 + x5 == 500000, "Portfolio" 
prob += x2 + x5 >= 250000, "Short-term"
prob += x1 + x4 + x5 <= 250000, "High-Risk"
prob += x1 + x2 + x4 >= 150000, "TaxFree"


print(prob)

prob.solve() 
print("status: " + LpStatus[prob.status]) 

for variable in prob.variables():
     print("{}* = {}".format(variable.name, variable.varValue)) 
     
print(value(prob.objective))


# We add these lines for sensitivity analysis
print("\n Sensitivity Analysis:")

for name, c in prob.constraints.items():
    print("\n{}: Slack={}, Shadow Price = {}".format(name, c.slack, c.pi)) # OR
#    print("\n", name, ":", ", Slack=", c.slack, ", Shadow Price=", c.pi)

print("\n ========================================")

for variable in prob.variables():
     print("\n{}* = {},   Reduced Cost = {}".format(variable.name, variable.varValue, variable.dj)) 


# Optimal solution:
# Put $75,000 into A Bonds, $75,000 into B Bonds, $175,000 into C Bonds, 
# and $175,000 into E Bonds. $ 0.00 into D Bonds. 

# Binding Constraints: All constraints are binding, as they all have slack of 0. 


# Constraint 1 has a Shadow Price of 0.09
# Meaning, if we can increase the amount we are able to invest by 1 unit (1 dollar in this case),
# we can increase profit by $.09
     
# Constraint 2 has a Shadow Price of -0.0075

# Constraint 3 has a Shadow Price of 0.0075, meaning if we increase our investment amount
# in bonds that are High-Risk by one unit, we can increase annual return by 0.0075.
     
# Constraint 4 has a Shadow Price of -0.0025





# The CitruSun Corporation ships frozen orange juice concentrate from processing 
# plants in Eustis and Clermond to distributions in Miami, Orlando, and Tallahassee. 
# Each plant can produce 20 tons of concentrate each week. .The company has just
# Received orders for 10 tons from Miami for the coming week, 15 tons from Orlando,
# and 10 tons for Tallahassee. The cost per ton for supplying each of the distributors
# from each of the processing plants is shown in the following table:
    
#            Miami     Orlando     Tallahassee
# Eustis     $260       $220          $290
# Clermont   $220       $240          $320
     
# The company wants to determine the minimum costly plan for filling their orders 
# for the coming week. 
     
# ormulate an Integer LP model for this problem

# Z = 260*Eustis_Miami + 220*Eustis_Orlando + 290*Eustis_Tall + 220*Clermont_Miami + 240*Clermont_Orlando + 320*Clermont_Tall
# Eutis_Miami + Eutis_Orlando + Eutis_Tall <= 20
# Clermont_Miami + Clermont_Orlando + Clermont_Tall <= 20
# Eustis_Miami + Clermont_Miami == 10
# Eustis_Orlando + Clermond_Orlando == 15
# Eustis_Tall + Clermont_Tall == 10


    
from pulp import *

# Create a list of all processing plants:
plant =["Eustis", "Clermont"]
# Create a dictionary for the capacity:
capacity = {"Eustis": 20,
            "Clermont": 20}
# Create a list of all distributors
dc = ["Miami", "Orlando", "Tallahassee"]
# Create a dictionary for the number of units of demand for each DC
demand = {"Miami": 10,
          "Orlando": 15,
          "Tallahassee": 10}
# Create a list of costs of each transportation path
costs = [
        [260, 220, 290],
        [220, 240, 320]
        ]
# Creates the prob
prob = LpProblem("Transportatin Problem", LpMinimize)
# Creates a list of tuples containing all the possible routes for transport. 
Routes = [(i,j) for i in range(0,len(plant)) for j in range(0,len(dc))]
# A dictionary called route_vars is created to contain the referenced decision variables (the routes)
route_vars = LpVariable.dicts("Routes",(plant,dc), lowBound=0)
# The objective function is added to prob first
prob += lpSum([route_vars[plant[i]][dc[j]]*costs[i][j] for (i,j,) in Routes]), "Sum of Supplying Costs"
# The capacity constraints are added to prob for each supply node (plant)
for i in plant:
    prob += lpSum([route_vars[i][j] for j in dc]) <= capacity[i], "Cost to supply plants %s"%i

for j in dc:
    prob += lpSum([route_vars[i][j] for i in plant]) >= demand[j], "Cost to supply DCenters %s"%j



print(prob)
prob.solve()
print("Status:", LpStatus[prob.status])

for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))
    
print("Z* = ", value(prob.objective))
# We add these lines for sensitivitty analyysis
print("\n Sensitivity Analysis: ")

for name, c in prob.constraints.items():
    print("\n", name, ":", ", Slack=", c.slack, ", Shadow Price=", c.pi)

for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)




# A young couple, Eve and Steven, want to divide their main household tasks (shopping,
# cooking, dishwashing, and laundering) between them so that each has two tasks but
# the total time they spend on household duties is kept to a minimum. Their efficiencies
# on these tasks differ, where the time each would need to perform the task is given by
# the following table:
    
#           Time Needed Per Week
#         Shopping      Cooking      Dishwashing       Laundry
# Eve     4.5 Hours    7.5 Hours      3.5 Hours       3.0 Hours
# Steven  5.0 Hours    7.2 Hours      4.5 Hours       3.2 Hours

# Problem 5 a) Formulate a BIP model:
# Z = 4.5*x1 + 7.5*x2 + 3.5*x3 + 3.0*x4 + 5.0*x5 + 7.2*x6 + 4.5*x7 + 3.2*x8  

#  x1 <= y1 
#  x5 <= y1
#  x2 <= y2
#  x6 <= y2
#  x3 <= y3
#  x7 <= y3
#  x4 <= y4
#  x8 <= y4
    
from pulp import *

prob = LpProblem("Eva and Steven Chores", pulp.LpMinimize)

x1 = LpVariable('Eve_Shopping', lowBound=0, upBound=1, cat='Integer')
x2 = LpVariable('Eve_Cooking', lowBound=0, upBound=1, cat= 'Integer')
x3 = LpVariable('Eve_Dishwashing', lowBound=0, upBound=1, cat= 'Integer')
x4 = LpVariable('Eve_Laundering', lowBound=0, upBound=1, cat= 'Integer')
x5 = LpVariable('Steven_Shopping', lowBound=0, upBound=1, cat= 'Integer')
x6 = LpVariable('Steven_Cooking', lowBound=0, upBound=1, cat= 'Integer')
x7 = LpVariable('Steven_Dishwashing', lowBound=0, upBound=1, cat='Integer')
x8 = LpVariable('Steven_Laundering', lowBound=0, upBound=1, cat='Integer')

y1 = LpVariable('ShoppingTask', lowBound=0, upBound=1, cat='Integer')
y2 = LpVariable('CookingTask', lowBound=0, upBound=1, cat='Integer')
y3 = LpVariable('DishwashingTask', lowBound=0, upBound=1, cat='Integer')
y4 = LpVariable('LaunderingTask', lowBound=0, upBound=1, cat='Integer')


# Objective function:
prob += 4.5*x1 + 7.5*x2 + 3.5*x3 + 3.0*x4 \
+ 5.0*x5 + 7.2*x6 + 4.5*x7 + 3.2*x8, "Obj"

# Constraints:

# Constraints:
prob += x1 + x5  == 1, "Shopping" 
prob += x2 + x6  == 1, "Cooking"
prob += x3 + x7  == 1, "Dishwashing"
prob += x4 + x8  == 1, "Laundering"
prob += x1 + x2 + x3 + x4 == 2, "Eve's Number of Tasks"
prob += x5 + x6 + x7 + x8 == 2, "Steven's Number of Tasks"
prob += y1 + y2 + y3 + y4 == 4, "Number of Tasks"

# Constraints for whether Eve/Steven is tasked with Shopping:
prob += x1 <= y1 
prob += x5 <= y1
# Constraints for whether Eve/Steven is tasked with Cooking:
prob += x2 <= y2
prob += x6 <= y2
# Constraints for whether Eve/Steven is tasked with Dishwashing:
prob += x3 <= y3
prob += x7 <= y3
# Constraints for whether Eve/Steven is tasked with Laundering:
prob += x4 <= y4
prob += x8 <= y4
print(prob)

prob.solve()
print(LpStatus[prob.status])

for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))
    
print("Optimal Function Value = {}".format(value(prob.objective)))

# Results: Steven will do laundry and cook (10.4 Hours weekly). Eve will do the dishes and shop (8 Hours weekly. 






















