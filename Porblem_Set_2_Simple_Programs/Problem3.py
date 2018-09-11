# -*- coding: utf-8 -*-
"""
Problem 3 - Using Bisection Search to Make the Program Faster
20.0/20.0 points (graded)
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. 
Why did we make it that way? You can try running your code locally so that 
the payment can be any dollar and cent amount (in other words, 
the monthly payment is a multiple of $0.01). Does your code still work? 
It should, but you may notice that your code runs more slowly, 
especially in cases with very large balances and interest rates. 
(Note: when your code is running on our servers, 
there are limits on the amount of computing time each submission is allowed, 
so your observations from running this experiment on the grading system 
might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than 
we did in Problem 2 without running into the problem of slow code? 
We can make this program run faster using a technique introduced in lecture 
- bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal
"""
#test data
#balance = 5000
#annualInterestRate = 0.08


inibalance = balance

MinterestRate= annualInterestRate/ 12.0
lowerbound = balance / 12
upperbound = (balance * (1 + MinterestRate)**12) / 12.0
ans = (upperbound + lowerbound)/2.0

gap = 0.01
i = 1
    
while abs(balance) > gap:
    ans = (upperbound + lowerbound)/2
    balance = inibalance
    for i in range(12):
        balance = balance - ans + ((balance - ans) * MinterestRate)
    if balance > gap:
        lowerbound = ans
    elif balance < -gap:
        upperbound = ans
    else:
        break
print('Lowest Payment:', round(ans, 2))
