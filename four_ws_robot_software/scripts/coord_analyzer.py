import csv
import math
import os
import matplotlib.pyplot as plt
import numpy as np

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # пропускаем заголовок
        for row in reader:
            data.append([float(row[0]), float(row[1])])
    return data

def calculate_std_dev(slam_data_x, slam_data_y, ground_truth_data_x, ground_truth_data_y):
    # вычисление разницы между данными ground truth и данными SLAM для X и Y
    differences_x = []
    differences_y = []
    for i in range(len(slam_data_x)):
        diff_x = slam_data_x[i] - ground_truth_data_x[i]
        differences_x.append(diff_x)
        diff_y = slam_data_y[i] - ground_truth_data_y[i]
        differences_y.append(diff_y)
    # вычисление среднее значение разницы для X и Y
    mean_x = sum(differences_x) / len(differences_x)
    mean_y = sum(differences_y) / len(differences_y)
    # вычисление сумму квадратов разностей для X и Y
    ssd_x = sum([(x - mean_x) ** 2 for x in differences_x])
    ssd_y = sum([(y - mean_y) ** 2 for y in differences_y])
    # вычисление СКО для X и Y
    std_dev_x = math.sqrt(ssd_x / (len(differences_x) - 1))
    std_dev_y = math.sqrt(ssd_y / (len(differences_y) - 1))
    return std_dev_x, std_dev_y

def file_rider(ground_truth_file, slam_data_file):
    # чтение данных из файлов
    ground_truth_data = read_csv(ground_truth_file)
    slam_data = read_csv(slam_data_file)
    return ground_truth_data, slam_data

def main():
    # задаем имена файлов в домашней директории
    ground_truth_file = os.path.expanduser('~/ground_truth_listener.csv')
    slam_data_file = os.path.expanduser('~/tf_map_base_listener.csv')

    # читаем данные из файлов
    ground_truth_data, slam_data = file_rider(ground_truth_file, slam_data_file)

    # разделение координат X и Y
    slam_data_x = [x[0] for x in slam_data]
    slam_data_y = [x[1] for x in slam_data]
    ground_truth_data_x = [x[0] for x in ground_truth_data]
    ground_truth_data_y = [x[1] for x in ground_truth_data]

    # вычисление значений СКО для X и Y
    std_dev_x, std_dev_y = calculate_std_dev(slam_data_x, slam_data_y, ground_truth_data_x, ground_truth_data_y)

    # вывод значений СКО для X и Y
    print("Standard deviation for X:", std_dev_x)
    print("Standard deviation for Y:", std_dev_y)

    # построение данных для ground truth и SLAM
    plt.plot(
            ground_truth_data_x,
            ground_truth_data_y,
            linestyle='-',
            color='black',
            label='Ground Truth Data'
            )
    plt.plot(
            slam_data_x,
            slam_data_y,
            linestyle='--',
            color='black',
            label='SLAM Data'
            )
    plt.legend()
    plt.show()

    # построение данных по координате X для ground truth и SLAM
    plt.plot(
            ground_truth_data_x,
            linestyle='-',
            color='black',
            label='Ground Truth Data'
            )
    plt.plot(
            slam_data_x,
            linestyle='--',
            color='black',
            label='SLAM Data'
            )
    plt.legend()
    plt.title('X Coordinate Data')
    plt.show()

    # построение данных по координате Y для ground truth и SLAM
    plt.plot(
            ground_truth_data_y,
            linestyle='-',
            color='black',
            label='Ground Truth Data'
            )
    plt.plot(
            slam_data_y,
            linestyle='--',
            color='black',
            label='SLAM Data'
            )
    plt.legend()
    plt.title('Y Coordinate Data')
    plt.show()

    # построение графика отклонения SLAM от Ground Truth для X
    x_error = [(gt - slam) for gt, slam in zip(ground_truth_data_x, slam_data_x)]
    plt.plot(
            x_error,
            linestyle='-',
            color='black',
            label='X Error'
            )
    plt.plot(
            [0, len(x_error)],
            [0, 0],
            linestyle='--',
            color='black',
            label='Expected value'
            )
    x_std_dev = np.std(x_error)
    plt.fill_between(
                    range(len(x_error)),
                    [x_std_dev]*len(x_error),
                    [-x_std_dev]*len(x_error),
                    alpha=0.3,
                    color='black',
                    label='STD'
                    )
    plt.legend()
    plt.title('SLAM Error (X Coordinate)')
    plt.show()

    # построение графика отклонения SLAM от Ground Truth для Y
    y_error = [(gt - slam) for gt, slam in zip(ground_truth_data_y, slam_data_y)]
    plt.plot(
            y_error,
            linestyle='-',
            color='black',
            label='Y Error'
            )
    plt.plot(
            [0, len(x_error)],
            [0, 0],
            linestyle='--',
            color='black',
            label='Expected value'
            )
    y_std_dev = np.std(y_error)
    plt.fill_between(
                    range(len(y_error)),
                    [y_std_dev]*len(y_error),
                    [-y_std_dev]*len(y_error),
                    alpha=0.3,
                    color='black',
                    label='STD'
                    )
    plt.legend()
    plt.title('SLAM Error (Y Coordinate)')
    plt.show()

if __name__ == '__main__':
    main()