import requests
# class DataFromURL:
    
def get_data_from_url():
    link_data = "https://leaflink-engineering-interview-docs.s3-us-west-2.amazonaws.com/public/frontend/WorldGeography/country_data.json"
    data = requests.get(link_data)
    regions = {}
    data_json = {k:v for v,k in enumerate(data)}
    
    for val in data.json()[:20]:
        print(val)
   
        

def get_country_data(aggregation="sum", field="population", by="region"):
    pass

get_data_from_url()