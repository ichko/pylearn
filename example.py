import matplotlib.pyplot as plt
import numpy as np
import math

from pylearn import high_order_model
from pylearn.data_loader import parse_data
from pylearn.space_transform import full_polynomial_mapper


# Logistic regression example
lr = high_order_model.PolynomialLogisticRegression()
lr.learning_rate = 50
lr.max_iterations = 800

X_lo, y_lo = parse_data('example_data/data2.txt')
y_lo = [int(y) for y in y_lo]

mapper = full_polynomial_mapper(12, 2)
predict = lr.fit(X_lo, y_lo, mapper)

x = y = np.arange(-1.5, 1.5, 0.08)
X, Y = np.meshgrid(x, y)
Z = [list(zip(rowX, rowY)) for rowX, rowY in zip(X, Y)]
Z = [[lr.unthresholded(list(data)) for data in row] for row in Z]

levels = [-5000, -0.05, 0, 0.015, 5000]
plt.contourf(X, Y, Z, cmap=plt.cm.winter, levels=levels)

colormap = np.array(['cyan', 'red'])
for i, row in enumerate(X_lo):
    plt.scatter(row[0], row[1], s=50, c=colormap[y_lo[i]])

# plt.plot([i / 20 for i in range(len(lr.error_log))],
#         [i * 500 for i in lr.error_log])

plt.show()


'''
# Linear regression example
lr = linear_model.LinearRegression()
predict = lr.fit(example_data.X_re, example_data.y_re)

test_data = [-100, 100]
test_results = [predict([x]) for x in test_data]

plt.plot(test_data, test_results)
plt.plot(example_data.X_re, example_data.y_re, 'ro')
plt.show()

example_data.X_re = [[-x[0] - 100] for x in example_data.X_re]
example_data.y_re = [y - 100 for y in example_data.y_re]


# Polynomial regression example
lr = high_order_model.PolynomialRegression()
predict = lr.fit(example_data.X_re,
                 example_data.y_re, [lambda x, _: x[0] ** 4])

test_data = list(np.arange(-150, -50, 5))
test_results = [predict([x]) for x in test_data]

plt.plot(test_data, test_results)
plt.plot(example_data.X_re, example_data.y_re, 'ro')
plt.show()
'''
