import requests
import json

netflix_cookie = "memclid=530dc900-255e-41dd-8abd-22e0b32694ce; clSharedContext=c353e5b3-5eae-4867-b2e6-ddee1a249602; nfvdid=BQFmAAEBEDp6Lm19BKzNOamNMsBnNt9g1Fm86vak6a8u35Oq4LClk0EjCJYie5TDMbmk2rr6RWplqKdgWg%2FJEeM11KY3D9VoSDybzuTpX55yYEaEdf6rjnZc1MngpTb%2F5lvZtJf%2FGYpwxCB4flBylNwklFUz8po8; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABSAucaBZpmVSB8CtjbcuQW2RtpO3AAhoOw.%26dt%3D1536612073491; NetflixId=v%3D2%26ct%3DBQAOAAEBEPXAc7Qw2CGhjoZIn32lmXmB0H4WQevxb45H0vzyglCNyRMDaSMTAtBUJwjgDz0MnBvK2H63CCLcW8cX4lyEaV1ZXmy4BCyaDZWS7ZI1hoPKIAz6Q8orVVsa62w2VPkd2HciL8pEocRVAoVgsYdEgYEBL83TQ1DbYT7UpuHbnv4S6QQQ2wFKcVu-IefIx3-kMo5Hf3yM3hd-WGVcwvAwtcMxXCUEfWvQFuDf-AyfgTWCO_PjjLkC4a1Wk67Ca5Wyi-d0n-Qa_V_U4TPhwxtLYqy3sDn_B3Bqx7A0RQoVHQ08SJaFUzRXY1ivAyaHftI0mMDe-884xTBI2k9TAyltjDryKC7Ls-XAtbwSJ5aLRSxUd9oGoymHms0AXvAi0fEo8PikOFdeIAY5hsG1jGbxH4JlSd8pZVqturY-4aFaYRSRin3kIroxFPVqxBFSMqZfwapKXmCykjdPIlucOqCjI-rE7JPEn6WF8ZwKzmJPktBpzerlPObh0DmoGKqj9VDGHxBsXTAibtgXJ6AWrfLwphdr3mUbpTekCTRCQoIHJT1t5_A3sPZ08_0hhpPcPC0KIhSaO_WxuuyczuEHawEvcclp0jMqEp0FITWPUU3ojNbhkABLBz53cnXTGYbSm7l8xT8q%26bt%3Ddbl%26ch%3DAQEAEAABABSKYNSvDj1w8oy4Qv8m-blOxgFzSYqWCnY.%26mac%3DAQEAEAABABS-HVXSwY-ShcbRhdumoToJ2EwHl97m2Bw.; profilesNewSession=0; cL=1536614242061%7C153661207338410534%7C153661207320198106%7C%7C7%7CULAFHOQJZVHVBKG4HLWPDKA4TI; pas=%7B%22supplementals%22%3A%7B%22muted%22%3Atrue%7D%7D; playerPerfMetrics=%7B%22uiValue%22%3A%7B%22throughput%22%3A7590%7D%2C%22mostRecentValue%22%3A%7B%22throughput%22%3A7922%7D%7D"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
'Cookie':netflix_cookie,
'Accept':'application/json, text/javascript, */*',
'Accept-Language':'en-GB,en;q=0.5',
'Accept-Encoding':'gzip, deflate, br',
'Content-Type':'application/json',
'DNT':'1',
'Referer':'https://www.netflix.com/search?q=breaking%20bad'}

genres='0,"to":1'
rmax='5'
base='[["newarrivals",{"from":'+genres+'},{"from":0,"to":'+rmax+'},["title","availability"]],["newarrivals",{"from":'+genres+'},{"from":0,"to":'+rmax+'},"boxarts","_342x192","jpg"]]';
data='{"paths":'+base+'}'

#use the pathEvaluator from your session here
url='https://www.netflix.com/api/shakti/v3e100fda/pathEvaluator?drmSystem=widevine&isWatchlistEnabled=false&isShortformEnabled=false&isVolatileBillboardsEnabled=false&falcor_server=0.1.0&withSize=true&materialize=true';

response=requests.post(url,data=data,headers=headers)

rjson=response.json()

print(rjson)

'''
videos=rjson['value']['videos']
for vid in videos:
    if vid.isnumeric():
        vo=videos[vid]
        title=vo['title']
        boxart=vo['boxarts']['_342x192']['jpg']['url']
        isplayable=vo['availability']['isPlayable']
        retjson='{"netflixid":"'+str(vid)+'","title":"'+str(title)+'","playable":'+str(isplayable)+',"boxart":"'+str(boxart)+'"}';
        print (retjson)
'''