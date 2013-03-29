from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.dexterity.utils import createContentInContainer
from plone.testing import z2
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import directlyProvides
from zope.lifecycleevent import modified

import unittest


class TonttuContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""

        # Required by Products.CMFPlone:plone-content to setup defaul plone site.
        z2.installProduct(app, 'Products.PythonScripts')

        # Load ZCML
        import tonttu.content
        self.loadZCML(package=tonttu.content)

    def setUpPloneSite(self, portal):
        """Set up Plone."""

        # Installs all the Plone stuff. Workflows etc. to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone')

        # Install portal content. Including the Members folder! to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')

        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'tonttu.content:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'Products.PythonScripts')


FIXTURE = TonttuContentLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="TonttuContentLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="TonttuContentLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def create_content(self, ctype, parent=None, **kwargs):
        """Create instance of dexterity content type"""
        if parent is None:
            parent = self.portal
        content = createContentInContainer(parent, ctype, checkConstraints=False, **kwargs)
        modified(content)
        return content


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
