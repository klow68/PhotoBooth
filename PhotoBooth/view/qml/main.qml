import QtQuick
import QtQuick.Controls

import QtQuick.Controls.Material
import QtQuick.Layouts
import qml

ApplicationWindow {
    visible: true
    width: 640
    height: 480

    title: qsTr("PhotoBooth")

    // QT FLAGS
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.CustomizeWindowHint | Qt.Dialog | Qt.WindowTitleHint

    // DESIGN THEME
    Material.theme: Material.System

    RowLayout{
        anchors.fill: parent
        Webcam{
            Layout.fillHeight: true
            Layout.fillWidth: true
        }
        ColumnLayout{
            Button{
                Layout.alignment: Qt.AlignCenter
                text: '[Smile]'
                onClicked:{
                    backend.test2()
                }
            }
        }
    }
}

