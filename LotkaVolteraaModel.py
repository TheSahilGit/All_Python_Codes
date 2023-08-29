import matplotlib.pyplot as plt
import numpy as np
import math
import csv


def prey_function(prey, pred):
    a = 2 / 3
    b = 4 / 3
    return a * prey - b * prey * pred


def pred_function(prey, pred):
    m = 1
    b = 4 / 3
    e = 3 / 4
    return e * b * prey * pred - m * pred


def euler_loop(prey, pred):
    h = 0.01
    t = 0
    file = open("LVModel.txt", "w+")
    for i in range(5000):
        prey = prey + h * prey_function(prey, pred)
        pred = pred + h * pred_function(prey, pred)
        t = i
        csv.writer(file).writerow([prey, pred, t])
    file.close()


def plot_loop1():
    euler_loop(1, 1)
    data = np.loadtxt("LVModel.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]

    plt.plot(time, prey_num, label="Prey Population")
    plt.plot(time, pred_num, label="Predator Population")
    plt.legend()
    plt.grid()
    plt.title("Lotka Volterra Model\n" + "Predator Population & Prey Population vs time graph")
    plt.xlabel("Time")
    plt.ylabel("Population of Prey and Predator")


def plot_loop2(x, y):
    data = np.loadtxt("LVModel.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]
    plt.plot(pred_num, prey_num, label="Initial (Predator,Prey): " + str(x) + "," + str(y))
    # plt.title("Lotka Volterra Model without Limit Prey")
    plt.legend()


def plot_loop3(x, y):
    data = np.loadtxt("LVModel.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]
    plt.plot(pred_num, prey_num, label="Without Limit Prey ")
    plt.legend()


def diff_phase_plot_loop():
    euler_loop(0.9, 0.9)
    plot_loop2(0.9, 0.9)

    euler_loop(1., 1.)
    plot_loop2(1., 1.)

    euler_loop(1.19, 1.11)
    plot_loop2(1.19, 1.11)

    euler_loop(1.19, 1.15)
    plot_loop2(1.19, 1.15)

    plt.grid()

    plt.title("Lotka Volterra Model\n" + "Phase Space Plot")
    plt.xlabel("Predator Population")
    plt.ylabel("Prey Population")


'''
##### Incomplete######
##### Extended LV MODEL ######

b = [[1., 1.09, 1.52, 0.], [0., 1., 0.44, 1.36], [2.33, 0., 1., 0.47], [1.21, 0.51, 0.35, 1.]]
a = [1., 0.72, 1.53, 1.27]
h = 0.01
p = [0, 0, 0, 0]


def extendedLV_function(i, p):
    s = [0, 0, 0, 0]
    for j in range(4):
        s[j] = s[j] + b[[i][j]] * p[j]
    return a[i] * p[i] * (1 - s)


file = open("ExtendenLV.txt", "w+")
for i in range(4):
    p[i] = p[i] + h * extendedLV_function(i, p)
    csv.writer(file).writerow(p[1], p[2], p[3], p[4])
'''


#### LV with Prey Limit ####

def prey_limit_function(prey, pred, k):
    a = 2 / 3
    b = 4 / 3
    return a * prey * (1 - prey / k) - b * prey * pred


def euler_loop_prey_limit(prey, pred, k):
    h = 0.01
    t = 0
    filetwo = open("LVModel_prey_limit.txt", "w+")
    for i in range(5000):
        prey = prey + h * prey_limit_function(prey, pred, k)
        pred = pred + h * pred_function(prey, pred)
        t = i
        csv.writer(filetwo).writerow([prey, pred, t])
    filetwo.close()


## This loop is  for Predator Population/Prey Population vs time graph for a particular carrying capacity ##
def limit_plot_loop1(k):
    euler_loop_prey_limit(1, 1, k)
    data = np.loadtxt("LVModel_prey_limit.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]

    plt.plot(time, prey_num, label="Prey Population")
    plt.plot(time, pred_num, label="Predator Population")
    plt.legend()
    plt.grid()
    plt.suptitle("Lotka Volterra Model for Prey Limit\n" + "Predator Population & Prey Population vs time graph")
    plt.xlabel("Time")
    plt.ylabel("Population of Prey and Predator")
    plt.title("Carrying Capacity K=" + str(k))


def limit_plot_loop2(x, y):
    data = np.loadtxt("LVModel_prey_limit.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]
    plt.plot(pred_num, prey_num, label="Initial (Predator,Prey): " + str(x) + "," + str(y))
    plt.legend()


def limit_plot_loop3(x, y):
    data = np.loadtxt("LVModel_prey_limit.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]
    plt.plot(pred_num, prey_num, label="With Limit Prey")
    plt.legend()


## This loop is for Predator Population/Prey Population vs time graph for different Carrying Capacity in four differnt subplots ##
def limit_subplot_loop(min_k, max_k):
    n = 0
    interval = (max_k - min_k) / 4
    for k in np.arange(min_k, max_k, interval):
        n = n + 1
        plt.subplot(2, 2, n)
        limit_plot_loop1(k)
        plt.subplots_adjust(0.12, 0.11, 0.90, 0.88, 0.29, 0.47)


## This loop is for phase plots:  ##
def limit_diff_phase_plot_loop(k):
    euler_loop_prey_limit(0.5, 0.5, k)
    limit_plot_loop2(0.5, 0.5)


def limit_diff_phase_plot_loop2(k):
    euler_loop_prey_limit(0.5, 0.5, k)
    limit_plot_loop3(0.5, 0.5)

    '''euler_loop_prey_limit(1.0, 1.0)
    limit_plot_loop2(1.0, 1.0)

    euler_loop_prey_limit(1.2, 1.2)
    limit_plot_loop2(1.2, 1.2)'''

    plt.grid()

    plt.title("Phase Space Plot for\n" + "k=" + str(k))
    plt.xlabel("Predator Population")
    plt.ylabel("Prey Population")


'''def euler_loop_prey_limit2(prey_in,pred_in):
    h = 0.01
    t = 0
    filetwo = open("LVModel_prey_limit.txt", "w+")
    for k in np.arange(1, 50, 0.5):
        prey=prey_in
        pred=pred_in
        for i in range(5000):
            prey = prey + h * prey_limit_function(prey, pred, k)
            pred = pred + h * pred_function(prey, pred)
            t = i
            csv.writer(filetwo).writerow([prey, pred, t, k])
    filetwo.close()

def limit_plot_loop3(prey_in, pred_in):
    euler_loop_prey_limit2(prey_in, pred_in)
    data = np.loadtxt("LVModel_prey_limit.txt", delimiter=',')
    prey_num = data[:, 0]
    pred_num = data[:, 1]
    time = data[:, 2]
    k=data[:,3]
    plt.plot(time,prey_num, '.')
    plt.plot(time, pred_num, '.')'''


#### This Loop plots 4 subplots of phase potrais of both limit prey and non limit prey for four different Carrying Capacity(k) ####
def limit_nonlimit_subplot_loop(k_min, k_max):
    interval = (k_max - k_min) / 4
    n = 0
    for k in np.arange(k_min, k_max, interval):
        n = n + 1
        plt.subplot(2, 2, n)
        euler_loop(0.5, 0.5)
        plot_loop3(0.5, 0.5)
        limit_diff_phase_plot_loop2(k)
    plt.subplots_adjust(0.12, 0.11, 0.90, 0.88, 0.29, 0.60)
    plt.suptitle("Phase Space Plots for both Limit Prey and Normal LV for different k values")


limit_subplot_loop(1, 4)
'''plt.savefig("ssss.png", dpi=500, facecolor='w', edgecolor='w',
            orientation='landscape', papertype='letter', format=None,
            transparent=False, bbox_inches=None, pad_inches=0.1,
            metadata=None)'''
plt.show()
