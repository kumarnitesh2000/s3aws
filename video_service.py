import json
import base64
import requests
import datetime

def unique_id():
  now=datetime.datetime.now()
  s=str(now)
  print(s)
  date=s[:10]
  #print(date)
  date_lis=date.split("-")[:]
  print(date_lis)
  time=s[11:19]
  time_lis=time.split(":")[:]
  print(time_lis)
  #date_lis,time_lis
  
  return{
    "date_Id":"/".join(date_lis),
    "time_Id":"/".join(time_lis)
  }

f=open("vid4.mp4","rb")
print(len(f.read()))
encode_byte=base64.b64encode(f.read())
vid_file=encode_byte.decode("utf-8")

is_Video=False
if len(f.read())>10:
  is_Video=True
hour_minute_sec_mili=unique_id()['time_Id']
date_month_year=unique_id()['date_Id']
data={
"is_Video":is_Video,
"vid_file":vid_file,
"hour_minute_sec_mili":hour_minute_sec_mili,
"date_month_year":date_month_year,

}
url="https://ybmldjafw8.execute-api.us-east-1.amazonaws.com/test/vid"
r=requests.post(url,data=json.dumps(data))

print(r.json())

f.close()
