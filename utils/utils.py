def convert_table_to_dictionary(table):
    result = []
    header = table.headings
    for row_data in table:
        result.append(dict(zip(header, row_data)))
    return result
