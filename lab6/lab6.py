import numpy as np
x = [[1, 2], [1, 5], [1, 7], [1, 8]]
y = [1, 2, 3, 3]
x = np.array(x)
print(x.T)


def wtf(x, y):
    x = np.array(x)
    y = np.array(y)
    xd = x.T * x.I
    result = xd * y
    return result


print(wtf(x, y))
