
from date_time_convertion import convert_date_to_month_format
from fetch_data import data_loading
from dispaly_result import print_month_result, print_year_result


def get_year_record(address, year, month):  
    ''' this function will get the year record from loaded data '''
    data = data_loading(address, year, month)
    max_temprature_index = data['Max TemperatureC'].idxmax()
    min_temprature_index = data['Min TemperatureC'].idxmin()
    max_humidity_index = data['Max Humidity'].idxmax()
    column_index = [max_temprature_index,min_temprature_index,max_humidity_index]
    column = ['Max TemperatureC', 'Min TemperatureC', 'Max Humidity']
    fetched_value = []
    for x, y in zip(column, column_index):
        column_set = ['GST', x]
        fetched_value.append(data.loc[y, column_set])
    max_temprature = fetched_value[0][1]
    min_temprature = fetched_value[1][1]
    max_humidity = fetched_value[2][1]
    max_temperature_month,max_temperature_day = convert_date_to_month_format(fetched_value[0][0])
    min_temperature_month,min_temperature_day = convert_date_to_month_format(fetched_value[1][0])
    max_humidity_month,max_humidity_day = convert_date_to_month_format(fetched_value[2][0])
    print_year_result(max_temprature,max_temperature_month,max_temperature_day,min_temprature,min_temperature_month,min_temperature_day,max_humidity,max_humidity_month,max_humidity_day)

def get_month_record(address, year, month): 
    ''' this function will get the month record from loaded data '''
    data = data_loading(address, year, month)
    high_temprature_average = int(data['Max TemperatureC'].mean())
    low_temprature_average = int( data['Min TemperatureC'].mean())
    max_humidity_average = int(data['Max Humidity'].mean())
    print_month_result(high_temprature_average,low_temprature_average,max_humidity_average)