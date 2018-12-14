
# import random

# import tensorflow as tf

# from supervised_reptile.args import argument_parser, model_kwargs, train_kwargs, evaluate_kwargs
# from supervised_reptile.eval import evaluate
# from supervised_reptile.models import MiniImageNetModel
# from supervised_reptile.miniimagenet import read_dataset
# from supervised_reptile.train import train

import csv
import os
from shutil import copyfile

DATA_DIR = 'data/miniimagenet'

def main():
    """
    Script for sorting images into classes
    """
    with open('data/all/test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        classes = {}
        for row in csv_reader:
            if row_count == 0:
                row_count += 1
            else:
                if row[1] in classes.keys():
                    classes[row[1]].append(row[0])
                else:
                    classes[row[1]] = [row[0]]
                row_count += 1
    for key in classes.keys():
        try:
            os.mkdir('data/all/test/' + key)
        except:
            raise Exception('failed')
        for pic in classes[key]:
            name = 'data/all/images/' + pic + '.jpg'
            copyfile(name, 'data/all/test/' + key + '/' + pic + '.jpg')






    print(classes)

    

if __name__ == '__main__':
    main()
