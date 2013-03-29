from tonttu.content.schema import MemberAreaSchema
from plone.app.layout.navigation.interfaces import INavigationRoot


class IMemberArea(MemberAreaSchema, INavigationRoot):
    """Interface for MemberArea"""
