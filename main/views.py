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

    ethkovan = alldata[1][0]
    ethkovan_id = alldata[1][1]
    ethkovan_logo = alldata[1][2]
    ethkovan_status = alldata[1][3]

    maticmainnet = alldata[2][0]
    maticmainnet_id = alldata[2][1]
    maticmainnet_logo = alldata[2][2]
    maticmainnet_status = alldata[2][3]

    maticmumbai = alldata[3][0]
    maticmumbait_id = alldata[3][1]
    maticmumbai_logo = alldata[3][2]
    maticmumbai_status = alldata[3][3]

    avalanchemainnet = alldata[4][0]
    avalanchemainnet_id = alldata[4][1]
    avalanchemainnet_logo = alldata[4][2]
    avalanchemainnet_status = alldata[4][3]

    avalanchetestnet = alldata[5][0]
    avalanchetestnet_id = alldata[5][1]
    avalanchetestnett_logo = alldata[5][2]
    avalanchetestnet_status = alldata[5][3]

    bscmainnet = alldata[6][0]
    bscmainnet_id = alldata[6][1]
    bscmainnet_logo = alldata[6][2]
    bscmainnet_status = alldata[6][3]

    bsctestnet = alldata[7][0]
    bsctestnet_id = alldata[7][1]
    bsctestnet_logo = alldata[7][2]
    bsctestnet_status = alldata[7][3]

    moonbeammoonbasealpha = alldata[8][0]
    moonbeammoonbasealpha_id = alldata[8][1]
    moonbeammoonbasealpha_logo = alldata[8][2]
    moonbeammoonbasealpha_status = alldata[8][3]

    moonbeammoonriver = alldata[9][0]
    moonbeammoonriver_id = alldata[9][1]
    moonbeammoonriver_logo = alldata[9][2]
    moonbeammoonriver_status = alldata[9][3]

    rskmainnet = alldata[10][0]
    rskmainnet_id = alldata[10][1]
    rskmainnet_logo = alldata[10][2]
    rskainnet_status = alldata[10][3]

    arbitrummainnet = alldata[11][0]
    arbitrummainnet_id = alldata[11][1]
    arbitrummainnet_logo = alldata[11][2]
    arbitrummainnet_status = alldata[11][3]

    arbitrumtestnet = alldata[12][0]
    arbitrumtestnet_id = alldata[12][1]
    arbitrumtestnet_logo = alldata[12][2]
    arbitrumtestnet_status = alldata[12][3]

    fantommainnet = alldata[13][0]
    fantommainnet_id = alldata[13][1]
    fantommainnet_logo = alldata[13][2]
    fantommainnet_status = alldata[13][3]

    fantomtestnet = alldata[14][0]
    fantomtestnet_id = alldata[14][1]
    fantomtestnet_logo = alldata[14][2]
    fantomtestnet_status = alldata[14][3]

    payload = {
        "ethmainnet" : ethmainnet,

    }

    return render(request, 'home.html', payload)


    # [['eth-mainnet', '1', 'https://www.covalenthq.com/static/images/icons/display-icons/ethereum-eth-logo.png', True], 
    # ['eth-kovan', '42', 'https://www.covalenthq.com/static/images/icons/display-icons/ethereum-eth-logo.png', True], 
    # ['matic-mainnet', '137', 'https://www.covalenthq.com/static/images/icons/display-icons/polygon-matic-logo.png', True], 
    # ['matic-mumbai', '80001', 'https://www.covalenthq.com/static/images/icons/display-icons/polygon-matic-logo.png', True],
    #  ['avalanche-mainnet', '43114', 'https://www.covalenthq.com/static/images/icons/display-icons/avalanche-avax-logo.png', True],
    #   ['avalanche-testnet', '43113', 'https://www.covalenthq.com/static/images/icons/display-icons/avalanche-avax-logo.png', True], 
    #   ['bsc-mainnet', '56', 'https://www.covalenthq.com/static/images/icons/display-icons/binance-coin-bnb-logo.png', True], 
    #   ['bsc-testnet', '97', 'https://www.covalenthq.com/static/images/icons/display-icons/binance-coin-bnb-logo.png', True], 
    #   ['moonbeam-moonbase-alpha', '1287', 'https://www.covalenthq.com/static/images/icons/display-icons/moonbeam-logo.png', True],
    #    ['moonbeam-moonriver', '1285', 'https://www.covalenthq.com/static/images/icons/display-icons/moonriver.png', True],
    #     ['rsk-mainnet', '30', 'https://www.covalenthq.com/static/images/icons/display-icons/rsk-mainnet-logo.svg', True], 
    #     ['rsk-testnet', '31', 'https://www.covalenthq.com/static/images/icons/display-icons/rsk-mainnet-logo.svg', True],
    #      ['arbitrum-mainnet', '42161', 'https://www.covalenthq.com/static/images/icons/display-icons/arbitrum-mainnet-logo.svg', True],
    #       ['arbitrum-testnet', '421611', 'https://www.covalenthq.com/static/images/icons/display-icons/arbitrum-mainnet-logo.svg', True],
    #        ['fantom-mainnet', '250', 'https://www.covalenthq.com/static/images/icons/display-icons/fantom-ftm-logo.png', True],
    #         ['fantom-testnet', '4002', 'https://www.covalenthq.com/static/images/icons/display-icons/fantom-ftm-logo.png', True], 
    #         ['palm-mainnet', '11297108109', 'https://www.covalenthq.com/static/images/icons/display-icons/palm-mainnet-logo.svg', True],
    #          ['palm-testnet', '11297108099', 'https://www.covalenthq.com/static/images/icons/display-icons/palm-mainnet-logo.svg', True],
    #           ['klaytn-mainnet', '8217', 'https://www.covalenthq.com/static/images/icons/display-icons/klaytn-mainnet-logo.svg', True],
    #            ['heco-mainnet', '128', 'https://www.covalenthq.com/static/images/icons/display-icons/heco-mainnet-logo.svg', True],
    #             ['heco-testnet', '256', 'https://www.covalenthq.com/static/images/icons/display-icons/heco-testnet-logo.svg', True],
    #              ['nervos-polyjuice-testnet', '71393', 'https://www.covalenthq.com/static/images/icons/display-icons/nervos-polyjuice-testnet-logo.svg', True],
    #               ['axie-mainnet', '2020', 'https://www.covalenthq.com/static/images/icons/display-icons/axie-logo.svg', True],
    #                ['evmos-testnet', '9000', 'https://www.covalenthq.com/static/images/icons/display-icons/evmos-logo.svg', True],
    #                 ['astar-shiden', '336', 'https://www.covalenthq.com/static/images/icons/display-icons/astar-shiden-logo.svg', True],
    #                  ['iotex-mainnet', '4689', 'https://www.covalenthq.com/static/images/icons/display-icons/iotex-logo.svg', True],
    #                   ['iotex-testnet', '4690', 'https://www.covalenthq.com/static/images/icons/display-icons/iotex-logo.svg', True],
    #                    ['covalent-internal-network-v1', '1131378225', 'https://www.covalenthq.com/static/images/covalent-logomark.png', True]]