
import math

class Linear_Regression:


    @staticmethod
    def mse(
            actual_value: list[int],
            predict_value: list[int]
    )->int:
        
        result = 0
        for i in range(1,len(actual_value)):
            result += (actual_value[i] - predict_value[i])**2

        result = math.sqrt(result/len(actual_value))
        
        return result

        
