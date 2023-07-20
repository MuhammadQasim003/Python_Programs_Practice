def print_year_result(max_temprature,max_temperature_month,max_temperature_day,min_temprature,min_temperature_month,min_temperature_day,max_humidity,max_humidity_month,max_humidity_day):
    ''' this function will display the result of year '''
    print("Highest: {}C on {} {}".format(int(max_temprature), max_temperature_month, max_temperature_day))
    print("Lowest: {}C on {} {}".format(int(min_temprature), min_temperature_month, min_temperature_day))
    print("Humidity: {}% On {} {}".format(int(max_humidity), max_humidity_month, max_humidity_day))

def print_month_result(high_temprature_average,low_temprature_average,max_humidity_average):
    ''' this function will display the result of month '''
    print("Highest Average: {}C".format(high_temprature_average))
    print("Lowest Average: {}C".format(low_temprature_average))
    print("Average Humidity: {}%".format(max_humidity_average))