import requests
r = requests.get('https://prod.jdgroupmesh.cloud/stores/jdsportsde/products/16576975_jdsportsde?api_key=1B3BB99B0B9B482D8B8552F64B00E12F')

print(r.status_code, r.text)
