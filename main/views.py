import requests
import json
import re
from datetime import datetime
from django.shortcuts import render

def getData():
    data_array = []

    url = "https://api.covalenthq.com/v1/chains/status/?quote-currency=USD&format=JSON&key=ckey_docs"
    x = requests.get(url)
    res = json.loads(x.text)
    data = res["data"]["items"]
    for each in data:
        name = each['name']
        chain_id = each['chain_id']
        logo_url = each['logo_url']
        time = each['synced_blocked_signed_at']
        
        time = time[11:][:-1]
        min = time.split(":")[1]

        date_time = datetime.strptime(time, "%H:%M:%S")
        current_time = datetime.now().strftime("%H:%M:%S")
        current_time = current_time.split(':')[1]
        current_time = int(current_time) + 30
        if (current_time > 60):
            current_time = current_time - 60

        if((current_time - int(min)) < 59 ):
            status = True
        else:
            status = False

        each_chain = [name, chain_id, logo_url, status]
        data_array.append(each_chain) 

    return data_array

def home(request):
    alldata = getData()
    ethmainnet = alldata[0][0]
    ethmainnet_id = alldata[0][1]
    ethmainnet_logo = alldata[0][2]
    ethmainnet_status = alldata[0][3]

    payload = {
        "ethmainnet" : ethmainnet,

    }

    return render(request, 'home.html', payload)