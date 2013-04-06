from Products.CMFCore.utils import getToolByName
from abita.utils.utils import get_workflow
from tonttu.content.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup"""

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('tonttu.content'))

    def test_browserlayer(self):
        from tonttu.content.browser.interfaces import ITonttuContentLayer
        from plone.browserlayer import utils
        self.failUnless(ITonttuContentLayer in utils.registered_layers())

    def test_metadata__dependency__plone_app_dexterity(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(setup.getVersionForProfile('profile-tonttu.content:default'), u'0')

    def get_type_info(self, name):
        types = getToolByName(self.portal, 'portal_types')
        return types.getTypeInfo(name)

    def test_types__tonttu_content_MemberArea__i18n_domain(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.i18n_domain, 'tonttu.content')

    def test_types__tonttu_content_MemberArea__meta_type(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.meta_type, 'Dexterity FTI')

    def test_types__tonttu_content_MemberArea__title(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.title, 'Member Area')

    def test_types__tonttu_content_MemberArea__description(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.description, '')

    def test_types__tonttu_content_MemberArea__content_icon(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.getIcon(), 'group.png')

    def test_types__tonttu_content_MemberArea__allow_discussion(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertFalse(ctype.allow_discussion)

    def test_types__tonttu_content_MemberArea__global_allow(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertFalse(ctype.global_allow)

    def test_types__tonttu_content_MemberArea__filter_content_types(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertTrue(ctype.filter_content_types)

    def test_types__tonttu_content_MemberArea__allowed_content_types(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.allowed_content_types, ('Folder', 'Image',))

    def test_types__tonttu_content_MemberArea__schema(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.schema, 'tonttu.content.schema.MemberAreaSchema')

    def test_types__tonttu_content_MemberArea__klass(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.klass, 'tonttu.content.content.MemberArea')

    def test_types__tonttu_content_MemberArea__add_permission(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.add_permission, 'tonttu.content.AddMemberArea')

    def test_types__tonttu_content_MemberArea__behaviors(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.behaviors, (
            'plone.app.content.interfaces.INameFromTitle',
            'plone.app.dexterity.behaviors.metadata.IDublinCore'))

    def test_types__tonttu_content_MemberArea__default_view(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.default_view, 'view')

    def test_types__tonttu_content_MemberArea__default_view_fallback(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertFalse(ctype.default_view_fallback)

    def test_types__tonttu_content_MemberArea__view_methods(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.view_methods, ('view',))

    def test_types__tonttu_content_MemberArea__default_aliases(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        self.assertEqual(ctype.default_aliases, {
            '(Default)': '(dynamic view)',
            'edit': '@@edit',
            'sharing': '@@sharing',
            'view': '(selected layout)',
        })

    def test_types__tonttu_content_MemberArea__action__view__title(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.title, 'View')

    def test_types__tonttu_content_MemberArea__action__view__condition(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.condition, '')

    def test_types__tonttu_content_MemberArea__action__view__url_expr(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.getActionExpression(), 'string:${folder_url}/')

    def test_types__tonttu_content_MemberArea__action__view__visible(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types__tonttu_content_MemberArea__action__view__permissions(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.permissions, (u'View',))

    def test_types__tonttu_content_MemberArea__action__edit__title(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.title, 'Edit')

    def test_types__tonttu_content_MemberArea__action__edit__condition(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.condition, '')

    def test_types__tonttu_content_MemberArea__action__edit__url_expr(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}/edit')

    def test_types__tonttu_content_MemberArea__action__edit__visible(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_types__tonttu_content_MemberArea__action__edit__permissions(self):
        ctype = self.get_type_info('tonttu.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.permissions, (u'Modify portal content',))

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['tonttu.content'])
        self.failIf(installer.isProductInstalled('tonttu.content'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['tonttu.content'])
        from tonttu.content.browser.interfaces import ITonttuContentLayer
        from plone.browserlayer import utils
        self.failIf(ITonttuContentLayer in utils.registered_layers())
