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

from msrest.serialization import Model


class VICredential(Model):
    """Username / Password Credentials to connect to vcenter.

    :param username: Gets or sets username to connect with the vCenter.
    :type username: str
    :param password: Gets or sets the password to connect with the vCenter.
    :type password: str
    """

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VICredential, self).__init__(**kwargs)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)