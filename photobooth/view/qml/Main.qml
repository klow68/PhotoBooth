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
            print(UiData.projectPath);
        }
    }

    title: qsTr("PhotoBooth")

    // QT FLAGS
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint

    // DESIGN THEME
    Material.theme: Material.System

    RowLayout {
        anchors.fill: parent
        Webcam {
            Layout.fillHeight: true
            Layout.fillWidth: true
        }
        ColumnLayout {
            Button {
                Layout.alignment: Qt.AlignCenter
                text: '[Smile]'
                onClicked: {
                    backend.test2(); // qmllint disable
                }
            }
            // Test image with qrc
            // Image{
            //     Layout.fillHeight: true
            //     Layout.fillWidth: true
            //     source: "qrc:assets/cadre_photo.jpg"
            // }
        }
    }
}
