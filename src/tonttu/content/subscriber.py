from Acquisition import aq_parent
from Products.ATContentTypes.interfaces.image import IATImage
from Products.Archetypes.interfaces import IObjectEditedEvent
from Products.Archetypes.interfaces import IObjectInitializedEvent
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.FactoryTool import TempFolder
from five import grok
from tonttu.content.interfaces import IMemberArea
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectCreatedEvent


@grok.subscribe(IATImage, IObjectInitializedEvent)
def move_image_to_image_folder(context, event):
    assert context == event.object
    parent = aq_parent(context)
    if IMemberArea.providedBy(parent):
        folder = parent.get('image-folder')
        if folder is None:
            folder = parent[parent.invokeFactory('Folder', id='image-folder', title='Image Folder')]
            folder.reindexObject()
        data = parent.manage_cutObjects([context.id])
        folder.manage_pasteObjects(data)
