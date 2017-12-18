salary = [15000, 20000, 17000, 18900, 30000]

def new_salary(salary):
    return salary+.23*salary

print('The salary after raise: ')
for index, each in enumerate(salary,start=1):
    raised_salary=new_salary(each)
print('For employee {}, total salary = Rs. {:.2f}'.format(index, raised_salary))