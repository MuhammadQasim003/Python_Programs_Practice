import pandas as pd 
import glob 
import sys 
from datetime import datetime 
import calendar 

def print_result_yearly(V1,M,D,V2,M1,D1,V3,M2,D2):
    print("Highest: {}C on {} {}".format(int(V1), M, D))
    print("Lowest: {}C on {} {}".format(int(V2), M1, D1))
    print("Humidity: {}% On {} {}".format(int(V3), M2, D2))

def print_result_monthly(specific_value,specific_value1,average):
    print("Highest Average: {}C".format(specific_value))
    print("Lowest Average: {}C".format(specific_value1))
    print("Average Humidity: {}%".format(average))

def convert_date_to_month_format(x):
    date_str = str(x)
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    month = date_obj.strftime('%B')
    day = date_obj.strftime('%d')
    return month ,day

def data_loading(addres,year,z):
    file_pattern = '{}/*_{}_{}.txt'.format(addres,year,z) 
    file_names = glob.glob(file_pattern)  
    data_frames = []  
    for file in file_names:
        data = pd.read_csv(file) 
        data_frames.append(data)
    combined_data = pd.concat(data_frames, ignore_index=True) 
    combined_data.rename(columns={'PKT': 'GST'}, inplace=True) 
    combined_data.rename(columns={'PKST': 'GST'}, inplace=True) 
    return combined_data

def getting_yearly_record(addres,year,z):   
    data = data_loading(addres,year,z)
    colum_set_1 = ['GST', 'Max TemperatureC']
    max_temprature_index = data['Max TemperatureC'].idxmax()
    min_temprature_index = data['Min TemperatureC'].idxmin()
    max_humidity_index = data['Max Humidity'].idxmax()
    max_temprature_data = data.loc[max_temprature_index, colum_set_1]
    colum_set_2 = ['GST', 'Min TemperatureC']
    min_temprature_data = data.loc[min_temprature_index, colum_set_2] 
    colum_set_3 = ['GST', 'Max Humidity']
    max_humidity_data = data.loc[max_humidity_index, colum_set_3] 
    max_temprature = max_temprature_data[1]
    min_temprature = min_temprature_data[1]
    max_humidity = max_humidity_data[1]
    max_temperature_month,max_temperature_day = convert_date_to_month_format(max_temprature_data[0])
    min_temperature_month,min_temperature_day = convert_date_to_month_format(min_temprature_data[0])
    max_humidity_month,max_humidity_day = convert_date_to_month_format(max_humidity_data[0])
    print_result_yearly(max_temprature,max_temperature_month,max_temperature_day,min_temprature,min_temperature_month,min_temperature_day,max_humidity,max_humidity_month,max_humidity_day)

def getting_monthly_record(addres,year,z):   
    data = data_loading(addres,year,z)
    H_TEMP_AVG = int(data['Max TemperatureC'].mean())
    L_TEMP_AVG = int( data['Min TemperatureC'].mean())
    AVG_HUMID = int(data['Max Humidity'].mean())
    print_result_monthly(H_TEMP_AVG,L_TEMP_AVG,AVG_HUMID)

def chart_printing(addres,year,z):
    red_color = "\033[91m"
    blue_color = "\033[94m"
    reset_color = "\033[0m"
    data = data_loading(addres,year,z)
    H_TEMP = data['Max TemperatureC']
    L_TEMP = data['Min TemperatureC']
    for i, (x, y) in enumerate(zip(H_TEMP, L_TEMP), start=1):
        if x == 'NaN' or y == 'NaN':
            print("Invalid value: x={}, y={}".format(x,y))
        else:
            try:
                x = int(x)
                print("{} {}{}{} {}C".format(i,red_color,'+' * x, reset_color,x))
                y = int(y)
                print("{} {}{}{} {}C".format(i,blue_color,'+' * y, reset_color,y))
            except ValueError:
                print("Invalid value: x={}, y={}".format(x,y))
    print(reset_color) 
    print("------------------------------------Bounus Section-------------------------------------")
    for i, (x, y) in enumerate(zip(H_TEMP, L_TEMP),start=1):
        if x == 'NaN' or y == 'NaN':
            print("Invalid value: x={}, y={}".format(x,y))
        else:
            try:
                x = int(x)
                y = int(y)

                x_line = "{}{}{}".format(red_color,'+'* x, reset_color)
                y_line = "{}{}{} {}C - {}C".format(blue_color,'+' * y, reset_color,x,y)

                print("{}{}".format(x_line,y_line))

            except ValueError:
                print("Invalid value: x={}, y={}".format(x,y))  

def main():
    if sys.argv[1] == "-e":
        try:
            addres = sys.argv[3]
            year = sys.argv[2]
            z = "*"
            getting_yearly_record(addres,year,z)
        except ValueError:
            print("You are Entering wrong argument in year ")
        
    elif sys.argv[1] == '-a':
        try:
            address = sys.argv[3]
            date_splited = str(sys.argv[2]).split('/')
            year = date_splited[0]
            z = calendar.month_abbr[int(date_splited[1])]
            getting_monthly_record(address,year,z)
        except ValueError:
            print("You are Entering wrong argument in year or month")
    elif sys.argv[1] == '-c':
        try:
            address = sys.argv[3]
            date_splited = str(sys.argv[2]).split('/')
            year = date_splited[0]
            z = calendar.month_abbr[int(date_splited[1])]
            chart_printing(address,year,z)
        except ValueError:
            print("You are Entering wrong argument in year or month")
    else:
        print("Error")

main()