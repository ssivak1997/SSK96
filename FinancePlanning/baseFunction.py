from operationsFunction import *

# Getting the information from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
father_name = input("Enter your father name: ")
x = input("Is " + father_name + " alive? (Y/N): ")
if x == 'Y' or x == 'y':
    father_age = int(input("Enter " + father_name + "'s age: "))
mother_name = input("Enter your mother name: ")
y = input("Is " + mother_name + " alive? (Y/N): ")
if y == 'Y' or y == 'y':
    mother_age = int(input("Enter " + mother_name + "'s age: "))
print("Select your marital status:\n1. Single\n2. Married")
marital_status = input("Marital Status: ")
child = []
child_age = []
child_education_planned_age = []
child_education_cost = []
child_education_current_savings = []
child_marriage_planned_age = []
child_marriage_cost = []
child_marriage_current_savings = []
if marital_status in ('Married', 'married', 'M', 'm', '2'):
    spouse_name = input("Enter your spouse's name: ")
    spouse_age = int(input("Enter " + spouse_name + "'s age: "))
    child_count = int(input("No. of. children: "))
    i = 1
    while i <= int(child_count):
        name = input("Enter your " + str(i) + " child's name: ")
        child.append(name)
        c_age = int(input("Enter " + name + "'s age: "))
        child_age.append(c_age)
        i += 1
income = int(input("Enter your total monthly income: "))
expense = int(input("Enter your monthly expenses: "))
tli = input("Availed Term Life Insurance? (Y/N): ")
if tli == 'Y' or tli == 'y':
    tli_sum = input("Enter the Term Life Insurance Sum Amount: ")
else:
    tli_sum = 0
mediclaim = input("Availed Medi-Claim? (Y/N): ")
if mediclaim == 'Y' or mediclaim == 'y':
    mediclaim_sum = input("Enter the Medi-Claim Sum Amount: ")
else:
    mediclaim_sum = 0
hl = input("Have you availed housing loan? (Y/N):")
if hl == 'Y' or hl == 'y':
    housing_loan = int(input("Enter the value of housing loan amount: "))
    housing_loan_emi = int(input("Enter the monthly emi amount: "))
else:
    housing_loan = 0
    housing_loan_emi = 0
    house_goal = input("Are you planning to have a new house? (Y/N) ")
    if house_goal == 'Y' or house_goal == 'y':
        house_estmtn = int(input("Enter the estimated budget of the house you are planning to have: "))
        house_eta = int(input("Enter the number of years from now when you are planning to begin the house work: "))
        house_savings = int(input("Enter the current amount of savings for the new house: "))
cl = input("Have you availed car loan? (Y/N):")
if cl == 'Y' or cl == 'y':
    car_loan = int(input("Enter the value of car loan amount: "))
    car_loan_emi = int(input("Enter the monthly emi amount: "))
else:
    car_loan = 0
    car_loan_emi = 0
    car_goal = input("Are you planning to buy a new car? (Y/N) ")
    if car_goal == 'Y' or car_goal == 'y':
        car_estmtn = int(input("Enter the estimated budget of the car you are planning to buy: "))
        car_eta = int(input("Enter the number of years from now when you are planning to buy the car: "))
        car_savings = int(input("Enter the current amount of savings for the new car: "))
if marital_status in ('Married', 'married', 'M', 'm', '2'):
    i = 1
    while i <= int(child_count):
        e_age = int(input("Enter the age of " + child[i - 1] + "'s education plan to begin with: "))
        child_education_planned_age.append(e_age)
        e_cost = int(input("Enter the current cost of education: "))
        child_education_cost.append(e_cost)
        e_savings = int(input("Enter the current savings for " + child[i-1] + "'s education: "))
        child_education_current_savings.append(e_savings)
        m_age = int(input("Enter the age of " + child[i - 1] + "'s marriage plan to begin with: "))
        child_marriage_planned_age.append(m_age)
        m_cost = int(input("Enter the current cost of marriage:"))
        child_marriage_cost.append(m_cost)
        m_savings = int(input("Enter the current savings for " + child[i - 1] + "'s marriage: "))
        child_marriage_current_savings.append(m_savings)
        i += 1
