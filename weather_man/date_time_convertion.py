from datetime import datetime 

def convert_date_to_month_format(x):
    """
     this function will convert date from 2000-1-1 to 1 Jan 2000 format
    Args:
        x (int): contian the value of date in 2000-1-1 format

    Returns:

        list: list contain the month and dat required for further processing
    """
    
    date_str = str(x)
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    month = date_obj.strftime('%B')
    day = date_obj.strftime('%d')
    return month ,day
