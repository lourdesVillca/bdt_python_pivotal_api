import json
import re


def convert_table_to_dictionary(table):
    result = []
    header = table.headings
    for row_data in table:
        result.append(dict(zip(header, row_data)))

    for row_data in result:
        for key, value in row_data.items():
            if is_boolean(row_data[key]):
                row_data[key] = json.loads(value)
            elif is_integer(row_data[key]):
                row_data[key] = json.loads(value)
    return result


def is_boolean(value):
    if value == 'true' or value == 'false':
        return True
    else:
        return False


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def map_url(end_point, context):
    mapped_url = end_point
    if re.search(r'<.*>', end_point):
        if hasattr(context, 'project_response'):
            mapped_url = re.sub("<project_id>", str(context.project_response.json()["id"]), end_point)
        if hasattr(context, 'story_response'):
            mapped_url = re.sub("<story_id>", str(context.story_response.json()["id"]), mapped_url)
        if hasattr(context, 'workspace_response'):
            mapped_url = re.sub("<workspace_id>", str(context.workspace_response.json()["id"]), mapped_url)
    return mapped_url


def delete_projects(context):
    project_list = context.request_api.execute_request('get', 'projects')
    if project_list.json():
        for project in project_list.json():
            delete_url = 'projects/' + str(project['id'])
            context.request_api.execute_request('delete', delete_url)


def delete_workspace(context):
    workspace_list = context.request_api.execute_request('get', 'my/workspaces')
    for workspace in workspace_list.json():
        delete_url = '/my/workspaces/' + str(workspace['id'])
        context.request_api.execute_request('delete', delete_url)
