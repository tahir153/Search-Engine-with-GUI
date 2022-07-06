import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_btn = QAction( "Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Back Button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload Button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Home Button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.back_to_home)
        navbar.addAction(home_btn)

        # Search Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.search_bar)
        navbar.addWidget(self.url_bar)

    def back_to_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def search_bar(self):
        url = self.url_bar.text()
        # self.browser.setUrl(QUrl(url))
        self.browser.setUrl(QUrl("http://"+str(url)))


app = QApplication(sys.argv)
QApplication.setApplicationName("Tahir's Browser")
Window = MainWindow()
app.exec()