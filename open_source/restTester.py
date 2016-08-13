import requests

def runRestTester():
    restUrl = input("Please write the url: ")
    if len(restUrl.split('://')) < 2:
        restUrl = 'http://' + restUrl

    #localhost/restexample/rest.php

    dataCount = int(input("How much data you want to send?"))
    i = 0
    rest = dict()
    while i < dataCount:
        restKey = input("Please write rest key:")
        restVal = input("Please write rest value:")
        rest[restKey] = restVal
        i += 1
    print("Choose your methods.\n [1]Get\n [2]Post\n [3]Head\n [4]put\n [5]patch\n [6]Delete\n ")
    method = input("Please write your method.")
    def f(method):
        return {
            '1': requests.get(restUrl, data=rest),
            '2': requests.post(restUrl, data=rest),
            '3': requests.head(restUrl, data=rest),
            '4': requests.put(restUrl, data=rest),
            '5': requests.patch(restUrl, data=rest),
            '6': requests.delete(restUrl, data=rest),
        }[method]

    response = f(method)
    print("Response:", response, "\n", "Text:", response.text)
tryagain = 'y'
while tryagain != 'n':
    runRestTester()
    tryagain = input('Try again? [y] or [n]')
input("Please click any key to exit.")
