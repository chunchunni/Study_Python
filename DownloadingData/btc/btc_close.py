import json

filename = 'DownloadingData/btc/data/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
