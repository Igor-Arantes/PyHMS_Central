
import pandas as pd






pre_get = 'http://'
get_hms = '/get/data?localtime&airpresok&airtempok&headvsok&heavprok&heavvlok&ptchupvok&relhumiok&rollptvok&winddirok&windspdok'
get_epta = '/get/data?localtime&airpresok&airtempok&headvsok&relhumiok&winddirok&windspdok'


def get_status_hms(target, pre_get, get_hms):
    try:
        status = pd.read_json(pre_get+target+get_hms,orient='index')
        status.columns = ['Status']
        return status
    except:
        return print(f"Error: Type {target} not conected")
    
    

def get_status_epta(target, pre_get, get_epta):
    try:
        status = pd.read_json(pre_get+target+get_epta,orient='index')
        status.columns = ['Status']
        return status
    except:
        return print(f"Error: Type {target} not conected")
    