from five import grok
from tonttu.content.interfaces import IMemberArea
from zope.lifecycleevent.interfaces import IObjectAddedEvent


@grok.subscribe(IMemberArea, IObjectAddedEvent)
def add_image_folder(context, event):
    assert context == event.object
    folder = context[context.invokeFactory('Folder', id='image-folder', title='Image Folder')]
    folder.reindexObject()
