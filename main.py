#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dropbox
import access

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = access.access_token
    transfer_data = TransferData(access_token)

    file_from = 'kloudless_local.txt'  # This is name of the file to be uploaded
    file_to = '/test_dropbox/kloudless_cloud.txt'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transfer_data.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()
