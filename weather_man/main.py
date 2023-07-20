import sys 
import calendar
from print_record_chart import print_chart 
from data_extraction import get_month_record, get_year_record

def main():
    ''' this function will get the user argument and run the condition according to user arguments'''
    if sys.argv[1] == "-e":
        try:
            address = sys.argv[3]
            year = sys.argv[2]
            month = "*"
            get_year_record(address, year, month)
        except ValueError:
            print("You are Entering wrong argument in year ")
        
    elif sys.argv[1] == '-a':
        try:
            address = sys.argv[3]
            date_splited = str(sys.argv[2]).split('/')
            year = date_splited[0]
            month = calendar.month_abbr[int(date_splited[1])]
            get_month_record(address, year, month)
        except ValueError:
            print("You are Entering wrong argument in year or month")
    elif sys.argv[1] == '-c':
        try:
            address = sys.argv[3]
            date_splited = str(sys.argv[2]).split('/')
            year = date_splited[0]
            month = calendar.month_abbr[int(date_splited[1])]
            print_chart(address, year, month)
        except ValueError:
            print("You are Entering wrong argument in year or month")
    else:
        print("Error")

if __name__ == "__main__":
    main()
