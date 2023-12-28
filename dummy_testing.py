
# names = [
#     "Fares",
#     "Mohamed",
#     "Ahmed",
#     "Ali",
#     "Omar",
#     "Khaled",
#     "Hassan",
#     "Hussein",
#     "Abdallah",
#     "Ranim",
#     "Nour",
#     "Nada",
#     "Ahlam",
#     "Hala",
#     "Hind",
# ]

# def getLawyers(index):
#     random_name = names[random.randint(0, len(names) - 1)]
#     random_reviews_number = random.randint(0, 100)
#     return {
#         "id": index,
#         "name": random_name,
#         "email": f"{random_name}{index}@gmail.com",
#         "rating": index % 5 + 0.5,
#         "reviews": random_reviews_number,
#         }


# db_lawyers : List = [ getLawyers(i) for i in range(100)]

# def get_reviews(index):
#     random_lawyer = random.randint(0, 99)
#     return {
#         "id": index,
#         "lawyer_id": random_lawyer,
#         "review": " i like : " + db_lawyers[random_lawyer]["name"],
#         "rating": index % 5 + 0.5,
#         }

# db_reviews : List = [ get_reviews(i) for i in range(100)] 
# def get_review_of_lawyer(index):
#     try :
#         return list(filter(lambda review: review["lawyer_id"] == index, db_reviews))
        
#     except:
#         raise HTTPException(
#             status_code=404, detail="lawyer not found"
#         )
