import logging
import os
import pandas as pd
from sklearn.model_selection import train_test_split


#creating logging obj
logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

#logging in console
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

#logging in a file
os.makedirs('logs',exist_ok=True)
log_file_path = os.path.join('logs','data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

#setting format for logs
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(format)
file_handler.setFormatter(format)

#adding both types of logging to logger obj
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#load data
def load_data(data_url: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_url)
        logger.debug(f'data loaded from {data_url}')
        return df
    except pd.errors.ParserError as e:
        logger.error('Falied to parse the CSV file %s',e)
        raise
    except Exception as e:
        logger.error('Error while loadung %s',e)
        raise

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace = True)
        df.rename(columns = {'v1': 'target', 'v2': 'text'}, inplace = True)
        logger.debug('Data pre procesing complete')
        return df
    except KeyError as e:
        logger.error('Missing column in DataFrame %s',e)
        raise
    except Exception as e:
        logger.error('Error while preprocessing %s',e)
        raise

def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str):
    try:
        raw_data_path = os.path.join(data_path,'raw_data')
        os.makedirs(raw_data_path,exist_ok=True)
        train_data.to_csv(os.path.join(raw_data_path,'train.csv'),index = False)
        test_data.to_csv(os.path.join(raw_data_path,'test.csv'),index = False)
        logger.debug('Data saving complete')
    except KeyError as e:
        logger.error('Missing column in DataFrame %s',e)
        raise
    except Exception as e:
        logger.error('Error while saving data %s',e)
        raise
def main():
    try:
        test_size = 0.2
        data_path = r'C:\Users\ADMIN\Desktop\MLOPS project\spam.csv'
        df = load_data(data_path)
        processed_data = preprocess_data(df)
        train_data,test_data = train_test_split(processed_data,test_size = test_size, random_state=2)
        save_data(train_data, test_data, data_path =r'C:\Users\ADMIN\Desktop\MLOPS project\data')
    except Exception as e:
        logger.error('Failed to complete data ingestion %s',e)
        print('error: ',e)
if __name__ == '__main__':
    main()


    