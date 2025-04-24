import numpy as np

class LinearRegression:
    def __init__(self):
        self.x = np.array([1, 2, 3, 4, 5])
        self.y = np.array([3, 5, 7, 9, 11])
        self.LinearRegression(self.x, self.y)

    def LinearRegression(self, x, y):
        n = len(x)
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xy = np.sum((x[i]*y[i] for i in range(n)))
        sum_sq_x = np.sum(x[i]**2 for i in range(n))
        sum_x_square = np.sum(self.x ** 2)

        numerator = n * sum_xy - sum_x *sum_y
        denominator = n * sum_x_square - (sum_x **2)
        slope = numerator/denominator
        print(slope)

        intercept = (sum_y - slope*sum_x)/n
        print(intercept)


        targetValue = int(input("Enter target Value"))
        predictedValue = slope*targetValue + intercept
        print(predictedValue)
        print(f"for targerValue  {targetValue} prediction is  {predictedValue} .")


if __name__ == '__main__':
    LinearRegression()