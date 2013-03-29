from Products.CMFCore.utils import getToolByName
from abita.utils.utils import get_workflow
from tonttu.content.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for subscriber: add_image_folder"""

    def test(self):
        member_area = self.create_content('tonttu.content.MemberArea', id='member-area')
        self.assertIsNotNone(member_area.get('image-folder'))
