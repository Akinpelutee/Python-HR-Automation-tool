import pandas as pd


departments = ["Operations", "Engineering", "Marketing", "Product", "Partnership"]
names = [
    "Temitope", "Adaeze", "Suzan", "Justina", "Gfave", "Jessey", "Jemima", "Victor", "Comfort", "Ebube", "Dotun", "Somto", "Rasheed", "Blaize",
    ]
months = ["Jan", "Feb", "March", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def get_name():
    """
    Gets the name of worker

    Returns:
        The name of the worker

    Raises:
        ValueError if name of worker not present in the names global variable list
    """
    while True:
        try:
            name = str(input("Worker name (or 'q' to quit) ")).strip()
            if name == 'q':
                return None
            if name.lower() in [n.lower() for n in names]:
                return name.capitalize()
            else:
                raise ValueError ("Name not found. Enter a valid name or 'q' to quit: ")
        except ValueError as e:
            print(e)
    
def get_dept():
    """
    Gets the department of worker

    Returns:
        The department of the worker

    Raises:
        ValueError if name of worker not present in the department global variable list
    """
    while True:
        try:
            dept = str(input("Worker department (or 'q' to quit): "))
            if dept == 'q':
                return None
            if dept.lower() in [d.lower() for d in departments]:
                return dept.capitalize()
            else:
                raise ValueError (f"Dept not in departments. Enter a valid department or 'q' to quit: ")
        except ValueError as e:
            print(e)
            


def get_month():
    """
    Gets the month 

    Returns:
        The month

    Raises:
        ValueError if month not present in the months global variable list
    """
    while True:
        try:
            month = str(input("Enter the month, e.g 'jan' or 'q' to quit: "))
            if month == 'q':
                return None
            if month.lower() in [m.lower() for m in months]:
                return month.capitalize()
            else:
                raise ValueError (f"{month} not in months. Enter the month, e.g 'jan'")
        except ValueError as e:
            print(e)
    


def get_week():
    """
    Gets the week of the month

    Returns:
        The week of the month
    
    Raises:
        ValueError if value is negative or > 5
        TypeError if non integer value is entered
    """
    while True:
        try:
            week = str(input("Enter the week. e.g 1-5 or 'q' to quit: "))
            if week == 'q':
                return None
            if week.isdigit() and int(week) > 0:
                return week
            else:
                raise ValueError ("Value must be an Interger!!!. 'q' to quit ")
        except ValueError as e:
            print(e)

def get_total_time_worked():
    """
    Gets the total time worked for the week by the worker

    Returns:
        The total time worked for the week by the worker

    Raises:
        TypeError if a non integer value is input
    """
    while True:
        try:
            time_worked = str(input("Enter the time worked in 'HH:MM' or 'q' to quit: "))
            if time_worked == 'q':
                return None
            hours, minutes = map(int, time_worked.split(':'))
            if hours < 0 or minutes < 0 or minutes >= 60:
                raise ValueError ("Value cannot be a string or less than 0. It should be in (HH:MM) format!!!")
            decimal_time = hours + minutes / 60
            return round(decimal_time,2)
        except ValueError as e:
            print(e)

def get_idle_mins():
    """
    Gets the idle mins of the worker

    Returns:
        The idle mins of the worker in percentage

    Raises:
        TypeError if non integer value is input
    """
    while True:
        try:
            idle_min = input("Enter the idle mins (or 'q' to quit): ")
            if idle_min == 'q':
                return None
            if idle_min.isdigit() and int(idle_min) >= 0:
                idle_min_percentage = int(idle_min) / 100
                return idle_min_percentage
            else:
                raise ValueError ("Value cannot be a str or negative.")
        except ValueError as e :
            print (e)


def get_expected_hr_worked():
    """
    Gets the number of hrs expected to work in a week

    Returns:
        The expected num of hrs worked

    Raises:
        TypeError if non integer value is input
        ValueError if a negative is input
    """
    while True:
        try:
            expected_hr = int(input("Enter the number of expected hour worked ('q' to quit): "))
            if expected_hr == 'q':
                return None
            if expected_hr < 0:
                raise ValueError("Value cannot be a string or negative. Try again!!!")
            return expected_hr
        except ValueError as e:
            print(e)
        except Exception as e:
            print("An unexpected error occured:", str(e))


def get_kpi_assigned():
    """
    Gets worker's kpi assigned for the week

    Returns:
        The number of kpi assigned to the worker for the week

    Raises:
        TypeError if non integer value is input
        ValuError when a negative value is input
    """
    while True:
        try:
            kpi_assigned = int(input("Enter the number of kpi assigned for the week ('q' to quit): "))
            if kpi_assigned == 'q':
                return None
            if kpi_assigned < 0:
                raise ValueError ("Value cannot be negative. Try again!!!")
            return kpi_assigned
        except ValueError as e:
            print(e)

def get_kpi_completed():
    """
    Gets worker's kpi completed for the week

    Returns:
        The number of kpi completed by the worker for the week

    Raises:
        ValuError when a negative value is input
    """
    while True:
        try:
            kpi_completed = int(input("Enter the number of kpi_completed for the week: "))
            if kpi_completed == 'q':
                return None
            if kpi_completed < 0:
                raise ValueError ("Value cannot be negative. Try again!!!")
            return kpi_completed
        except ValueError as e:
            print(e)



def get_gather_time():
    """
    Gets number of avg hrs available in gather office

    Returns:
        The number in percentage of hrs available in gather

    Raises:
        ValuError when a negative value is input
    """
    while True:
        try:
            gather_time = input("Enter the no of hour available on gather in e.g (35,40) format. ('q' to quit): ")
            if gather_time.lower() == 'q':
                return None
            val_1, val_2 = map(int, gather_time.split(','))
            if val_1 < 0 or val_2 < 0:
                raise ValueError ("Value cannot be negative!!!")
            avg_gather_time = (val_1 + val_2) / 2
            expected_hr_worked = get_expected_hr_worked()
            gather_time_percentage = (avg_gather_time / expected_hr_worked) * 100
            return round(gather_time_percentage,2)
        except ValueError as e:
            print(e)
