import pandas as pd


departments = ["Operations", "Engineering", "Marketing", "Product", "Partnership"]
names = [
    "sam", "kylie", "tops", "mary", "jessica", "folan", "suzzy", "darren", "smith", "eden", "josh", "jeane", "adam", "taylor", "coren"
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
    try:
        name = str(input("Worker name: "))
        if name.lower() not in names:
            raise ValueError ("Name must be someone working in the company:")
        return name
    except ValueError as e:
        print(e)
        return get_name
    
def get_dept():
    """
    Gets the department of worker

    Returns:
        The department of the worker

    Raises:
        ValueError if name of worker not present in the department global variable list
    """
    try:
        dept = str(input("Worker name: "))
        if dept.lower() not in  departments:
            raise ValueError (f"{dept} not in departments. Try again!!!")
        return dept
    except ValueError as e:
        print(e)
        return get_dept


def get_month():
    """
    Gets the month 

    Returns:
        The month

    Raises:
        ValueError if month not present in the months global variable list
    """
    try:
        month = str(input("Enter the month, e.g 'jan': "))
        if month.lower() not in months:
            raise ValueError (f"{month} not in months. Enter the month, e.g 'jan'")
        return month
    except ValueError as e:
        print(e)
        return get_month
    


def get_week():
    """
    Gets the week of the month

    Returns:
        The week of the month
    
    Raises:
        ValueError if value is negative or > 5
        TypeError if non integer value is entered
    """
    try:
        week = int(input("Enter the week. e.g 1-5"))
        if week <= 0:
            raise ValueError ("Value must be an Interger. ")
        return week
    except ValueError as e:
        print(e)
        return get_week

def get_total_time_worked():
    """
    Gets the total time worked for the week by the worker

    Returns:
        The total time worked for the week by the worker

    Raises:
        TypeError if a non integer value is input
    """
    try:
        time_worked = input("Enter the time worked in 'HH:MM': ")
        hours, minutes = map(int, time_worked.split(':'))
        if hours < 0 or minutes < 0 or minutes >= 60:
            raise ValueError ("Value cannot be a string or less than 0. It should be in (HH:MM) format!!!")
        decimal_time = hours + minutes / 60
        return decimal_time
    except ValueError as e:
        print(e)
        return get_total_time_worked

def get_idle_mins():
    """
    Gets the idle mins of the worker

    Returns:
        The idle mins of the worker in percentage

    Raises:
        TypeError if non integer value is input
    """
    

def get_expected_hr_worked():
    """
    Gets the number of hrs expected to work in a week

    Returns:
        The expected num of hrs worked

    Raises:
        TypeError if non integer value is input
        ValueError if a negative is input
    """
    pass

def get_kpi_assigned():
    """
    Gets worker's kpi assigned for the week

    Returns:
        The number of kpi assigned to the worker for the week

    Raises:
        TypeError if non integer value is input
        ValuError when a negative value is input
    """
    pass

def get_kpi_completed():
    """
    Gets worker's kpi completed for the week

    Returns:
        The number of kpi completed by the worker for the week

    Raises:
        ValuError when a negative value is input
    """
    pass

def get_gather_time():
    """
    Gets number of avg hrs available in gather office

    Returns:
        The number in percentage of hrs available in gather

    Raises:
        ValuError when a negative value is input
    """
    pass
