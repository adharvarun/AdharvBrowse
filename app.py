from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys


class UserDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(UserDialog, self).__init__(*args, **kwargs)
        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QFormLayout()

        title = QLabel("User")
        font = title.font()
        font.setPointSize(20)
        title.setAlignment(Qt.AlignCenter)
        title.setFont(font)

        self.psswd = QLabel(self)
        self.pixmap = QPixmap(os.path.join('images', 'psswd.png'), 'Passwords')
        self.psswd.setPixmap(self.pixmap)
        self.psswd.resize(self.pixmap.width(), self.pixmap.height())
        self.psswd.setAlignment(Qt.AlignCenter)
        self.psswd.setToolTip("Passwords")

        self.card = QLabel(self)
        self.pixmap = QPixmap(os.path.join('images', 'card.png'))
        self.card.setPixmap(self.pixmap)
        self.card.resize(self.pixmap.width(), self.pixmap.height())
        self.card.setAlignment(Qt.AlignCenter)
        self.card.setToolTip("Payment Methods")

        self.adr = QLabel(self)
        self.pixmap = QPixmap(os.path.join('images', 'location.png'))
        self.adr.setPixmap(self.pixmap)
        self.adr.setAlignment(Qt.AlignCenter)
        self.adr.resize(self.pixmap.width(), self.pixmap.height())
        self.adr.setToolTip("Addresses and More")

        layout.addWidget(title)
        layout.addWidget(self.psswd)
        layout.addWidget(self.card)
        layout.addWidget(self.adr)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
        self.setWindowTitle("User")
        self.setWindowIcon(QIcon(os.path.join('images', 'avatar.png')))


