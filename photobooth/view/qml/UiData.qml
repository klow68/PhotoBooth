pragma Singleton
import QtQuick

QtObject {
    property string projectPath: ""
    property string photosPath: projectPath + "/photos"
}
