import requests
import datetime
from requests import sessions
from requests.sessions import session
date=datetime.date.today()
date=str(date).split('-')
date=date[::-1]
date='-'.join(date)
def get_list():
    req= requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=392&date='+date)
    data = req.json()
    data=dict(data)['sessions']
    num=1
    fin={}
    for i in range(len(data)):
        if data[i]['fee_type']=='Free' and data[i]['vaccine']=='COVISHIELD':
            if data[i]['available_capacity_dose2']>0:
                fin[num]=str(data[i]['name'])
                num+=1
    for i,j in fin.items():
        print(i,j)
    val=str(input('Choose the number of the vaccination center '))
    return fin[int(val)]

