# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok / WMS Base project
#
#    Copyright (C) 2018 Georges Racinet <gracinet@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.tests.testcase import BlokTestCase
from .. import import_declarations


class TestPhysObjPackage(BlokTestCase):

    def test_reload(self):
        import sys
        module_type = sys.__class__  # is there a simpler way ?

        def fake_reload(module):
            self.assertIsInstance(module, module_type)

        import_declarations(reload=fake_reload)
