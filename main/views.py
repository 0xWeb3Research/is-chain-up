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
    ethmainnet_id= alldata[0][1]
    ethmainnet_logo = alldata[0][2]
    ethmainnet_status = alldata[0][3]
    ethkovan = alldata[1][0]
    ethkovan_id= alldata[1][1]
    ethkovan_logo = alldata[1][2]
    ethkovan_status = alldata[1][3]
    maticmainnet = alldata[2][0]
    maticmainnet_id= alldata[2][1]
    maticmainnet_logo = alldata[2][2]
    maticmainnet_status = alldata[2][3]
    maticmumbai = alldata[3][0]
    maticmumbai_id= alldata[3][1]
    maticmumbai_logo = alldata[3][2]
    maticmumbai_status = alldata[3][3]
    avalanchemainnet = alldata[4][0]
    avalanchemainnet_id= alldata[4][1]
    avalanchemainnet_logo = alldata[4][2]
    avalanchemainnet_status = alldata[4][3]
    avalanchetestnet = alldata[5][0]
    avalanchetestnet_id= alldata[5][1]
    avalanchetestnet_logo = alldata[5][2]
    avalanchetestnet_status = alldata[5][3]
    bscmainnet = alldata[6][0]
    bscmainnet_id= alldata[6][1]
    bscmainnet_logo = alldata[6][2]
    bscmainnet_status = alldata[6][3]
    bsctestnet = alldata[7][0]
    bsctestnet_id= alldata[7][1]
    bsctestnet_logo = alldata[7][2]
    bsctestnet_status = alldata[7][3]
    moonbeammoonbasealpha = alldata[8][0]
    moonbeammoonbasealpha_id= alldata[8][1]
    moonbeammoonbasealpha_logo = alldata[8][2]
    moonbeammoonbasealpha_status = alldata[8][3]
    moonbeammoonriver = alldata[9][0]
    moonbeammoonriver_id= alldata[9][1]
    moonbeammoonriver_logo = alldata[9][2]
    moonbeammoonriver_status = alldata[9][3]
    rskmainnet = alldata[10][0]
    rskmainnet_id= alldata[10][1]
    rskmainnet_logo = alldata[10][2]
    rskmainnet_status = alldata[10][3]
    rsktestnet = alldata[11][0]
    rsktestnet_id= alldata[11][1]
    rsktestnet_logo = alldata[11][2]
    rsktestnet_status = alldata[11][3]
    arbitrummainnet = alldata[12][0]
    arbitrummainnet_id= alldata[12][1]
    arbitrummainnet_logo = alldata[12][2]
    arbitrummainnet_status = alldata[12][3]
    arbitrumtestnet = alldata[13][0]
    arbitrumtestnet_id= alldata[13][1]
    arbitrumtestnet_logo = alldata[13][2]
    arbitrumtestnet_status = alldata[13][3]
    fantommainnet = alldata[14][0]
    fantommainnet_id= alldata[14][1]
    fantommainnet_logo = alldata[14][2]
    fantommainnet_status = alldata[14][3]
    fantomtestnet = alldata[15][0]
    fantomtestnet_id= alldata[15][1]
    fantomtestnet_logo = alldata[15][2]
    fantomtestnet_status = alldata[15][3]
    palmmainnet = alldata[16][0]
    palmmainnet_id= alldata[16][1]
    palmmainnet_logo = alldata[16][2]
    palmmainnet_status = alldata[16][3]
    palmtestnet = alldata[17][0]
    palmtestnet_id= alldata[17][1]
    palmtestnet_logo = alldata[17][2]
    palmtestnet_status = alldata[17][3]
    klaytnmainnet = alldata[18][0]
    klaytnmainnet_id= alldata[18][1]
    klaytnmainnet_logo = alldata[18][2]
    klaytnmainnet_status = alldata[18][3]
    hecomainnet = alldata[19][0]
    hecomainnet_id= alldata[19][1]
    hecomainnet_logo = alldata[19][2]
    hecomainnet_status = alldata[19][3]
    hecotestnet = alldata[20][0]
    hecotestnet_id= alldata[20][1]
    hecotestnet_logo = alldata[20][2]
    hecotestnet_status = alldata[20][3]
    nervospolyjuicetestnet = alldata[21][0]
    nervospolyjuicetestnet_id= alldata[21][1]
    nervospolyjuicetestnet_logo = alldata[21][2]
    nervospolyjuicetestnet_status = alldata[21][3]
    axiemainnet = alldata[22][0]
    axiemainnet_id= alldata[22][1]
    axiemainnet_logo = alldata[22][2]
    axiemainnet_status = alldata[22][3]
    evmostestnet = alldata[23][0]
    evmostestnet_id= alldata[23][1]
    evmostestnet_logo = alldata[23][2]
    evmostestnet_status = alldata[23][3]
    astarshiden = alldata[24][0]
    astarshiden_id= alldata[24][1]
    astarshiden_logo = alldata[24][2]
    astarshiden_status = alldata[24][3]
    iotexmainnet = alldata[25][0]
    iotexmainnet_id= alldata[25][1]
    iotexmainnet_logo = alldata[25][2]
    iotexmainnet_status = alldata[25][3]
    iotextestnet = alldata[26][0]
    iotextestnet_id= alldata[26][1]
    iotextestnet_logo = alldata[26][2]
    iotextestnet_status = alldata[26][3]
    covalentinternalnetworkv1 = alldata[27][0]
    covalentinternalnetworkv1_id= alldata[27][1]
    covalentinternalnetworkv1_logo = alldata[27][2]
    covalentinternalnetworkv1_status = alldata[27][3]

    payload = {
   "ethmainnet" : ethmainnet,
    "ethmainnet_id" : ethmainnet_id,
    "ethmainnet_logo" : ethmainnet_logo,
    "ethmainnet_status" : ethmainnet_status,
    "ethkovan" : ethkovan,
    "ethkovan_id" : ethkovan_id,
    "ethkovan_logo" : ethkovan_logo,
    "ethkovan_status" : ethkovan_status,
    "maticmainnet" : maticmainnet,
    "maticmainnet_id" : maticmainnet_id,
    "maticmainnet_logo" : maticmainnet_logo,
    "maticmainnet_status" : maticmainnet_status,
    "maticmumbai" : maticmumbai,
    "maticmumbai_id" : maticmumbai_id,
    "maticmumbai_logo" : maticmumbai_logo,
    "maticmumbai_status" : maticmumbai_status,
    "avalanchemainnet" : avalanchemainnet,
    "avalanchemainnet_id" : avalanchemainnet_id,
    "avalanchemainnet_logo" : avalanchemainnet_logo,
    "avalanchemainnet_status" : avalanchemainnet_status,
    "avalanchetestnet" : avalanchetestnet,
    "avalanchetestnet_id" : avalanchetestnet_id,
    "avalanchetestnet_logo" : avalanchetestnet_logo,
    "avalanchetestnet_status" : avalanchetestnet_status,
    "bscmainnet" : bscmainnet,
    "bscmainnet_id" : bscmainnet_id,
    "bscmainnet_logo" : bscmainnet_logo,
    "bscmainnet_status" : bscmainnet_status,
    "bsctestnet" : bsctestnet,
    "bsctestnet_id" : bsctestnet_id,
    "bsctestnet_logo" : bsctestnet_logo,
    "bsctestnet_status" : bsctestnet_status,
    "moonbeammoonbasealpha" : moonbeammoonbasealpha,
    "moonbeammoonbasealpha_id" : moonbeammoonbasealpha_id,
    "moonbeammoonbasealpha_logo" : moonbeammoonbasealpha_logo,
    "moonbeammoonbasealpha_status" : moonbeammoonbasealpha_status,
    "moonbeammoonriver" : moonbeammoonriver,
    "moonbeammoonriver_id" : moonbeammoonriver_id,
    "moonbeammoonriver_logo" : moonbeammoonriver_logo,
    "moonbeammoonriver_status" : moonbeammoonriver_status,
    "rskmainnet" : rskmainnet,
    "rskmainnet_id" : rskmainnet_id,
    "rskmainnet_logo" : rskmainnet_logo,
    "rskmainnet_status" : rskmainnet_status,
    "rsktestnet" : rsktestnet,
    "rsktestnet_id" : rsktestnet_id,
    "rsktestnet_logo" : rsktestnet_logo,
    "rsktestnet_status" : rsktestnet_status,
    "arbitrummainnet" : arbitrummainnet,
    "arbitrummainnet_id" : arbitrummainnet_id,
    "arbitrummainnet_logo" : arbitrummainnet_logo,
    "arbitrummainnet_status" : arbitrummainnet_status,
    "arbitrumtestnet" : arbitrumtestnet,
    "arbitrumtestnet_id" : arbitrumtestnet_id,
    "arbitrumtestnet_logo" : arbitrumtestnet_logo,
    "arbitrumtestnet_status" : arbitrumtestnet_status,
    "fantommainnet" : fantommainnet,
    "fantommainnet_id" : fantommainnet_id,
    "fantommainnet_logo" : fantommainnet_logo,
    "fantommainnet_status" : fantommainnet_status,
    "fantomtestnet" : fantomtestnet,
    "fantomtestnet_id" : fantomtestnet_id,
    "fantomtestnet_logo" : fantomtestnet_logo,
    "fantomtestnet_status" : fantomtestnet_status,
    "palmmainnet" : palmmainnet,
    "palmmainnet_id" : palmmainnet_id,
    "palmmainnet_logo" : palmmainnet_logo,
    "palmmainnet_status" : palmmainnet_status,
    "palmtestnet" : palmtestnet,
    "palmtestnet_id" : palmtestnet_id,
    "palmtestnet_logo" : palmtestnet_logo,
    "palmtestnet_status" : palmtestnet_status,
    "klaytnmainnet" : klaytnmainnet,
    "klaytnmainnet_id" : klaytnmainnet_id,
    "klaytnmainnet_logo" : klaytnmainnet_logo,
    "klaytnmainnet_status" : klaytnmainnet_status,
    "hecomainnet" : hecomainnet,
    "hecomainnet_id" : hecomainnet_id,
    "hecomainnet_logo" : hecomainnet_logo,
    "hecomainnet_status" : hecomainnet_status,
    "hecotestnet" : hecotestnet,
    "hecotestnet_id" : hecotestnet_id,
    "hecotestnet_logo" : hecotestnet_logo,
    "hecotestnet_status" : hecotestnet_status,
    "nervospolyjuicetestnet" : nervospolyjuicetestnet,
    "nervospolyjuicetestnet_id" : nervospolyjuicetestnet_id,
    "nervospolyjuicetestnet_logo" : nervospolyjuicetestnet_logo,
    "nervospolyjuicetestnet_status" : nervospolyjuicetestnet_status,
    "axiemainnet" : axiemainnet,
    "axiemainnet_id" : axiemainnet_id,
    "axiemainnet_logo" : axiemainnet_logo,
    "axiemainnet_status" : axiemainnet_status,
    "evmostestnet" : evmostestnet,
    "evmostestnet_id" : evmostestnet_id,
    "evmostestnet_logo" : evmostestnet_logo,
    "evmostestnet_status" : evmostestnet_status,
    "astarshiden" : astarshiden,
    "astarshiden_id" : astarshiden_id,
    "astarshiden_logo" : astarshiden_logo,
    "astarshiden_status" : astarshiden_status,
    "iotexmainnet" : iotexmainnet,
    "iotexmainnet_id" : iotexmainnet_id,
    "iotexmainnet_logo" : iotexmainnet_logo,
    "iotexmainnet_status" : iotexmainnet_status,
    "iotextestnet" : iotextestnet,
    "iotextestnet_id" : iotextestnet_id,
    "iotextestnet_logo" : iotextestnet_logo,
    "iotextestnet_status" : iotextestnet_status,
    "covalentinternalnetworkv1" : covalentinternalnetworkv1,
    "covalentinternalnetworkv1_id" : covalentinternalnetworkv1_id,
    "covalentinternalnetworkv1_logo" : covalentinternalnetworkv1_logo,
    "covalentinternalnetworkv1_status" : covalentinternalnetworkv1_status,
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