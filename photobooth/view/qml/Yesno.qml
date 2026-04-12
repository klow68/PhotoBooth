import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Popup {
    id: popup
    modal: true
    focus: true
    closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

    ColumnLayout {
        anchors.fill: parent

        Image {
            id: image
            Layout.alignment: Qt.AlignCenter
            Layout.fillHeight: true
            Layout.fillWidth: true
            fillMode: Image.PreserveAspectFit
            smooth: true
            source: UiData.photoOverlayReady
            visible: image.source !== ""
        }

        AnimatedImage {
            id: animation
            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: 181
            Layout.preferredHeight: 150
            // gif used: https://www.artstation.com/artwork/qAkERa
            source: "qrc:assets/loading.gif"
            visible: image.source === ""
        }

        RowLayout {
            Layout.alignment: Qt.AlignCenter

            Button {
                Layout.alignment: Qt.AlignCenter
                text: 'Cancel'
                onClicked: {
                    popup.close();
                    // reset image to avoid showing the previous one when reopening the popup
                    UiData.photoOverlayReady = "";
                }
            }
            Button {
                Layout.alignment: Qt.AlignCenter
                text: 'Print'
                onClicked: {
                    popup.close();
                    // reset image to avoid showing the previous one when reopening the popup
                    UiData.photoOverlayReady = "";
                }
            }
        }
    }
}
