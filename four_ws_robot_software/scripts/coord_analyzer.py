import csv
import math
import os
import matplotlib.pyplot as plt

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            data.append([float(row[0]), float(row[1])])
    return data

def calculate_std_dev(slam_data_x, slam_data_y, ground_truth_data_x, ground_truth_data_y):
    # Calculate differences between ground truth and SLAM data for X and Y separately
    differences_x = []
    differences_y = []
    for i in range(len(slam_data_x)):
        diff_x = slam_data_x[i] - ground_truth_data_x[i]
        differences_x.append(diff_x)
        diff_y = slam_data_y[i] - ground_truth_data_y[i]
        differences_y.append(diff_y)
    # Calculate mean of differences for X and Y separately
    mean_x = sum(differences_x) / len(differences_x)
    mean_y = sum(differences_y) / len(differences_y)
    # Calculate sum of squared differences for X and Y separately
    ssd_x = sum([(x - mean_x) ** 2 for x in differences_x])
    ssd_y = sum([(y - mean_y) ** 2 for y in differences_y])
    # Calculate standard deviation for X and Y separately
    std_dev_x = math.sqrt(ssd_x / (len(differences_x) - 1))
    std_dev_y = math.sqrt(ssd_y / (len(differences_y) - 1))
    return std_dev_x, std_dev_y

def main():
    # Read in ground truth data and SLAM data
    ground_truth_file = os.path.expanduser('~/ground_truth_listener.csv')
    slam_data_file = os.path.expanduser('~/tf_map_base_listener.csv')
    ground_truth_data = read_csv(ground_truth_file)
    slam_data = read_csv(slam_data_file)

    # Separate X and Y vectors
    slam_data_x = [x[0] for x in slam_data]
    slam_data_y = [x[1] for x in slam_data]
    ground_truth_data_x = [x[0] for x in ground_truth_data]
    ground_truth_data_y = [x[1] for x in ground_truth_data]

    # Calculate standard deviation for X and Y separately
    std_dev_x, std_dev_y = calculate_std_dev(slam_data_x, slam_data_y, ground_truth_data_x, ground_truth_data_y)

    # Print standard deviation for X and Y separately
    print("Standard deviation for X:", std_dev_x)
    print("Standard deviation for Y:", std_dev_y)

    # Plot ground truth data and SLAM data
    plt.scatter(ground_truth_data_x, ground_truth_data_y, label='Ground Truth Data')
    plt.scatter(slam_data_x, slam_data_y, label='SLAM Data')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()