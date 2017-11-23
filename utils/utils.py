import re


def convert_table_to_dictionary(table):
    result = []
    header = table.headings
    for row_data in table:
        result.append(dict(zip(header, row_data)))
    return result


def map_url(end_point, context):
    mapped_url = end_point
    if hasattr(context, 'project_response') and 'project' in end_point:
        mapped_url = re.sub("<.*>", str(context.project_response.json()["id"]), end_point)
    elif hasattr(context, 'workspace_response') and 'workspaces' in end_point:
        mapped_url = re.sub("<.*>", str(context.workspace_response.json()["id"]), end_point)
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
