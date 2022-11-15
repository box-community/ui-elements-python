import boxAnnotations from 'https://cdn.skypack.dev/box-annotations';

function preview_annotations(file_id, access_token, options) {
    var annotations = new BoxAnnotations();
    var preview = new Box.ContentPreview();
    options['boxAnnotations'] = annotations;
    return preview;
}

var contentPreviewer = preview_annotations(file_id, accessToken, options);
console.log('Content Previewer:', contentPreviewer);
console.log('Content Component:', contentPreviewer.component);
// console.log('Content Viewer:', contentPreviewer.preview.viewer);
// console.log('Content Annotator:', contentPreviewer.preview.viewer.annotator);

contentPreviewer.addListener('viewer', previewerViewer);
contentPreviewer.addListener('load', previewerLoad);
contentPreviewer.addListener('navigate', previewerNavigate);
contentPreviewer.addListener('notification', previewerNotification);
contentPreviewer.addListener('viewerevent', previewerViewerEvent);

// TODO: implement annotator related events

function previewerViewer(viewer) {
    console.log('viewer object:', viewer);
}

function previewerLoad(e) {
    console.log('load:', e);
    sendEventToServer('load', e.file);
}

function previewerNavigate(e) {
    console.log('navigate:', e);
    sendEventToServer('navigate', e);
}

function previewerNotification(e) {
    console.log('notification:', e);
    sendEventToServer('notification', e);
}

function previewerViewerEvent(e) {
    console.log('viewer event:', e);
    sendEventToServer('viewerevent', e);
}


function sendEventToServer(eventType, e) {

    var localData = {
        eventType: eventType,
        e: e
    };

    $.ajax({
        url: "{{ url_for('event') }}",
        type: 'POST',
        data: JSON.stringify(localData),
        contentType: 'application/json;charset=UTF-8',
    });
};

contentPreviewer.show(file_id, accessToken, options);