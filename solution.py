import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest as ztest


chat_id = 409995141 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:

  score, pval = ztest([x_success, y_success], [x_cnt, y_cnt])
  bool_solution = True
  print(pval)

  if pval < 0.02:
    bool_solution = True
  else:  
    bool_solution = False

  return bool_solution
