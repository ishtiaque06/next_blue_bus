from csv_parser import parser
from get_csv_data import get_data

import datetime

"""
Function retrieves the day's relevant csv file and returns a list of dictionaries of time
"""
def relevant_csv():
    csv_list = parser() #makes list of csvs parsed from the BlueBus Website
    today = (datetime.datetime.now()).strftime('%A')  #gives the name of the day
    
    for csv in csv_list:
        if today in csv:
            
            relevant_csv = csv
            
        #since there are 2 different CSVs for Saturday: Daytime and Nighttime
        elif today == "Saturday" and ("Daytime" in csv): 
                relevant_csv = csv
        
        elif today == "Saturday" and ("Night" in csv):
            relevant_csv = csv
                
                               
                
    time_dict_list = get_data(relevant_csv)  #a list of dictionaries with relevant time for the current day
    
    return time_dict_list


if __name__ == '__main__':
    relevant_csv()

