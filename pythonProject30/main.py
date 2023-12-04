import datetime
import pprint
from Data_salary.salary import calculate_salary
from Data_employees.people import get_employes

dt = datetime.datetime.today()

if __name__ == '__main__':
    calculate_salary()
    get_employes()
    print(dt)