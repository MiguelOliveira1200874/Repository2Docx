from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qsci import QsciScintilla, QsciLexerPython

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor = QsciScintilla(self)
        self.setCentralWidget(self.editor)

        # Set the lexer for Python syntax
        lexer = QsciLexerPython()
        self.editor.setLexer(lexer)

        # Enable line numbers
        self.editor.setMarginType(1, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(1, "0000")

        # Additional configurations like enabling folding, setting themes, etc.

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()