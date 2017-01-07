#
# Copyright (c) 2017 by QA Cafe.
# All Rights Reserved.
#

import os.path

class Imports:
    RESOURCE = 'imports'
    BASE = '/' + RESOURCE + '/'

    def __init__(self, service):
        self.service = service
        self.base = self.BASE

    def list(self):
        return self.service.list(self.base)

    def stage_import_from_file(self, filepath):
        return self.service._post(self.base, files={'file': (os.path.basename(filepath), open(filepath, 'rb'))})

    def stage_import_from_filesystem(self, filepath):
        return self.service._post(self.base, params={'path': filepath})

    def stage_import_from_url(self, url, token=None, insecure=False):
        return self.service._post(self.base, params={'url': url, 'token': token, 'insecure': insecure})

    def get(self, id):
        return self.service.get(self.base, id)

    def get_commit_request(self, id):
        return self.service._get(self.base+str(id)+'/request/')

    def commit(self, id, commit_request):
        return self.service._post(self.base+str(id)+'/commit/', json=commit_request)

    def delete(self, id):
        return self.service.delete(self.base, id)