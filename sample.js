import ContentPreview from 'box-ui-elements/es/elements/content-preview';

// In this example we dynamically import box-annotations which will provide a BoxAnnotations object in global 
// You may see one already from legacy annotations if you do not dynamically load the latest version of box-annotations

const importAnnotations = () => import(/* webpackChunkName: "box-annotations"
*/ 'box-annotations');

function App() {
    const token = "YOUR_TOKEN"
    const fileId = 'YOUR_FILE_ID'
    const boxAnnotations = useRef(null);
    const [annotationsLoaded, setAnnotationsLoaded] = useState(false);

    useEffect(() => {
        importAnnotations().then(() => {
            boxAnnotations.current = new global.BoxAnnotations();
            setAnnotationsLoaded(true);
        });
    }, []);

    return (
        <div className="App">
            {annotationsLoaded && (<ContentPreview
                boxAnnotations={boxAnnotations.current}
                contentSidebarProps={{
                    hasActivityFeed: true, // Enabled Activity Feed which will show you the comments in the sidebar
                    features: {
                        activityFeed: {
                            annotations: {
                                enabled: true // Enables the ability to see your annotation comment in the Activity Feed 
                            }
                        }
                    }
                }}
                enableAnnotationsDiscoverability // Region button still appears with showAnnotationsControls but this is required to use it
                showAnnotations={annotationsLoaded} // Show annotations on the file
                showAnnotationsControls // Shows annotation controls in toolbar
                showAnnotationsDrawing // This and showAnnotationsDrawingCreate need to be true to enable the drawing annotation in the toolbar showAnnotationsDrawingCreate
                fileId={annotationsLoaded ? fileId : undefined}
                token={token}
            />)
            }
        </div>
    );
}


 /*
    {
    "type": "file",
    "id": "977175886204",
    "etag": "1",
    "permissions": {
        "can_download": true,
        "can_preview": true,
        "can_upload": true,
        "can_comment": true,
        "can_rename": true,
        "can_delete": true,
        "can_share": true,
        "can_set_share_access": true,
        "can_invite_collaborator": true,
        "can_annotate": true,
        "can_view_annotations_all": true,
        "can_view_annotations_self": true,
        "can_create_annotations": true,
        "can_view_annotations": true
    },
    "shared_link": null,
    "sha1": "6b5afbbeee7fc516837dd177fa0ec18c7d8310a6",
    "file_version": {
        "type": "file_version",
        "id": "1056477010381",
        "sha1": "6b5afbbeee7fc516837dd177fa0ec18c7d8310a6"
    },
    "name": "bui-ui-elements (1).png",
    "size": 306660,
    "extension": "png",
    "representations": {
        "entries": [
            {
                "representation": "3d",
                "properties": {},
                "info": {
                    "url": "https://api.box.com/2.0/internal_files/977175886204/versions/1056477010381/representations/3d"
                },
                "status": {
                    "state": "none"
                },
                "content": {
                    "url_template": "https://public.boxcloud.com/api/2.0/internal_files/977175886204/versions/1056477010381/representations/3d/content/{+asset_path}"
                }
            },
            {
                "representation": "jpg",
                "properties": {
                    "dimensions": "1024x1024",
                    "paged": "false",
                    "thumb": "false"
                },
                "info": {
                    "url": "https://api.box.com/2.0/internal_files/977175886204/versions/1056477010381/representations/jpg_1024x1024"
                },
                "status": {
                    "state": "success"
                },
                "content": {
                    "url_template": "https://public.boxcloud.com/api/2.0/internal_files/977175886204/versions/1056477010381/representations/jpg_1024x1024/content/{+asset_path}"
                }
            },
            {
                "representation": "png",
                "properties": {
                    "dimensions": "2048x2048",
                    "paged": "true",
                    "thumb": "false"
                },
                "info": {
                    "url": "https://api.box.com/2.0/internal_files/977175886204/versions/1056477010381/representations/png_paged_2048x2048"
                },
                "status": {
                    "state": "success"
                },
                "content": {
                    "url_template": "https://public.boxcloud.com/api/2.0/internal_files/977175886204/versions/1056477010381/representations/png_paged_2048x2048/content/{+asset_path}"
                },
                "metadata": {
                    "pages": 1
                }
            },
            {
                "content": {
                    "url_template": "https://public.boxcloud.com/api/2.0/files/977175886204/content?preview=true&version=1056477010381"
                },
                "representation": "ORIGINAL",
                "status": {
                    "state": "success"
                }
            }
        ]
    },
    "watermark_info": {
        "is_watermarked": false
    },
    "authenticated_download_url": "https://public.boxcloud.com/api/2.0/files/977175886204/content",
    "is_download_available": true
}
*/


/*
{
    "NAME": "Image",
    "REP": "png",
    "EXT": [
        "ai",
        "bmp",
        "dcm",
        "eps",
        "gif",
        "heic",
        "png",
        "ps",
        "psd",
        "tga",
        "tif",
        "tiff"
    ],
    "ASSET": "1.png"
}
*/