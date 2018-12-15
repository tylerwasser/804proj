import csv
import os
from shutil import copyfile


def manhattan_dist(feature_array1, feature_array2):
    dist = 0
    for i in range(len(feature_array1)):
        dist += abs(int(feature_array1[i]) - int(feature_array2[i]))
    return dist


def knn(feature_array1, feature_array2, test_array):
    first_dist = manhattan_dist(feature_array1, test_array)
    second_dist = manhattan_dist(feature_array2, test_array)
    if first_dist == second_dist:
        return 0
    elif first_dist > second_dist:
        return 2
    return 1


def get_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        first_data = []
        second_data = []
        test_data = []
        for row in csv_reader:
            if row[0] == '':
                pass
            else:
                if row_count % 3 == 0:
                    first_data.append(row[1:])
                elif row_count % 3 == 1:
                    second_data.append(row[1:])
                else:
                    test_data.append(row[1:])
                row_count += 1
    return (first_data, second_data, test_data)

def main():
    """
    Script for sorting images into classes
    """
    output = []
    first_data, second_data, test_data = get_data('data_features.csv')
    for i in range(len(test_data)):
        output.append(knn(first_data[i], second_data[i], test_data[i]))
    print(output)
 

if __name__ == '__main__':
    main()