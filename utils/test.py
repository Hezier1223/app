import json

import requests

headers = {
    'appver': '11.2.5_qnreading_4.6.60',
    'cache-control': 'no-cache',
    'devicetoken': '<21f74968 01ff564f a7a9f454 0e3b97f0 62aa6ccd 86b9f746 6756f294 7fc728b9>',
    'devid': 'BC8A2BEF-7946-4688-8FC4-01D47382696B',
    'postman-token': 'cc19f89a-05e7-16e3-cdff-9ce5bb39230d',
    'qn-rid': '1D18C30D-68E4-4F5D-9224-537BBA0A9CBD',
    'qn-sig': '463AEA100794AC811F1279CAD7C72B80',
    'user-agent': 'qnreading (iPhone7)',
}

data = [
    ('queryid', ''),
    ('query', '古天乐'),
    ('type', 'aggregate'),
    ('adcode', '310106'),
    ('sid', 5757821415400871164),
    ('page', 2)
]

response = requests.post('https://r.cnews.qq.com/searchByType', headers=headers, data=data)
print(json.loads(response.text))

url = "https://r.cnews.qq.com/searchByType"

payload = "query=古天乐&type=aggregate&adcode=310106".encode('utf-8')

headers = {
    'devicetoken': "<21f74968 01ff564f a7a9f454 0e3b97f0 62aa6ccd 86b9f746 6756f294 7fc728b9>",
    'qn-rid': "1D18C30D-68E4-4F5D-9224-537BBA0A9CBD",
    'qn-sig': "463AEA100794AC811F1279CAD7C72B80",
    'user-agent': "qnreading (iPhone7)",
    'appver': "11.2.5_qnreading_4.6.60",
    'devid': "BC8A2BEF-7946-4688-8FC4-01D47382696B",
    'cache-control': "no-cache",
    'postman-token': "f8e11cc9-71ce-5f1c-6c64-67fc0965c0ab"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(json.loads(response.text))
