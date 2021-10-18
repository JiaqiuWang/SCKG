
import numpy as np



def softmax1(x):
    """构建softmax 函数：计算向量的v的softmax向量"""
    # 1.计算向量的指数值
    exp_v = np.exp(x)
    print("向量的指数值：\n", exp_v)
    print("向量求和np.sum():", np.sum(exp_v))
    softmax_v = exp_v / np.sum(exp_v)
    print("softmax_v:\n", softmax_v)


vec_1 = [1, 3, 5, 0, -1, 0.42]
vec_2 = [1, 2, 3]
softmax1(vec_1)
softmax1(vec_2)
print(8 * "*" * 8)


def softmax2(x):
    """构建一种数据值稳定的softmax函数"""
    x = x - np.max(x)  # 根据softmax函数的性质  softmax(x) = softmax(x + c), c为常数，c一般用-max(vec)来标识\

    print("x-max:\n", x)
    expv = np.exp(x)
    softmaxv = expv / np.sum(expv)
    print("softmax值：", softmaxv)


vec3 = [1000, 2000, 3000]
softmax2(vec3)
print(8 * "*" * 8)


def softmax3(x):
    """基于向量和矩阵的softmax值计算

    :argument
    x -- A N dimensional vector or M * N dimensional numpy matrix

    :return
    x -- You are allowed to modify x in-place
    """
    print("x:\n", x)
    print("origin shape:", x.shape, ", Type:", type(x), ", length-x.shape:", len(x.shape))

    if len(x.shape) > 1:
        # Matrix
        # minmax = lambda x: x - np.max(x)
        # x = np.apply_along_axis(minmax, 1, x)
        print("-max:\n", x, ", shape:", x.shape, ", type:", type(x))
        exp = lambda x: np.exp(x)
        x = np.apply_along_axis(exp, 1, x)
        print("exp:\n", x, ", shape:", x.shape, ", type:", type(x))
        denom = lambda x: x / np.sum(x)
        x = np.apply_along_axis(denom, 1, x)
        print("final_x:", x, ", shape:", x.shape, ", type:", type(x))

        pass
    else:
        # Vector 向量
        x_max = np.max(x)
        x = np.exp(x - np.max(x))
        x = x / np.sum(x)


vec4 = [[1, 2, 5],
        [4, 8, 10]]
np_vec4 = np.mat(vec4)
print("np_nec4-type:", type(np_vec4))
print("max-v:", np.max(vec4))
softmax3(np_vec4)



