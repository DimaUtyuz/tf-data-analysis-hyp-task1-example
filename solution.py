import statsmodels.stats.proportion as p


chat_id = 617910360 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    _, pval = p.proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
    return pval <= 0.1
