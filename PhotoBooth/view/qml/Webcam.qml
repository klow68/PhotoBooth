import QtQuick
import QtMultimedia
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

Rectangle {
    id: toto
    visible: true

    // List media devices
    MediaDevices {
        id: mediaDevices
    }

    // capture the session
    CaptureSession {
        id: captureSession
        camera: Camera {
            id: camera
            cameraDevice: mediaDevices.defaultVideoInput
        }
        imageCapture: ImageCapture {
            id: imageCapture
        }
        videoOutput: videoOutput
    }

    RowLayout{
        height:500
        width:700
    // display the video output
    VideoOutput {
        id: videoOutput
        // anchors.fill: parent
        // TODO remove
        Layout.preferredHeight:200
        Layout.preferredWidth:200
    }

    Timer {
        id: timer
        running: false
        repeat: false

        property var callback

        onTriggered: callback()
    }



    
    Button{     
        // TODO add this to a utils
        function setTimeout(callback, delay) {
            if (timer.running) {
                console.error("nested calls to setTimeout are not supported!");
                return;
            }
            timer.callback = callback;
            // note: an interval of 0 is directly triggered, so add a little padding
            timer.interval = delay + 1;
            timer.running = true;
        }
        function setCapture(){
            
            image.source=imageCapture.preview
        }
        
        text: "test"
        onClicked:{
            imageCapture.captureToFile("")


            print("start delay")
            setTimeout(setCapture, 500)
            print(image.source)
        }
    }
    
    Rectangle{
        Layout.preferredHeight:200
        Layout.preferredWidth:200
        color:"red"
        Image{
            id: image
            anchors.fill :parent
            // Layout.preferredHeight:200
            // Layout.preferredWidth:200
            fillMode: Image.PreserveAspectFit
            smooth: true
        }
        
    }
    }


    Component.onCompleted: {
        captureSession.camera.start();
    }
    clip:true
}