print("TOTAL LIABILITIES:")
personal_loan = int(input("Enter the value of personal loan amount: "))
gold_loan = int(input("Enter the value of gold loan amount: "))
misc_loan = int(input("Enter the value of miscellaneous loan amount: "))
print("The value of housing loan is: " + str(housing_loan))
print("The value of car loan is: " + str(car_loan))
if hl == 'Y' or hl == 'y' and cl == 'Y' or cl == 'y':
    emi = housing_loan_emi + car_loan_emi
elif hl == 'Y' or hl == 'y' and cl == 'N' or cl == 'n':
    emi = housing_loan_emi
elif hl == 'N' or hl == 'n' and cl == 'Y' or cl == 'y':
    emi = car_loan_emi
else:
    emi = 0
print("Total emi: " + str(emi))
tl = personal_loan + gold_loan + misc_loan + housing_loan + car_loan
print("Total liabilities : " + str(tl))
ret_age = int(input("What is your planned retirement age? "))
post_ret_period = int(input("Enter the post retirement period in years: "))
exp_inflation_rate = int(input("Enter the expected inflation rate: "))
exp_growth_rate = int(input("Enter the expected growth rate: "))
print("|"*60)

# Calculating the protective investment plans and it's optimal planning if they haven't availed any housing loan before
ideal_tli = calc_ideal_term_insurance(income, tl)
ideal_medi_claim_sum = calc_ideal_medic_insurance(income)
ideal_medi_claim_premium = calc_ideal_medic_insurance_premium(income)
print("\nPROTECTIVE INVESTMENT:")
print(" \t\t\t\t\t\t\t\tCURRENT VALUE\tIDEAL VALUE")
print("Term Life Insurance \t\t\t\t" + str(tli_sum) + " \t" + str(ideal_tli))
print("Medical Insurance - Sum Insured \t" + str(mediclaim_sum) + " \t\t" + str(ideal_medi_claim_sum))
print("Medical Insurance - Premium \t\t" + "0" + " \t\t\t\t" + str(ideal_medi_claim_premium))
print("*" * 10)

# Calculating the Short Term Goals and its optimal planning
print("\nSHORT TERM GOALS:")
if hl == 'N' or hl == 'n':
    ideal_housing_goal = calc_housing_plan(house_estmtn, house_eta, house_savings, exp_growth_rate)
    print("1. House Goal:")
    print("Total value of house: " + str(house_estmtn))
    print("Required Down Payment: " + str(int(int(house_estmtn) * 0.3)))
    print("Current Savings for downpayment: " + str(house_savings))
    print("Balance to be saved: " + str(int(int(house_estmtn) * 0.3) - int(house_savings)))
    print("Monthly savings required for down payment: " + str(ideal_housing_goal))
elif cl == 'N' or cl == 'n':
    ideal_car_goal = calc_car_plan(car_estmtn, car_eta, car_savings, exp_growth_rate)
    print("\n2. Car Goal:")
    print("Total value of car: " + str(car_estmtn))
    print("Required Down Payment: " + str(int(int(car_estmtn) * 0.3)))
    print("Current Savings for downpayment: " + str(car_savings))
    print("Balance to be saved:" + str((int(car_estmtn) * 0.3) - int(car_savings)))
    print("Monthly savings required for down payment: " + str(ideal_car_goal))
else:
    print("TBP")
print("*" * 10)

