#!/usr/bin/env python3

import requests
import os
import logging
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_PATH = 'api/v4'
DEFAULT_PAGE_SIZE = 100

try:
    gitlab_token = os.getenv('GITLAB_TOKEN')
    gitlab_url = os.getenv('GITLAB_URL')
except Exception as e:
    logger.error(e)

def get_project_by_group(group_id):
    custom_headers = {'PRIVATE-TOKEN': gitlab_token}
    query_string = {'per_page': DEFAULT_PAGE_SIZE}
    api_path = '%s/%s/groups/%s/projects' % (gitlab_url, BASE_PATH, group_id)

    req = requests.get(api_path, params=query_string, headers=custom_headers)
    if req.status_code == 200:
        return req.json()
    else:
        return False

def get_project_ci_var(project_id):
    custom_headers = {'PRIVATE-TOKEN': gitlab_token}
    query_string = {'per_page': DEFAULT_PAGE_SIZE}
    api_path = '%s/%s/projects/%s/variables' % (gitlab_url, BASE_PATH, project_id)

    req = requests.get(api_path, params=query_string, headers=custom_headers)
    if req.status_code == 200:
        return req.json()
    else:
        return False

group_id = sys.argv[1]

projects = get_project_by_group(group_id)
print('---')
print('ci_variables:')

for project in projects:
    ci_vars = get_project_ci_var(project['id'])
    print('  # project id : %s, project_path : %s' % (project['id'], project['path_with_namespace']))
    if ci_vars is False:
        print('  # got 403')
    else:
        for ci_var in ci_vars:
            print("  - source_var_level: project")
            print("    source_id: %s" % (project['id']))
            print("    source_var_key: '%s'" % (ci_var['key']))
            print("    dest_var_level: group")
            print("    dest_id: CHANGEME")
print('...')
    