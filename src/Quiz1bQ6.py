// Added new compounding rate calculator
//
// This fixes a bug

    
def future_value(present_value, annual_rate, periods_per_year, years):
	rate_per_period = annual_rate / periods_per_year
	periods = periods_per_year * years

    # Put your code here.
	# More code here
	new_value = present_value * (1 + rate_per_period) ** periods
	return new_value

print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, 0.02, 365, 3))
print ("$500 at 4% compounded 10 times during each of 10 years yield $", future_value(500, .04, 10, 10))
print ("$750 at 6% compounded 15 times during each of 10 years yield $", future_value(750, .06, 15, 10))
// Specify floats
print ("$850.01 at 9% compounded 12 times during each of 10 years yield $", future_value(850.01, .09, 12, 10))
