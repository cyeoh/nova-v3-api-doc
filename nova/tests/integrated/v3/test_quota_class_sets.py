# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2012 Nebula, Inc.
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


class QuotaClassesSampleJsonTests(api_sample_base.ApiSampleTestBaseV3):
    extension_name = "os-quota-class-sets"
    section_name = 'Quota Classes'
    section_doc = "Quota classes management support."
    set_id = 'test_class'

    def test_show_quota_classes(self):
        # Get api sample to show quota classes.
        response = self._doc_do_get('os-quota-class-sets/%s', self.set_id,
                                    'class_id',
                                    api_desc='Shows the quota for class.')
        subs = {'set_id': self.set_id}
        self._verify_response('quota-classes-show-get-resp', subs,
                              response, 200)

    def test_update_quota_classes(self):
        # Get api sample to update quota classes.
        response = self._doc_do_put('os-quota-class-sets/%s', self.set_id,
                                    'class_id',
                                    'quota-classes-update-post-req',
                                    {},
                                    api_desc='Updates quota for class.')
        self._verify_response('quota-classes-update-post-resp',
                              {}, response, 200)


class QuotaClassesSampleXmlTests(QuotaClassesSampleJsonTests):
    ctype = "xml"
