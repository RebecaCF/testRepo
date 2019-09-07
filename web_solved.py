import csv
import os

# udemy_csv = "./resources/web_starter.csv"
udemy_csv = os.path.join(".","resources","web_starter.csv")

# We want the title, the price, the subscribers
# Reviews, percent of review, length
title = []
price = []
subscribers = []
reviews = []
reviews_percent = []
lenght = []

with open(udemy_csv, "r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#   test = next(csvreader)
    for row in csvreader:
        # add title
        title.append(row[1])
        # add price
        price.append(row[4])
        # add subscribers
        subscribers.append(row[5])
        # reviews
        reviews.append(row[6])
        # percent of reviews
        percent = round(int(row[6])/ int(row[5]),2)
        reviews_percent.append(percent)
        # lenght
        new_lenght = row[9].split(" ")
        lenght.append(float(new_lenght[0]))



# print(reviews_percent)
# print(test)

cleanCsv = zip(title, price, subscribers, reviews, reviews_percent, lenght)

outputFile = os.path.join("webFinal.csv")

with open(outputFile, "w", newline="\n") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title","Course Price", "Subscribers","Reviews",
    "Percent of Reviews", "Lenght of Course"])
    writer.writerows(cleanCsv)
