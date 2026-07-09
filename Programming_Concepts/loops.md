# LOOPS IN PROGRAMMING

Based on my understanding it is to run the same lines of code multiple times

## What is a Loop?
A loop runs the same code over and over again as long as the condition is `true`. e.g


```py
dice = random.randint(1,2)
while dice != 6:
    dice = random.randint(1,2)
    count += 1
print("You've got 6!")
```

## Nested Loop 

This is a loop inside another loop.

```py
numExperiments = 1000
totalRolls = 0

for i in range(numExperiments):
    count = 0
    while True:
        dice = random.ranint(1,6)
        count += 1
        if dice == 6:
            break
    totalRolls += count
print('Doing', numExperiments,'experiments')
print('Average rolls to get 6: ', totalRolls/numExperiments)
```