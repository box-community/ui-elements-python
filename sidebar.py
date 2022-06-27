from flask import render_template

def sidebar(active_page, token,file_id):
    token = token
    file_id = file_id

    options = {
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

    return render_template('sidebar.html',active_page=active_page, token=token, file_id=file_id, options=options)