CLASS_A = 20
CLASS_B = 15
CLASS_C = 10
def main():
    soldTickets_A = int(input('Enter number of sold tickets of class A: '))
    soldTickets_B = int(input('Enter number of sold tickets of class B: '))
    soldTickets_C = int(input('Enter number of sold tickets of class C: '))
    incomeFrom_A = income_A(soldTickets_A)
    incomeFrom_B = income_B(soldTickets_B)
    incomeFrom_C = income_C(soldTickets_C)
    print('Class A income =',incomeFrom_A)
    print('Class B income =',incomeFrom_B)
    print('Class C income =',incomeFrom_C)
    income = total_income(incomeFrom_A,incomeFrom_B,incomeFrom_C)
    print('Total income =',income)
def income_A(tickets):
    return CLASS_A*tickets
def income_B(tickets):
    return CLASS_B*tickets
def income_C(tickets):
    return CLASS_C*tickets
def total_income(income1,income2,income3):
    return income1+income2+income3
main()