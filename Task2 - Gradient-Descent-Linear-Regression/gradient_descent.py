import csv
import matplotlib.pyplot as plt

num = 0
points = [[], []]

with open("dataset.csv") as dataset:
    reader = csv.reader(dataset, delimiter=",")
    next(reader)
    
    for row in reader:
        points[0].append(float(row[0]))
        points[1].append(float(row[1]))
        num += 1
        

def hypothesis(theta0, theta1, x):
    return theta0 + theta1 * x


def cost(theta0, theta1):
    segma = 0
    for i in range(num):
        segma += (hypothesis(theta0, theta1, points[0][i]) - points[1][i]) ** 2
        
    return segma / (2 * num)


def gradient_descent(theta0, theta1, alpha):
    segma0 = 0
    segma1 = 0
    
    for i in range(num):
        segma0 += hypothesis(theta0, theta1, points[0][i]) - points[1][i]
        segma1 += (hypothesis(theta0, theta1, points[0][i]) - points[1][i]) * points[0][i]
        
    theta0 -= alpha * segma0 / num
    theta1 -= alpha * segma1 / num
    
    return theta0, theta1


def main():
    alpha = 0.0006
    theta0 = 0
    theta1 = 0
    
    for i in range(100000):
        theta0, theta1 = gradient_descent(theta0, theta1, alpha)
    print(cost(theta0, theta1), theta0, theta1)
    
    plt.plot(points[0], points[1], "x")
    result = [hypothesis(theta0, theta1, x) for x in points[0]]
    
    plt.plot(points[0], result, color="black")
    plt.show()
    
    
    
main()







