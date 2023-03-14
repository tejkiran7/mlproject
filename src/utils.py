'''
This file will contain all the common functionalities that we can use for the entire project
'''

import os
import sys
import numpy as np
import pandas as pd
import dill #used to dump python objects to file

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)