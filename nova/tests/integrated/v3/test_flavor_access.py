# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.tests.integrated.v3 import api_sample_base


class FlavorAccessSampleJsonTests(api_sample_base.ApiSampleTestBaseV3):
    extension_name = 'os-flavor-access'
    extra_extensions_to_load = ['flavor-manage']
    section_name = 'Flavor Access'
    section_doc = "Flavor access support."

    def _add_tenant(self):
        subs = {
            'tenant_id': 'fake_tenant',
            'flavor_id': 10,
        }
        response = self._doc_do_post('flavors/10/action', (), (),
                                     'flavor-access-add-tenant-req',
                                     subs,
                                     api_desc="Add flavor access for tenant.")
        self._verify_response('flavor-access-add-tenant-resp',
                              subs, response, 200)

    def _create_flavor(self):
        subs = {
            'flavor_id': 10,
            'flavor_name': 'test_flavor'
        }
        response = self._doc_do_post("flavors", (), (),
                                     "flavor-access-create-req",
                                     subs,
                                     api_desc="Extend flavor create to "
                                     "add accesss attribute to "
                                     "the response of flavor create.")
        subs.update(self._get_regexes())
        self._verify_response("flavor-access-create-resp", subs, response, 200)

    def test_flavor_access_create(self):
        self._create_flavor()

    def test_flavor_access_detail(self):
        response = self._doc_do_get('flavors/detail', (), (),
                                    api_desc="Extend flavor detail to "
                                    "add accesss attribute to "
                                    "the response of flavor detail.")
        subs = self._get_regexes()
        self._verify_response('flavor-access-detail-resp', subs, response, 200)

    def test_flavor_access_list(self):
        self._create_flavor()
        self._add_tenant()
        flavor_id = 10
        response = self._doc_do_get('flavors/%s/os-flavor-access' % flavor_id,
                                    (), (),
                                    api_desc="Return access list by flavor "
                                    "id.")
        subs = {
            'flavor_id': flavor_id,
            'tenant_id': 'fake_tenant',
        }
        self._verify_response('flavor-access-list-resp', subs, response, 200)

    def test_flavor_access_show(self):
        flavor_id = 1
        response = self._doc_do_get('flavors/%s' % flavor_id, (), (),
                                    api_desc="Extend flavor show to "
                                    "add accesss attribute to "
                                    "the response of flavor show.")
        subs = {
            'flavor_id': flavor_id
        }
        subs.update(self._get_regexes())
        self._verify_response('flavor-access-show-resp', subs, response, 200)

    def test_flavor_access_add_tenant(self):
        self._create_flavor()
        self._add_tenant()

    def test_flavor_access_remove_tenant(self):
        self._create_flavor()
        self._add_tenant()
        subs = {
            'tenant_id': 'fake_tenant',
        }

        response = self._doc_do_post('flavors/10/action', (), (),
                                     "flavor-access-remove-tenant-req",
                                     subs,
                                     api_desc="Remove flavor access for "
                                     "tenant.")
        exp_subs = {
            "tenant_id": self.api.project_id,
            "flavor_id": "10"
        }
        self._verify_response('flavor-access-remove-tenant-resp',
                              exp_subs, response, 200)


class FlavorAccessSampleXmlTests(FlavorAccessSampleJsonTests):
    ctype = 'xml'