class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class InfoDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InfoDialog, self).__init__(*args, **kwargs)
        linkTemplate = '<a href={0}>{1}</a>'
        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Connection is Secure")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        title.setStyleSheet("color: green")

        subtitle = QLabel(
            "Your information (for example, passwords or credit card numbers) are private when sent to this site.")
        subtitle.setStyleSheet("color: black")

        label1 = HyperlinkLabel(self)
        label1.setText(linkTemplate.format(
            'https://support.brave.com/hc/en-us/articles/360018185871-How-do-I-check-if-a-site-s-connection-is-secure-', 'Learn More'))

        text = QLabel("Permissions")
        text.setStyleSheet("color: grey")

        text3 = QLabel("Cookies (In Use)")
        text3.setStyleSheet("color: grey")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(label1)
        layout.addWidget(text)
        layout.addWidget(text3)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
        self.setWindowIcon(QIcon(os.path.join('images', 'lock-ssl.png')))
        self.setWindowTitle("Site Information (Dummy Feature [No Real Data])")


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("AdharvBrowse")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('images', 'logo.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.0 Beta"))
        layout.addWidget(
            QLabel("Made by Adharv Arun"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
        self.setWindowTitle("About AdharvBrowse")
        self.setWindowIcon(QIcon(os.path.join('images', 'question.png')))


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navbar = QToolBar("Navbar")
        navbar.setIconSize(QSize(16, 16))
        navbar.setStyleSheet("padding: 5px;")
        navbar.setMovable(False)
        self.addToolBar(navbar)

        back_btn = QAction(
            QIcon(os.path.join('images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navbar.addAction(back_btn)

        next_btn = QAction(
            QIcon(os.path.join('images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navbar.addAction(next_btn)

        reload_btn = QAction(
            QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload())
        navbar.addAction(reload_btn)

        home_btn = QAction(
            QIcon(os.path.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        navbar.addSeparator()

        lock = QAction(QIcon(os.path.join("images", "lock-ssl.png")),
                       "View Site Information", self)
        lock.setStatusTip("View Site Information")
        lock.triggered.connect(self.info)
        navbar.addAction(lock)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urlbar)

        navbar.addSeparator()
	
        usr = QAction(
            QIcon(os.path.join('images', 'avatar.png')), "User", self)
        usr.setStatusTip("View this User")
        usr.triggered.connect(self.user)
        navbar.addAction(usr)

        stop_btn = QAction(
            QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navbar.addAction(stop_btn)

        tab_btn = QAction(
            QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        tab_btn.setStatusTip("Create a New Tab")
        tab_btn.triggered.connect(lambda _: self.add_new_tab())
        navbar.addAction(tab_btn)

        file_menu = self.menuBar().addMenu("&File")

        new_tab_action = QAction(
            QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        file_menu.addAction(new_tab_action)

        Quit = QAction(QIcon(os.path.join('images', 'exit.png')), "Exit", self)
        Quit.triggered.connect(self.close)
        file_menu.addAction(Quit)

        open_file_action = QAction(
            QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(
            QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(
            QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(
            QIcon(os.path.join('images', 'question.png')), "About AdharvBrowse", self)
        about_action.setStatusTip(
            "Find out more about AdharvBrowse")  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_AdharvBrowse_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')),
                                               "AdharvBrowse Homepage", self)
        navigate_AdharvBrowse_action.setStatusTip(
            "Go to AdharvBrowse Homepage")
        navigate_AdharvBrowse_action.triggered.connect(
            self.navigate_AdharvBrowse)
        help_menu.addAction(navigate_AdharvBrowse_action)

        site_menu = self.menuBar().addMenu("&Site")
        next_action = QAction(
            QIcon(os.path.join('images', 'arrow-000.png')), 'Go Forward', self)
        next_action.setStatusTip("Forward to next page")
        next_action.triggered.connect(
            lambda: self.tabs.currentWidget().forward())
        site_menu.addAction(next_action)

        back_action = QAction(
            QIcon(os.path.join('images', 'arrow-180.png')), 'Go Backward', self)
        back_action.setStatusTip("Go back to previous page")
        back_action.triggered.connect(lambda: self.tabs.currentWidget().back())
        site_menu.addAction(back_action)

        lock = QAction(QIcon(os.path.join("images", "lock-ssl.png")),
                       "View Site Information", self)
        lock.setStatusTip("View Site Information")
        lock.triggered.connect(self.info)
        site_menu.addAction(lock)

        reload_btn = QAction(
            QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload())
        site_menu.addAction(reload_btn)

        home_btn = QAction(
            QIcon(os.path.join('images', 'home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        site_menu.addAction(home_btn)

        stop_btn = QAction(
            QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        site_menu.addAction(stop_btn)

        self.add_new_tab(QUrl.fromLocalFile(os.path.join(os.getcwd(), 'homepage.html')),
                         'New Tab - AdharvBrowse')

        self.show()

        self.setWindowTitle("AdharvBrowse")
        self.setWindowIcon(QIcon(os.path.join('images', 'favicon.png')))
        self.showMaximized()

    def add_new_tab(self, qurl=None, label="New Tab - AdharvBrowse"):

        if qurl is None:
            qurl = QUrl(QUrl.fromLocalFile(os.path.join(os.getcwd(), 'homepage.html')))

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def user(self):
        dlg = UserDialog()
        dlg.exec_()

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - AdharvBrowse" % title)

    def navigate_AdharvBrowse(self):
        self.tabs.currentWidget().setUrl(QUrl("https://google.com"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def info(self):
        dlg = InfoDialog()
        dlg.exec_()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.tabs.currentWidget().setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_home(self, label="Homepage - AdharvBrowse"):
        self.tabs.currentWidget().setUrl(QUrl(QUrl.fromLocalFile(os.path.join(os.getcwd(), 'homepage.html'))))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

        self.setStyleSheet("""QLineEdit {
            padding: 5px; 
            border-radius: 5px; 
            background: #f9f9f9;
        }
        QToolButton {
            background: #f9f9f9;
            border-radius: 10px;
            min-width: 8ex;
            padding: 5px;
            margin-right: 2px;
        }
        QToolButton:hover {
            background: lightgrey;
            border-radius: 10px;
            min-width: 8ex;
            padding: 5px;
            margin-right: 2px;
        }
        QTabBar {
            background: lightgrey;
        }
        QTabBar::tab {
            margin: 0.5;
            border: 1px solid lightgrey;
            background: #f9f9f9;
            border-radius: 5px;
            min-width: 8ex;
            padding: 5px;
            margin-right: 2px;
            color: #000;
            }
        QTabBar::tab:selected {
            color: black;
            background: white;
        }
        QTabBar::tab:hover {
            background: #f0f0f0;
        }
        QWidget {
            padding: 2px;
        }
        """)


app = QApplication(sys.argv)
app.setApplicationName("AdharvBrowse")
app.setOrganizationName("CodeWithAdharv")

window = MainWindow()

app.exec_()
