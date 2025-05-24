monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter yourtotal monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are", monthly_savings)
ProjectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: ", ProjectedSavings)