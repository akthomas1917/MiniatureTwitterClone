from twitter import *
from datetime import datetime

login = {"akthomas19":"twitter!", "YbDrummer":"flapadoodle7", "Jarin_R":"Jarin@0107"}

codes = {"akthomas19":['2337287593-RjMQdHMvXBn12RoleIqZdHFvpaS7n12rqs7D7JW', '9AnUM8eQycAMQZzRWlGl0gxLKkvQme2jeXVJ7WWBj69Mi', 'zV6g6E7gtqKGScetvNwrXMioF', 'gppjfGNQKyLts6BssGda7enY1hAtE4mbYMH0LVdfmY8u9az76L'],
         "YbDrummer":['2785066548-KLEuHtpe2l6vbLCRPcoAbUjBcAUVQwvt2VeUYXa', '5MkvGsCrPJq8eFwGNlltV0DOR4SJZ0AXGppOd07NCkROo', 'nsyZelbOQhfZuGn7WAZtNfKLa', 'Wpa5ifEFl9t5EGwccOPdwoOarglo1akmQkiDejqF3wM68ZbiSG'],
         "Jarin_R": ['4389968475-hn8Ss54SGz6Ngtnq9Jc8xsmylUE4cnvdyyoHiXG', 'PIzV9orFTJfmfsEOEj1Dbes1m63qNC3XunyJSQoYuOia4', 'mrTcM21barL0cu7tnhDAAts3X', 'mqYXqZVAg8rCS4mlOnSALzQVF82c0FOzsDImweNh2agbxOK6Ld']
         }
#codes values are ordered access_token, access_token_secret, consumer_key, consumer_secret

print("Welcome to PyTweet! PyTweet allows a user to send out a tweet using a Python script.")
print("Please enter your Twitter username and password.")

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

validate = False
while validate == False:

    username = input("Username: ")
    password = input("Password: ")

    if(login[username] == password):
        print("Successful login!")

        usercodes = codes[username]
        access_token = usercodes[0]
        access_token_secret = usercodes[1]
        consumer_key = usercodes[2]
        consumer_secret = usercodes[3]

        validate = True

    else:
        print("That username/password isn't recognized. Please try again.")

pytweet = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

stop = False

while stop == False:
    tweet = input("Compose your tweet: ")

    pytweet.statuses.update(status=tweet)

    now = datetime.now()
    currentMinute = now.minute
    if(now.minute < 10):
        currentMinute = "0" + str(now.minute)

    if(now.hour > 12):
        time = str((now.hour-12)) + ":" + str(currentMinute) + "PM"
    elif(now.hour == 12):
        time = str((now.hour)) + ":" + str(currentMinute) + "PM"
    else:
        time = str((now.hour)) + ":" + str(currentMinute) + "AM"

    date = (str(now.month) + "/" + str(now.day) + "/" + str(now.year))

    print("'" + tweet + "'" + " successfully tweeted at " + time + " on " + date + ".")

    end = input("Do you want to tweet again? (y|n)")
    if end == 'n':
        stop = True
        print("Thank you for trying PyTweet! The program has terminated.")
    else:
        continue

###Andrew Codes###
# Access token & access token secret
# 2337287593-RjMQdHMvXBn12RoleIqZdHFvpaS7n12rqs7D7JW (Access token)
# 9AnUM8eQycAMQZzRWlGl0gxLKkvQme2jeXVJ7WWBj69Mi (Access token secret)
# Consumer API keys
# mrTcM21barL0cu7tnhDAAts3X (Consumer API key)
# gppjfGNQKyLts6BssGda7enY1hAtE4mbYMH0LVdfmY8u9az76L (Consumer API key secret)

###Avi Codes###
# Access token & access token secret
# 2785066548-KLEuHtpe2l6vbLCRPcoAbUjBcAUVQwvt2VeUYXa (Access token)
# 5MkvGsCrPJq8eFwGNlltV0DOR4SJZ0AXGppOd07NCkROo (Access token secret)
# Consumer API keys
# nsyZelbOQhfZuGn7WAZtNfKLa (API key)
# Wpa5ifEFl9t5EGwccOPdwoOarglo1akmQkiDejqF3wM68ZbiSG (API secret key)

###Jarin Codes###
# Access token & access token secret
# 4389968475-hn8Ss54SGz6Ngtnq9Jc8xsmylUE4cnvdyyoHiXG (Access token)
# PIzV9orFTJfmfsEOEj1Dbes1m63qNC3XunyJSQoYuOia4 (Access token secret)
# Consumer API keys
# mrTcM21barL0cu7tnhDAAts3X (API key)
# mqYXqZVAg8rCS4mlOnSALzQVF82c0FOzsDImweNh2agbxOK6Ld (API secret key)

