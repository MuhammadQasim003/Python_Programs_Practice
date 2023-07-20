from fetch_data import data_loading

def print_chart(address, year, month):
    ''' this function will print the temprature chart use red color for high temprature and 
    use blue color for low temprature'''
    red_color = "\033[91m"
    blue_color = "\033[94m"
    reset_color = "\033[0m"
    data = data_loading(address, year, month)
    high_temprature = data['Max TemperatureC']
    low_temprature = data['Min TemperatureC']
    for i, (x, y) in enumerate(zip(high_temprature, low_temprature), start=1):
        if x == 'NaN' or y == 'NaN':
            print("Invalid value: x={}, y={}".format(x, y))
        else:
            try:
                x = int(x)
                print("{} {}{}{} {}C".format(i, red_color, '+' * x, reset_color, x))
                y = int(y)
                print("{} {}{}{} {}C".format(i, blue_color, '+' * y, reset_color, y))
            except ValueError:
                print("Invalid value: x={}, y={}".format(x, y))
    print(reset_color) 
    print("------------------------------------Bounus Section-------------------------------------")
    for i, (x, y) in enumerate(zip(high_temprature, low_temprature),start=1):
        if x == 'NaN' or y == 'NaN':
            print("Invalid value: x={}, y={}".format(x, y))
        else:
            try:
                x = int(x)
                y = int(y)

                x_line = "{}{}{}".format(red_color, '+'* x, reset_color)
                y_line = "{}{}{} {}C - {}C".format(blue_color, '+' * y, reset_color, x, y)

                print("{}{}".format(x_line,y_line))

            except ValueError:
                print("Invalid value: x={}, y={}".format(x, y))  
