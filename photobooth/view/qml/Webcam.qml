import QtQuick
import QtMultimedia
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

Rectangle {
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

    RowLayout {
        height: 500
        width: 700
        // display the video output
        VideoOutput {
            id: videoOutput
            // anchors.fill: parent
            // TODO remove
            Layout.preferredHeight: 200
            Layout.preferredWidth: 200
        }

        Timer {
            id: timer
            running: false
            repeat: false

            property var callback

            onTriggered: callback() // qmllint disable
        }

        Button {
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
            function setCapture() {
                image.source = imageCapture.preview;
            }

            text: "test"
            onClicked: {
                // TODO add date to filename
                imageCapture.captureToFile(UiData.photosPath);

                print("start delay");
                // TODO add a check when the image is ready instead of a fixed delay
                setTimeout(setCapture, 500);
                print(image.source);
            }
        }

        Rectangle {
            Layout.preferredHeight: 200
            Layout.preferredWidth: 200
            color: "red"
            Image {
                id: image
                anchors.fill: parent
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
    clip: true
}