# Calculating the Long Term Goals and its optimal planning
print("\nLONG TERM GOALS:")
infl_adj_edcn_cost = []
infl_adj_mrrg_cost = []
for i in range(child_count):
    edctn_cost = calc_edcn_plan(child_age[i], child_education_planned_age[i], child_education_cost[i], child_education_current_savings[i], exp_growth_rate, exp_inflation_rate)
    infl_adj_edcn_cost.append(edctn_cost)
    print("Education Plan for " + child[i]+ ":")
    print("Current age of "+ child[i]+": " + str(child_age[i]))
    print("Age of " + child[i] + " while entering higher education: "+str(child_education_planned_age[i]))
    print("Current cost of  higher education of " + child[i] + ": "+ str(child_education_cost[i]))
    print("Monthly savings required for higher education of " + child[i] + ": " + str(infl_adj_edcn_cost[i]))
    mrrg_cost = calc_mrrg_plan(child_age[i], child_marriage_planned_age[i], child_marriage_cost[i], child_marriage_current_savings[i], exp_growth_rate, exp_inflation_rate)
    infl_adj_mrrg_cost.append(mrrg_cost)
    print("\nMarriage Plan for " + child[i] + ":")
    print("Current age of " + child[i] + ": " + str(child_age[i]))
    print("Planned marriage age of " + child[i] + ": " + str(child_marriage_planned_age[i]))
    print("Current cost of  marriage of " + child[i] + ": " + str(child_marriage_cost[i]))
    print("Monthly savings required for marriage of " + child[i] + ": " + str(infl_adj_mrrg_cost[i]))
print("*"*10)

# Calculating the retirement plan
annl_amnt = calc_annual_exp(age, ret_age, expense, exp_inflation_rate)
pst_rtrmnt_fct = calc_ret_factor(exp_growth_rate, exp_inflation_rate, post_ret_period)
pst_rtrmnt_req_amnt = annl_amnt*pst_rtrmnt_fct
ret_savings_factor = calc_ret_savings_factor(age, ret_age, exp_growth_rate)
pst_rtrmnt_savings = pst_rtrmnt_req_amnt/ret_savings_factor
print("\nRETIREMENT PLAN:")
print("Post retirement required amount: " + str(pst_rtrmnt_req_amnt))
print("Post retirement savings factor: " + str(ret_savings_factor))
print("Monthly savings for retirement: " + str(pst_rtrmnt_savings))
# Consolidating the summary of the financial planning done so far
print("#"*10)
print("\nSUMMARY OF FINANCIAL PLANNING")
monthly_tli = (ideal_tli*0.0005)/12
monthly_mediclaim = ideal_medi_claim_premium/12
if x in ("Y", "y") and y in ("Y", "y"):
    parental_monthly_tli = monthly_tli*2
    parental_monthly_mediclaim = monthly_mediclaim*2
elif x in ("Y", "y") or y in ("Y", "y"):
    parental_monthly_tli = monthly_tli*0.5
    parental_monthly_mediclaim = monthly_mediclaim*0.5
print("Total Income: " + str(income))
print("Total Expenses: " + str(expense))
print("\nMonthly contribution to Term Insurance: " + str(monthly_tli))
print("Monthly contribution to Medical Insurance: " + str(monthly_mediclaim))
print("Monthly contribution to Term Insurance for parents: " + str(parental_monthly_tli))
print("Monthly contribution to Medical Insurance for parents: " + str(parental_monthly_mediclaim))
total_insurance = monthly_mediclaim+monthly_tli+parental_monthly_tli+parental_monthly_mediclaim
print("Total Insurance: " + str(total_insurance))
print("\nHousing Loan EMI: " + str(housing_loan_emi))
print("Car Loan EMI: " + str(car_loan_emi))
print("Total EMI: " + str(emi))
print("\n")
for i in range(child_count):
    print("Savings for Education of " + child[i] +" : " + str(infl_adj_edcn_cost[i]))
    print("Savigns for Marriage of " + child[i] +" : " + str(infl_adj_mrrg_cost[i]))
print("Savings for Retirement: " + str(int(pst_rtrmnt_savings)))
edctn_savings = sum(infl_adj_edcn_cost)
marriage_savigns = sum(infl_adj_mrrg_cost)
total_savings = int(pst_rtrmnt_savings+edctn_savings+marriage_savigns)
print("Total Savings: " + str(total_savings))
net_amnt = income - (total_savings+emi+total_insurance+expense)
print("\nNet amount of income-expense summary is " + str(net_amnt))
if net_amnt > 0:
    print("Your income-expense net amount is surplus and you can consider investing more")
else:
    print("Your income-expense net amount is deficit and you should consider increasing your income or reducing your expenses")