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

    def test_workflow__tonttu_content_MemberArea(self):
        workflow = getToolByName(self.portal, 'portal_workflow')
        self.assertEqual(
            workflow.getChainForPortalType('tonttu.content.MemberArea'), ('private_state_workflow',))

    def test_workflows__private_state_workflow__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        self.assertEqual(workflow.description, '')

    def test_workflows__private_state_workflow__initial_state(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        self.assertEqual(workflow.initial_state, 'private')

    def test_workflows__private_state_workflow__manager_bypass(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        self.assertFalse(workflow.manager_bypass)

    def test_workflows__private_state_workflow__state_variable(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        self.assertEqual(workflow.state_var, 'review_state')

    def test_workflows__private_state_workflow__title(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        self.assertEqual(workflow.title, 'Private State Workflow')

    def test_workflows__private_state_workflow__permissions(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        self.assertEqual(workflow.permissions, (
            'Access contents information',
            'Change portal events',
            'Modify portal content',
            'View'))

    def test_workflows__private_state_workflow__states__private__title(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        state = workflow.states.private
        self.assertEqual(state.title, 'Private')

    def test_workflows__private_state_workflow__states__private__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        state = workflow.states.private
        self.assertEqual(state.description, 'Can only be seen and edited by the owner.')

    def test_workflows__private_state_workflow__states__private__transitions(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        state = workflow.states.private
        self.assertEqual(state.getTransitions(), ())

    def test_workflows__private_state_workflow__states__private__permission__Access_contents_information(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('Access contents information'), {
            'acquired': 0,
            'roles': ['Contributor', 'Editor', 'Manager', 'Owner', 'Reader', 'Site Administrator'],
        })

    def test_workflows__private_state_workflow__states__private__permission__Modify_portal_content(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('Modify portal content'), {
            'acquired': 0,
            'roles': ['Editor', 'Manager', 'Owner', 'Site Administrator'],
        })

    def test_workflows__private_state_workflow__states__private__permission__View(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        state = workflow.states.private
        self.assertEqual(state.getPermissionInfo('View'), {
            'acquired': 0,
            'roles': ['Contributor', 'Editor', 'Manager', 'Owner', 'Reader', 'Site Administrator'],
        })

    def test_workflows__private_state_workflow__variables__action__for_catalog(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.action
        self.assertFalse(variable.for_catalog)

    def test_workflows__private_state_workflow__variables__action__for_status(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.action
        self.assertTrue(variable.for_status)

    def test_workflows__private_state_workflow__variables__action__updata_always(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.action
        self.assertTrue(variable.update_always)

    def test_workflows__private_state_workflow__variables__action__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.action
        self.assertEqual(variable.description, 'Previous transition')

    def test_workflows__private_state_workflow__variables__action__default(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.action
        self.assertEqual(variable.getDefaultExprText(), 'transition/getId|nothing')

    def test_workflows__private_state_workflow__variables__action__guard(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.action
        self.assertIsNone(variable.info_guard)

    def test_workflows__private_state_workflow__variables__actor__for_catalog(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.actor
        self.assertFalse(variable.for_catalog)

    def test_workflows__private_state_workflow__variables__actor__for_status(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.actor
        self.assertTrue(variable.for_status)

    def test_workflows__private_state_workflow__variables__actor__updata_always(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.actor
        self.assertTrue(variable.update_always)

    def test_workflows__private_state_workflow__variables__actor__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.actor
        self.assertEqual(variable.description, 'The ID of the user who performed the previous transition')

    def test_workflows__private_state_workflow__variables__actor__default(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.actor
        self.assertEqual(variable.getDefaultExprText(), 'user/getId')

    def test_workflows__private_state_workflow__variables__actor__guard(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.actor
        self.assertIsNone(variable.info_guard)

    def test_workflows__private_state_workflow__variables__comments__for_catalog(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.comments
        self.assertFalse(variable.for_catalog)

    def test_workflows__private_state_workflow__variables__comments__for_status(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.comments
        self.assertTrue(variable.for_status)

    def test_workflows__private_state_workflow__variables__comments__updata_always(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.comments
        self.assertTrue(variable.update_always)

    def test_workflows__private_state_workflow__variables__comments__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.comments
        self.assertEqual(variable.description, 'Comment about the last transition')

    def test_workflows__private_state_workflow__variables__comments__default(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.comments
        self.assertEqual(variable.getDefaultExprText(),
            "python:state_change.kwargs.get('comment', '')")

    def test_workflows__private_state_workflow__variables__comments__guard(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.comments
        self.assertIsNone(variable.info_guard)

    def test_workflows__private_state_workflow__variables__review_history__for_catalog(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.review_history
        self.assertFalse(variable.for_catalog)

    def test_workflows__private_state_workflow__variables__review_history__for_status(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.review_history
        self.assertFalse(variable.for_status)

    def test_workflows__private_state_workflow__variables__review_history__updata_always(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.review_history
        self.assertFalse(variable.update_always)

    def test_workflows__private_state_workflow__variables__review_history__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.review_history
        self.assertEqual(variable.description, 'Provides access to workflow history')

    def test_workflows__private_state_workflow__variables__review_history__default(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.review_history
        self.assertEqual(variable.getDefaultExprText(),
            "state_change/getHistory")

    def test_workflows__private_state_workflow__variables__review_history__guard(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.review_history
        self.assertEqual(variable.info_guard.permissions,
            ('Request review', 'Review portal content'))

    def test_workflows__private_state_workflow__variables__time__for_catalog(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.time
        self.assertFalse(variable.for_catalog)

    def test_workflows__private_state_workflow__variables__time__for_status(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.time
        self.assertTrue(variable.for_status)

    def test_workflows__private_state_workflow__variables__time__updata_always(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.time
        self.assertTrue(variable.update_always)

    def test_workflows__private_state_workflow__variables__time__description(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.time
        self.assertEqual(variable.description, 'When the previous transition was performed')

    def test_workflows__private_state_workflow__variables__time__default(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.time
        self.assertEqual(variable.getDefaultExprText(),
            "state_change/getDateTime")

    def test_workflows__private_state_workflow__variables__time__guard(self):
        workflow = get_workflow(self.portal, 'private_state_workflow')
        variable = workflow.variables.time
        self.assertIsNone(variable.info_guard)

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
