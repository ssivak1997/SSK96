# from baseFunction import *
import math

# Function to calculate the Term Life Insurance Plan value
def calc_ideal_term_insurance(income, liabilities_sum):
    return ((income*12*15)+liabilities_sum)
# Function to calculate the Medical Insurance Plan value
def calc_ideal_medic_insurance(income):
    return math.floor(income*12*0.5)
def calc_ideal_medic_insurance_premium(income):
    return math.floor(income*12*0.03)
# Function to calculate the Housing Plan value
def calc_housing_plan(estmn, eta, savings, growth_rate):
    min_down_payment = estmn*0.3
    req_down_payment = min_down_payment-savings
    r = (growth_rate/100)/12
    f = (((1+r)**(eta*12))-1)/r
    return math.floor(req_down_payment/f)
# Function to calculate the Car Plan value
def calc_car_plan(estmn, eta, savings, growth_rate):
    min_down_payment = estmn*0.3
    req_down_payment = min_down_payment-savings
    r = (growth_rate/100)/12
    f = (((1+r)**(eta*12))-1)/r
    return math.floor(req_down_payment/f)
# Function to calculate the Child Education Plan
def calc_edcn_plan(age, p_age, c_cost, savings, growth_rate, i_rate):
    n = p_age-age
    req_balance_savings = c_cost - savings
    i = 1 + (i_rate/100)
    i_adjusted = req_balance_savings*(i)**(n)
    r = (growth_rate / 100) / 12
    f = (((1 + r) ** (n * 12)) - 1) / r
    return math.floor(i_adjusted/f)
# Function to calculate the Child Marriage Plan
def calc_mrrg_plan(age, p_age, c_cost, savings, growth_rate, infl_rate):
    n = p_age-age
    req_balance_savings = c_cost - savings
    i = 1 + (infl_rate/100)
    i_adjusted = req_balance_savings*(i)**(n)
    r = (growth_rate / 100) / 12
    f = (((1 + r) ** (n * 12)) - 1) / r
    return math.floor(i_adjusted/f)
# Function to calculate the adjusted annual expenses
def calc_annual_exp(age, ret_age, expense, infl_rate):
    n = ret_age-age
    r = (1 + (infl_rate/100))**n
    return math.floor(expense * 0.6 * r)
def calc_ret_factor(growth_rate, infl_rate, post_ret_period):
    n = post_ret_period*12
    r = ((growth_rate-infl_rate)/100)/12
    a = ((1+r)**n)-1
    b = r*((1+r)**n)
    return(a/b)
def calc_ret_savings_factor(age, ret_age, growth_rate):
    # print("Inside ret savings factor calculation function:")
    # print(age)
    # print(ret_age)
    # print(ret_age-age)
    n = (ret_age-age)*12
    # print("n = " + str(n))
    r = (growth_rate/100)/12
    # print("r = " + str(r))
    f = ((1+r)**n)-1
    # print("f = " + str(f))
    return(f/r)