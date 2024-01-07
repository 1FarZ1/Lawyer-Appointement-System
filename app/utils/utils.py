import math
class Utils :
    def calculate_rating(prev_ratings:list[float] , new_rating:int):
        if prev_ratings == 0 :
            return new_rating
        else :
            return round((sum(prev_ratings)+new_rating)/(len(prev_ratings)+1)*2)/2
        


 