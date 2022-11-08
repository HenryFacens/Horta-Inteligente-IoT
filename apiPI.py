import requests
import json

baseUrl = f"https://172.16.230.10/piwebapi"
dataserver ='s0tL5TGyV2r0e9YEgriOLroQUElTRVJWRVI'
scope = 'pi:PISERVER'
authorization ='Basic YWRtaW5pc3RyYXRvcjpTbWFydCoyMDIxQA=='

def getPiPoints(name):
    url = baseUrl + f"//search/query"
    params = {"q": f"name:*{name}*", "scope":scope, "count":1000}
    headers = {  'Authorization': authorization }
    response = requests.request("GET", url, headers=headers, verify=False, params=params)
    response = json.loads(response.text)["Items"]
    return response

    
def setValue(webid,value):
    url = baseUrl + f"/streams/{webid}/value"
    payload = json.dumps({"Value":value})
    headers = {  'Authorization': authorization, 'Content-Type': 'application/json' }
    return requests.request("POST", url, headers=headers, verify=False, data=payload)

