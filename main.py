import requests


def get_metrics_list():
    url = "http://localhost:9090/api/v1/label/__name__/values"
    r = requests.get(url)
    #print(r.json()['data'])

    return r.json()['data'][:20]

def get_metrics(metric):
    #url = http://localhost:9090/
    pass

print(get_metrics_list())