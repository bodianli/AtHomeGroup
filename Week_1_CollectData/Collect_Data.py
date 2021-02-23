import json
import pandas as pd

with open('output.json', encoding='utf-8-sig', errors='ignore') as f:
    data = json.load(f, strict=False)

information_extract = data["div"]["div"]
lenth = len(information_extract)

store_name = []
store_address = []
store_state = []
store_city = []
store_zipcode = []
pickup_in_store = []
pickup_curbside = []
local_store_delivery = []

for i in range(lenth):
    # Collecting Store Name
    store_name.append(information_extract[i]["@id"])  # Store Name
    # Address
    store_address.append(information_extract[i]["div"]["div"][2]["span"][0]["#text"])  # Address
    # ZipCode
    store_zipcode.append(information_extract[i]["div"]["div"][2]["span"][1]["#text"][-5:])  # Last 5 Digits

    # Collect Information of "Details"
    Count_1 = (len(information_extract[i]["div"]["div"][1]["div"]))
    # If there is no details about store, printed list should be "NULL'
    if Count_1 == 3:
        Count_2 = len(information_extract[i]["div"]["div"][1]["div"]["div"]["div"])
        if Count_2 == 3:
            pickup_in_store.append(1)
            pickup_curbside.append(1)
            local_store_delivery.append(1)
        else:
            pickup_in_store.append(1)
            pickup_curbside.append(1)
            local_store_delivery.append(None)
    else:
        pickup_in_store.append(None)
        pickup_curbside.append(None)
        local_store_delivery.append(None)

Dictionary = {
    "Name": store_name,
    "Address": store_address,
    "ZipCode": store_zipcode,
    "Pickup_InStore": pickup_in_store,
    "Pickup_Curbside": pickup_curbside,
    "Local_Delivery": local_store_delivery
}

data = pd.DataFrame(data=Dictionary)
data.to_csv("Final_Data.csv")
