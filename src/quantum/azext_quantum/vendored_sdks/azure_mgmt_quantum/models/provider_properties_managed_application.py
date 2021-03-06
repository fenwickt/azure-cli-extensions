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


class ProviderPropertiesManagedApplication(Model):
    """Provider's Managed-Application info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar publisher_id: Provider's publisher id.
    :vartype publisher_id: str
    :ivar offer_id: Provider's offer id.
    :vartype offer_id: str
    """

    _validation = {
        'publisher_id': {'readonly': True},
        'offer_id': {'readonly': True},
    }

    _attribute_map = {
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProviderPropertiesManagedApplication, self).__init__(**kwargs)
        self.publisher_id = None
        self.offer_id = None
