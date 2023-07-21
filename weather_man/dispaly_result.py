def print_year_result(max_temprature,max_temperature_month,max_temperature_day,min_temprature,min_temperature_month,min_temperature_day,max_humidity,max_humidity_month,max_humidity_day):
    """
        This function will display the result of year
    Args:
        max_temprature (str): variable contain the value of max temprature 
        max_temperature_month (str): variable contain month of the max temprature
        max_temperature_day (str): varable contian day of the max temprature
        min_temprature (str): variable contain the value of min temprature
        min_temperature_month (str): varaible contain month of the min temprature
        min_temperature_day (str):  variable contain day of the min temprature
        max_humidity (str): variable contain the value max humidity
        max_humidity_month (str): variable contain month of the max humidity
        max_humidity_day (str): variable contain day of the max humidity
    """
    
    print("Highest: {}C on {} {}".format(int(max_temprature), max_temperature_month, max_temperature_day))
    print("Lowest: {}C on {} {}".format(int(min_temprature), min_temperature_month, min_temperature_day))
    print("Humidity: {}% On {} {}".format(int(max_humidity), max_humidity_month, max_humidity_day))

def print_month_result(high_temprature_average,low_temprature_average,max_humidity_average):
    """
    this function will display the result of month 
    Args:
        high_temprature_average (str): variable contain the average value of max temprature
        low_temprature_average (str): variable contain the average value of min temprature
        max_humidity_average (str): variable contain the average value of max humidity
    """
    print("Highest Average: {}C".format(high_temprature_average))
    print("Lowest Average: {}C".format(low_temprature_average))
    print("Average Humidity: {}%".format(max_humidity_average))
