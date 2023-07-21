import glob
import pandas as pd

def data_loading(address, year, month):
    """ this function is using globe to load the bunch of file from directly 
    and then storing them  into one dataFrame
    Args:
        address (str): use to get the root address for the data directory
        year (str): get the desired year argument for the directory 
        month (str): get the desired month argument for the directory 
    Returns:
        list: return combined_data which contian with all the required data re  quired for processing
    """
    
    file_pattern = '{}/*_{}_{}.txt'.format(address, year, month) 
    file_names = glob.glob(file_pattern)  
    data_frames = []  
    for file in file_names:
        data = pd.read_csv(file) 
        data_frames.append(data)
    combined_data = pd.concat(data_frames, ignore_index=True) 
    combined_data.rename(columns={'PKT': 'GST'}, inplace=True) 
    combined_data.rename(columns={'PKST': 'GST'}, inplace=True) 
    return combined_data
