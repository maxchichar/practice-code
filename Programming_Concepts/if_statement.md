# IF STATEMENTS IN PROGRAMMING

if statements allow your program to make decision based on the situation and respond based on the particular situation.

## What is an if Statement?
An if statement runs when a block of code condition is true.
Like a dice game, if the numder on a dice is not equal to 6 try again:

Python
```py
dice = random.randint(1,6)
print('You rolled a ' + str(dice))

if dice == 6:
    print('You won 🥳!! by getting 6')
else:
    print('Try again')
```

Go
```go 
var dice = rand.IntN(6) + 1

if dice != 6{
    fmt.Print("Try again")
}else if dice == 6{
    fmt.Print("You got 6 🥳. Congrants")
}else{
    fmt.Print("Roll")
}
```

## When Should You Use an if Statement?

When your program is to do something based on a situation e.g If a user get the password and username correctly print `"Welcome"` else if he get's the password and username wrong `"Access Denied"`

## The Else if Statement

Python
```py
age = 15
print('Age: ' + str(age))

if age < 18:
    print('You are a Teenager')
elif age < 13:
    print('You are a Child')
else:
    print('You are an Adult')
```

## The Nested if Statement
This an if statement inside another if statement.

Python
```py
age = 19
print('Age: ' + str(age))

if age < 13:
    print('You are a Child')
elif age < 20:
    print('You are a Teenager')
    if age > 18:
        print('and an Adult')
else:
    print('You are an Adult')
```

