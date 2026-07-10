# Data types tutorial in Python

revenue = 50
expense = 10 
profit = revenue - expense
print(profit)

margin = profit * 100 / revenue

print(margin)

print(type(margin)) # float
print(id(margin))

expenses_description = "mexican food are dish dash in sunnyvale"
print(type(expenses_description)) # str

print(expenses_description)
print(len(expenses_description))

# Naming convention is usually snake case: Refer to PEP style guide: https://peps.python.org/pep-0008/


revenues = [50, 60, 55]
expenses = [10, 30, 35]

for rev in revenues:
    print(f"Revenues: {rev}") # Format string
    

for i in range(len(revenues)):
    net_profit = revenues[i] - expenses[i]
    net_margin = net_profit * 100 / revenues[i]
    print(f"Margin Q{i + 1} >>> {net_margin:.2f}") 

# Using the append and list
margins = []

for i in range(len(revenues)):
    net_profit = revenues[i] - expenses[i]
    net_margin = net_profit * 100 / revenues[i]
    margins.append(net_margin)
    print(margins)

# Dictionary
fin = { 
    "revenue": 50, 
    "expenses": 10
}


print(type(fin)) # dict

fin["profit"] = fin["revenue"] - fin["expenses"]
print(fin)

financials = [
    {"revenue": 50, "expenses": 10}, # q1
    {"revenue": 60, "expenses": 30}, # q2
    {"revenue": 55, "expenses": 35} # q3
]
print(financials)

for fin in financials:
    profit = fin["revenue"] - fin["expenses"]
    fin["margin"] = profit * 100 / fin["revenue"]
print(financials)

# Nested Dictionary
financials = {
    "Q1": {"revenue": 50, "expense": 10},
    "Q2": {"revenue": 60, "expense": 30},
    "Q3": {"revenue": 55, "expense": 35}
}

for quarter, data in financials.items():
    margin = data["revenue"] - data["expense"] * 100 / data["revenue"]
    print(f"Quarter: {quarter} Data: {data} Margin: {margin}")