class Utils :
    def calculate_average_rating(prev_ratings:list[float] , new_rating:int):
        if prev_ratings == 0 :
            return new_rating
        else :
            return (sum(prev_ratings) + new_rating) / (len(prev_ratings) + 1)
        


 