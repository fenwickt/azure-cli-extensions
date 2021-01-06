# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .arm_proxy_resource import ARMProxyResource


class NotebookWorkspace(ARMProxyResource):
    """A notebook workspace resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The unique resource identifier of the database account.
    :vartype id: str
    :ivar name: The name of the database account.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :ivar notebook_server_endpoint: Specifies the endpoint of Notebook server.
    :vartype notebook_server_endpoint: str
    :ivar status: Status of the notebook workspace. Possible values are:
     Creating, Online, Deleting, Failed, Updating.
    :vartype status: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'notebook_server_endpoint': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'notebook_server_endpoint': {'key': 'properties.notebookServerEndpoint', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NotebookWorkspace, self).__init__(**kwargs)
        self.notebook_server_endpoint = None
        self.status = None