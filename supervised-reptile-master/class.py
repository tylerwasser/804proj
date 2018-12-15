
import csv
import os
from shutil import copyfile


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



    

if __name__ == '__main__':
    main()
