from flask import Flask, render_template


def explorer(active_page,token):
    token = token
    rootFolderId = 0

    optionsSidebar = {
        'hasActivityFeed': True,
        'hasMetadata': True,
        'hasSkills': True,
        'hasVersions': True,
        'detailsSidebarProps': {
            'hasProperties': True,
            'hasNotices': True,
            'hasAccessStats': True,
            'hasClassification': True,
            'hasRetentionPolicy': True,
        },
    }

    optionsPreviewer = {
        'logoUrl': 'box',
        'contentSidebarProps':optionsSidebar,
    }

    optionsUploader = {
    }

    options = {
        'container': '.explorer',
        'currentFolderId': rootFolderId,
        'logoUrl': 'box',

        'defaultView': 'files',
        'sortBy': 'name',
        'sortDirection': 'ASC',

        'canPreview': True,
        'canDownload': True,
        'canDelete': True,
        'canRename': True,
        'canUpload': True,
        'canCreateNewFolder': True,
        'canShare': True,
        'canSetShareAccess': True,

        'contentPreviewProps': optionsPreviewer,
        'contentUploaderProps': optionsUploader,

    }

    return render_template('explorer.html',active_page=active_page, token=token, rootFolderId=rootFolderId, options=options)
