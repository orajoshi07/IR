import tweepy 
from tkinter import * 
from time import sleep
from datetime import datetime
from textblob import TextBlob 
import matplotlib.pyplot as plt 
consumer_key = 'oEtFa5rcUFKQ0c8OjmAbGUu54'
consumer_secret = 'Ssw024U1kHBlrOxmUbYZx8ZX4rDJam9VRS4T8cKFPzJ2mmElQl'
access_token = '700594962556014592-ReVsnL46ioYOgrecXmoVgQ3dG3Ukn5H'
access_token_secret = 'JPlFMCFifxFXSXmqj3qtB6vp4kUodyOxc38y8RmpKX20x'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print ('G.N.Khalsa College')
root = Tk()
label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)
label2 = Label(root, text="Sample Size")
E2 = Entry(root, bd =5)
def getE1():
    return E1.get()
def getE2():
    return E2.get()
def getData():
    getE1()
    keyword = getE1()
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    #Where the tweets are stored to be plotted
    polarity_list = []
    numbers_list = []
    number = 1
    for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(numberOfTweets):
        try:
            analysis = TextBlob(tweet.text)
            analysis = analysis.sentiment
            polarity = analysis.polarity
            polarity_list.append(polarity)
            numbers_list.append(number)
            number = number + 1
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    axes = plt.gca()
    axes.set_ylim([-1, 2])
    plt.scatter(numbers_list, polarity_list)
    averagePolarity = (sum(polarity_list))/(len(polarity_list))
    averagePolarity = "{0:.0f}%".format(averagePolarity * 100)
    time  = datetime.now().strftime("At: %H:%M\nOn: %m-%d-%y")
    plt.text(0, 1.25, "Average Sentiment:  " + str(averagePolarity) + "\n" + time, fontsize=12, bbox = dict(facecolor='none', edgecolor='black', boxstyle='square, pad = 1'))
    plt.title("Sentiment of " + keyword + " on Twitter")
    plt.xlabel("Number of Tweets")
    plt.ylabel("Sentiment")
    plt.show()
submit = Button(root, text ="Submit", command = getData)
label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)
root.mainloop()
