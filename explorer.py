from flask import Flask, render_template

def explorer(token):
    token = token
    rootFolderId = 0
    options = {
        'container' : '.explorer',
        'sortBy' : 'name',
        'sortDirection' : 'ASC',
        'logoUrl' : 'box',
        'canPreview' : True,
        'canDownload' : True,
        'canDelete' : True,
        'canRename' : True,
        'canUpload' : True,
        'canCreateNewFolder' : True,
        'canShare' : True,
        'canSetShareAccess' : True,
        'defaultView' : 'files',
    }
    return render_template('explorer.html', token=token,rootFolderId=rootFolderId,options=options)