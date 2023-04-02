import requests
r = requests.get('https://prod.jdgroupmesh.cloud/stores/jdsportsuk/products/16117278?channel=iphone-app&expand=variations,informationBlocks,customisations')

print(r.status_code, r.text)
