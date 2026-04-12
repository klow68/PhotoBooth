import QtQuick
import QtQuick.Controls

import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 640
    height: 480

    Connections {
        target: backend  // qmllint disable
        function onSProjectPath(message) {
            UiData.projectPath = message;
        }

        function onSPhotoOverlayReady(path) {
            UiData.photoOverlayReady = path;
        }
    }

    title: qsTr("PhotoBooth")

    // QT FLAGS
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint

    // DESIGN THEME
    Material.theme: Material.System

    ColumnLayout {
        anchors.fill: parent
        Webcam {
            id: webcam
            Layout.fillHeight: true
            Layout.fillWidth: true
        }

        Button {
            Layout.alignment: Qt.AlignCenter
            text: '[Smile]'
            onClicked: {
                webcam.capture();
                backend.add_overlay(UiData.capturedImagePath); // qmllint disable
                yesno.open();
            }
        }
    }

    Yesno {
        id: yesno
        width: parent.width
        height: parent.height
    }
}
