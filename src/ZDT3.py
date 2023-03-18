import numpy as np

class ZDT3:

    N = 30

    def _g(X):
        return 1 + 9/(ZDT3.N-1)*np.sum(X[1:])

    def _h(x_1, g_of_X):
        return 1 - np.sqrt(x_1/g_of_X) - x_1 * np.sin(10 * np.pi * x_1) / g_of_X

    def evaluate(X):
        assert X.shape == (30,)
        output = np.empty(2, dtype=np.float32)

        output[0] = X[0]

        g_of_x = ZDT3._g(X)

        output[1] = g_of_x * ZDT3._h(X[0], g_of_x)

        return output
