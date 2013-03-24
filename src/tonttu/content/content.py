from plone.dexterity.content import Container
from tonttu.content.interfaces import IMemberArea
from zope.interface import implements


class MemberArea(Container):
    """MemberArea content type"""
    implements(IMemberArea)
