pragma Singleton
import QtQuick

QtObject {
    // PROJECT
    property string projectPath: ""

    // PHOTOS
    property string photosPath: projectPath + "/photos/"
    property var capturedImage: ""
    property string capturedImagePath: ""
    property string photoOverlayReady: ""
}
