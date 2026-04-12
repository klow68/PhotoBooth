import QtQuick
import QtMultimedia
import QtQuick.Layouts
import QtQuick.Controls.Material

Item {

    signal capture

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
        UiData.capturedImage = imageCapture.preview;
    }

    onCapture: {
        print("capture signal received");
        UiData.capturedImagePath = UiData.photosPath + Qt.formatDateTime(new Date(), "dd-MM-yyyy_hhmmss") + ".jpg";
        imageCapture.captureToFile(UiData.capturedImagePath);

        print("start delay");
        // TODO add a check when the image is ready instead of a fixed delay
        // setTimeout(setCapture, 500);
        // print(image.source);

    }

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
        anchors.fill: parent
        // display the video output
        VideoOutput {
            id: videoOutput
            Layout.alignment: Qt.AlignCenter
            Layout.fillHeight: true
            Layout.fillWidth: true
        }

        Timer {
            id: timer
            running: false
            repeat: false

            property var callback

            onTriggered: callback() // qmllint disable
        }
    }

    Component.onCompleted: {
        captureSession.camera.start();
    }
    clip: true
}
