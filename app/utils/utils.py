import datetime
import math
class Utils :
    def calculate_rating(prev_ratings:list[float] , new_rating:int):
        if prev_ratings == 0 :
            return new_rating
        else :
            return round((sum(prev_ratings)+new_rating)/(len(prev_ratings)+1)*2)/2
        
    def saveFileToUploads(image) -> dict:
        import os
        basePath = "uploads/" +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(" ", "_").replace(":", "-").replace(".", "-")
        imagePath = (f"{basePath}/{image.filename}")
        if not os.path.exists(basePath):
            os.makedirs(basePath)    
        with open(imagePath, "wb+") as file_object:
            file_object.write(image.file.read())    
        return {
            "info": f"file '{image.filename}' saved at '{imagePath}'",
            "path": imagePath
        }

        


 