
def end_point_modifier(end_point,response,name):
    endpoint_value_id= (response.json())['id']
    print((response.json())['name'])
    return end_point.replace(name,str(endpoint_value_id))

