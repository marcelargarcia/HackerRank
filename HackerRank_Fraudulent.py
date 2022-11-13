#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
import statistics

def activityNotifications(expenditure, d):
    median = statistics.median(expenditure[0:d])
    notices = 0
    for i in range(d, len(expenditure)):
        if expenditure[i] >= median * 2:
            notices = notices + 1
        median = statistics.median(expenditure[i-d+1:i+1])
    return notices


if __name__ == '__main__':
    print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5],5))
    print(activityNotifications([10,20,30,40,50], 3))