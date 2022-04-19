import sys
from PyQt5 import QtWidgets


def get_text_values(initial_texts, parent=None, title="", label=""):
    dialog = QtWidgets.QInputDialog()
    dialog.setWindowTitle(title)
    dialog.setLabelText(label)
    dialog.show()
    # hide default QLineEdit
    dialog.findChild(QtWidgets.QLineEdit).hide()

    editors = []
    for i, text in enumerate(initial_texts, start=1):
        editor = QtWidgets.QLineEdit(text=text)
        dialog.layout().insertWidget(i, editor)
        editors.append(editor)

    ret = dialog.exec_() == QtWidgets.QDialog.Accepted
    return ret, [editor.text() for editor in editors]


def main():
    app = QtWidgets.QApplication(sys.argv)
    ok, texts = get_text_values(
        ["hello", "world"], title="Input Dialog", label="Enter your name:"
    )
    print(ok, texts)


if __name__ == "__main__":
    main()