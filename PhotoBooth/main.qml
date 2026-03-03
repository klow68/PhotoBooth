import QtQuick
import QtQuick.Controls
import QtMultimedia

import QtMultimedia
import QtQuick

ApplicationWindow {
    visible: true
    width: 640
    height: 480

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
        videoOutput: videoOutput
    }

    // display the video output
    VideoOutput {
        id: videoOutput
        anchors.fill: parent
    }

    Component.onCompleted: {
        captureSession.camera.start();
    }
}
