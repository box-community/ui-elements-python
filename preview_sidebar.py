from flask import render_template


def preview_sidebar(active_page, token, file_id):
    token = token
    file_id = file_id

    optionsPreview = {
        'container': '.previewer',
        'header': 'light',
        'logoUrl': '',

        'showAnnotations': False,
        'showDownload': True,
    }

    optionsSidebar = {
        'container': '.sidebar',
        'hasActivityFeed': True,
        'hasMetadata': True,
        'hasSkills': True,
        'detailsSidebarProps': {
            'hasProperties': True,
            'hasAccessStats': True,
            'hasVersions': True,
            'hasNotices': True,
        }
    }

    return render_template('preview_sidebar.html'
                        , active_page=active_page
                        , token=token
                        , file_id=file_id
                        , optionsPreview=optionsPreview
                        , optionsSidebar=optionsSidebar)
