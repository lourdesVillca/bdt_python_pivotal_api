import re


def convert_table_to_dictionary(table):
    result = []
    header = table.headings
    for row_data in table:
        result.append(dict(zip(header, row_data)))
    return result

def map_url(end_point, context):
    mapped_url = end_point
    if hasattr(context, 'project_response'):
        mapped_url =re.sub("<.*>", str(context.project_response.json()["id"]), end_point)
    return mapped_url