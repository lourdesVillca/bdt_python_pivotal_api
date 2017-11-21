def convert_table_to_dictionary(table):
    result = []
    header = table.headings
    for row_data in table:
        result.append(dict(zip(header, row_data)))
    return result

# def map_endpoint(end_point, object_id):
#     if object_id:
#
#     return end_point



