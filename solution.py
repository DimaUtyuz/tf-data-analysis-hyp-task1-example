import numpy
import statsmodels.stats.proportion as p
from scipy.stats import chi2
from scipy.stats import laplace, norm


chat_id = 617910360 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    v = (x_success / x_cnt - y_success / y_cnt) * numpy.sqrt((x_cnt + y_cnt) * x_cnt * y_cnt / ((x_success + y_success) * (x_cnt + y_cnt - x_success - y_success)))
    q = norm.ppf(0.1)
    return v <= q

# print(solution(2, 1000, 50, 1000))
