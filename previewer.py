from flask import render_template


def previewer(active_page, token,file_id,file_list=[]):
    token = token
    file_id = file_id

    if (active_page == 'previewer-multi-sidebar'):

        contentSidebarProps = {
            'detailsSidebarProps': {
                'hasNotices': True,
                'hasProperties': True,
                'hasAccessStats': True,
                'hasVersions': True
            },
            'hasActivityFeed': True,
            'hasSkills': True,
            'hasVersions': True,
            'hasMetadata': True
        }
    else:
        contentSidebarProps={}

    options = {
        'container': '.previewer',
        'header': 'light',
        'logoUrl':'box',

        'collection': file_list,

        'hasHeader': True,
        'showAnnotations': False,
        'showDownload': True,

        'contentSidebarProps': contentSidebarProps,

    }

    isSingle = True if len(file_list) == 0 else False

    return render_template('previewer.html',active_page=active_page, token=token, file_id=file_id, options=options, isSingle = isSingle)
