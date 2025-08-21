import sys
from pathlib import Path
filepath = Path(__file__)
file_dir = filepath.parent.parent
sys.path.append(str(file_dir))
from lesson_06.lesson_6 import is_student

from math import sqrt as square_root, pi, cos # 3
# from math import * # all
import sys as s
# import calculator
from calculator import add, multiply, PI
# Можна використовувати функції напряму
if __name__ == "__main__":
    result = square_root(16)
    pi_value = pi
    print(result, pi_value)
    cos_value = cos(0)
    print(cos_value)
    print(s.version)
    result = add(1, 2)
    print(result)
    mul = multiply(2, PI)
    print(mul)
    print(is_student)