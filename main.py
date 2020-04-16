import requests

def get_available_time_series():
    url = "http://localhost:9090/api/v1/label/__name__/values"
    r = requests.get(url)
    #print(r.json()['data'])

    return r.json()['data']

def get_time_series_metric(name):
    baseurl = "http://localhost:9090/api/v1/"
    url = baseurl + "query?query=" + name
    r = requests.get(url).json()
    #print(r)

    if r['status'] == "success":
        resultType = r['data']['resultType']
        print("Type of result : " + resultType)
        return r['data']['result']

print(get_available_time_series())

print(get_time_series_metric("node_time_seconds"))