import pandas as pd
import csv
from data_entering import get_dept,get_expected_hr_worked,get_gather_time,get_idle_mins,get_kpi_assigned,get_kpi_completed,get_month,get_name,get_total_time_worked,get_week

class CSV:
    """
    Allows the manipulation of the csv file
    """
    def __init__(self, csv_file='efficiency_metrics.csv'):
        """Initilizes the CSV file handler attributes"""
        self.csv_file = csv_file
        self.COLUMNS = [
            'dept','name','month','week','total_time_wrked','idle_mins','expected_hr_wrked','kpi_ass','kpi_comp','gather_time'
            ]
        

    def initialize_csv(self):
        """Initializes the csv file if it doesn't exist"""
        try:
            pd.read_csv(self.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.COLUMNS)

            #Export to csv format
            df.to_csv(self.csv_file, index=False)
            print(f"File {self.csv_file} initialized sucessfully")

    def add_data(
            self,dept,name,month,week,total_time_wrked,idle_mins,expected_hr_wrked,kpi_ass,kpi_comp,gather_time
            ):
        """Adds new entry to the file"""
        new_entry ={
            'name':name,
            'dept':dept,
            'month':month,
            'week':week,
            'total_time_wrked':total_time_wrked,
            'idle_mins':idle_mins,
            'expected_hr_wrked':expected_hr_wrked,
            'kpi_ass':kpi_ass,
            'kpi_comp':kpi_comp,
            'gather_time':gather_time
        }

        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.COLUMNS)
            writer.writerow(new_entry)
        print("Entry successfully added........")


def add_data():
    csv_handler = CSV()
    csv_handler.initialize_csv()
    name = get_name()
    dept = get_dept()
    month = get_month()
    week = get_week()
    total_time_wrked = get_total_time_worked()
    idle_mins = get_idle_mins()
    expected_hr_wrked = get_expected_hr_worked()
    kpi_ass = get_kpi_assigned()
    kpi_comp = get_kpi_completed()
    gather_time = get_gather_time()

    csv_handler.add_data(dept,name,month,week,total_time_wrked,idle_mins,expected_hr_wrked,kpi_ass,kpi_comp,gather_time)
  
add_data()