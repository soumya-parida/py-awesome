#extracting raw data files into the local directories
#importing packages to be used
import os
from dotenv import find_dotenv, load_dotenv
from requests import session
import logging

#payload for kaggle login
payload = {'action':'login',
           'username':'soumyaparida81',
           'password':'Soumya123'}

login_url = "https://www.kaggle.com/account/login"


def extract_data(url, output_file_path):
    ''' 
    This method extracts the training datasets from Kaggle website.
    The login values are from env files.
    '''
    with session() as s:
        s.post(login_url, payload)
        #assuming the login works. We are not chekcking the response.
        with open(output_file_path, 'wb') as handle:
            response = s.get(url, stream = True)
            for block in response.iter_content(1024):
                handle.write(block)

def main(project_dir):
    train_url = 'https://www.kaggle.com/c/3136/download/train.csv'
    test_url = 'https://www.kaggle.com/c/3136/download/test.csv'

    raw_data_path = os.path.join(project_dir, 'data', 'raw')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')

    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)


if __name__ == '__main__':
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    dot_envpath = find_dotenv()
    load_dotenv(dot_envpath)

    main(project_dir)

