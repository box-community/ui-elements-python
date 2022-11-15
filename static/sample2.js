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
                    hasActivityFeed: true, 
                    /* Enabled Activity Feed which will 
                    show you the comments in the sidebar*/
                    features: {
                        activityFeed: {
                            annotations: {
                                enabled: true 
                                /* Enables the ability to see
                                your annotation comment in the Activity Feed */
                            }
                        }
                    }
                }}
                enableAnnotationsDiscoverability 
                /* Region button still appears
                with showAnnotationsControls but this is required to use it*/
                showAnnotations={annotationsLoaded} // Show annotations on the file
                showAnnotationsControls // Shows annotation controls in toolbar
                showAnnotationsDrawing 
                /* This and showAnnotationsDrawingCreate
                need to be true to enable the drawing annotation in the toolbar*/
                showAnnotationsDrawingCreate
                fileId={annotationsLoaded ? fileId : undefined}
                token={token}
            />)
            }
        </div>
    );
}