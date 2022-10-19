# import time
# from plyer import notification
# import schedule


# # def get_today(id):

# #     response = dict()
# #     response["property"] = "Health"
# #     response["time"] = "9:00AM"
# #     response["message"] = "Check your heart rate"
# #     response["info"] = "Checking your heart rate in the morning is the best practise"
# #     return response

# # if __name__ == '__main__':
# # 	while True:

# def hr():
#     notification.notify(
#         title = "Check your heart rate",
#         message ="Checking your heart rate in the morning is the best practise.",
#         # app_icon = "path to your .ico file",
#         timeout= 10
#         )
#     #	time.sleep(6)
#     time.sleep(60*60)


# schedule.every().day.at("02:39").do(hr)

# while True:
 
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(1)