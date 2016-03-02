#!/usr/bin/python

from PyQt4 import QtCore
from PyQt4 import QtGui
from flask import Flask
from flask import render_template
import logging
import sys
import os

class MainWindows(QtGui.QMainWindow):
	
		
	def __init__(self, parent = None):
		super(MainWindows, self).__init__()
		self.initUI()
		
	def initUI(self):
		
		self.windw()
		self.statbar()
		self.home()
		self.menbar()

	def home(self):
		
		self.lab()		
		self.btn()					
		self.show()
		
	def menbar(self):
		
		server1 = QtGui.QAction("Index.php", self)
		server1.setStatusTip("Start a server with PHP support")
		server1.triggered.connect(self.php)
		
		server2 = QtGui.QAction("Index.html", self)
		server2.setStatusTip("Start a server with no PHP support")
		server2.triggered.connect(self.html)
		

		server3 = QtGui.QAction("PHP docroot", self)
		server3.setStatusTip("Open the PHP docroot")
		server3.triggered.connect(self.server3)
		
		server4 = QtGui.QAction("&Exit", self)
		server4.setStatusTip("Exit Application")
		server4.triggered.connect(self.exitt)
		
		server5 = QtGui.QAction("Install equipment", self)
		server5.setStatusTip("Install all needed part for PHP and GUI support")
		server5.triggered.connect(self.installpart)
		
		server6 = QtGui.QAction("HTML docroot", self)
		server6.setStatusTip("Open the HTML docroot")
		server6.triggered.connect(self.server6)

		helpp1 = QtGui.QAction("User guide", self)
		helpp1.setStatusTip("Guide how to use this applicatin")
		helpp1.triggered.connect(self.helpp)
		
		helpp2 = QtGui.QAction("Report Bug", self)
		helpp2.setStatusTip("Report Bug To Developer")
		helpp2.triggered.connect(self.reportbug)

		helpp3 = QtGui.QAction("Log activity", self)
		helpp3.setStatusTip("Open and see server activity log")
		helpp3.triggered.connect(self.helpp2)
		
		about1 = QtGui.QAction("About", self)
		about1.setStatusTip("About this application")
		about1.triggered.connect(self.about)
		
		about2 = QtGui.QAction("Bug list", self)
		about2.setStatusTip("List about bug on this app")
		about2.triggered.connect(self.about2)
		
		about3 = QtGui.QAction("Update list", self)
		about3.setStatusTip("List what update on this version")
		about3.triggered.connect(self.about3)
		
		mainMenu = self.menuBar()
		filemenu1 = mainMenu.addMenu('&Server')
		filemenu2 = mainMenu.addMenu('&Help')
		filemenu3 = mainMenu.addMenu('&About')
		
		filemenu1.addAction(server1)
		filemenu1.addAction(server2)
		
		filemenu1.addSeparator()
		filemenu1.addAction(server5)
		filemenu1.addAction(server3)
		filemenu1.addAction(server6)
		filemenu1.addSeparator()
		
		filemenu1.addAction(server4)
		
		filemenu2.addAction(helpp1)
		filemenu2.addAction(helpp3)
		filemenu2.addSeparator()
		filemenu2.addAction(helpp2)
		
		filemenu3.addAction(about2)
		filemenu3.addAction(about3)
		filemenu3.addSeparator()
		filemenu3.addAction(about1)	
		
	def statbar(self):

		self.statusBar()
		
	def windw(self):
		
		self.setWindowTitle("AESPro GUI Mode")
		self.setWindowIcon(QtGui.QIcon('.elements/.icon.png'))
		self.resize(350, 200)
		self.center()

	def btn(self):
		
		phpbutton = QtGui.QPushButton('Index.php', self)
		phpbutton.clicked.connect(self.php)
		phpbutton.setToolTip('click to start web server with PHP support')
		phpbutton.resize(phpbutton.minimumSizeHint())
		phpbutton.move(10, 100)
		
		htmlbutton = QtGui.QPushButton('Index.html', self)
		htmlbutton.clicked.connect(self.html)
		htmlbutton.setToolTip('click to start web server without PHP support')
		htmlbutton.resize(htmlbutton.minimumSizeHint())
		htmlbutton.move(250, 100)
		
		quitbutton = QtGui.QPushButton('&Exit', self)
		quitbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)
		quitbutton.setToolTip('Click to quit')
		quitbutton.resize(quitbutton.sizeHint())
		quitbutton.move(250, 145)
		
		instpart = QtGui.QPushButton("Install equipment", self)
		instpart.clicked.connect(self.installpart)
		instpart.setToolTip("Click to install all needed equipment")
		instpart.resize(instpart.sizeHint())
		instpart.move(111, 100)
		
	def lab(self):
		
		lab = QtGui.QLabel('<h1><b>Python Web Server</h></b>', self)
		lab.resize(260, 32)
		lab.move(55, 45)
		
	def reportbug(self):
	
		os.system("firefox --new-window mailto:oniioniichan@gmail.com")	
		
	def installpart(self):
		
		reply = QtGui.QMessageBox.information(self, "INFO",
			"Do you want to install necessary part ?",  QtGui.QMessageBox.No|
			QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:

			self.install()
		
		elif reply == QtGui.QMessageBox.No:
			
			QtGui.QMessageBox.warning(self, "WARNING", "<b><font size=18><center>Cancelled</font></b></center>\
			 <p><center>make sure your's server have php5, mysql-server, and phpmyadmin !!!</center></p>")
		
		else:

			event.ignore()

	def php(self):
			
			os.system("xfce4-terminal --title=AESPro --execute sudo python .elements/core-3.py")
		
	def html(self):
			
			os.system("xfce4-terminal --title=AESPro --execute sudo python core.py")

	def server3(self):
	
		os.system("Thunar php/")

	def server6(self):

		os.system("Thunar html/")
		
	def install(self):
	
		os.system("xfce4-terminal --title=AESPro --execute .elements/install/update.py")
		
	def helpp(self):
	
		self.faf = HowTo()
		self.faf.show()
		self.hide()

	def helpp2(self):

		self.FFF = logWindows()
		self.FFF.show()
		self.hide()
			
	def about(self):
		
		self.AboutApp = AboutWindows()
		self.AboutApp.show()
		self.hide()
			 
	def about2(self):

		self.ffa = Bug()
		self.ffa.show()
		self.hide()
			
	def about3(self):
	
		self.ffz = UpdateList()
		self.ffz.show()
		self.hide()
					
	def exit1(self):
		
		sys.exit()	
	
	def center(self):
		
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
	def closeEvent(self, event):
		
		reply = QtGui.QMessageBox.warning(self, "Exit",
			"are you want to exit this application ?", QtGui.QMessageBox.Yes |
			QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			
			event.accept()

		else:

			event.ignore()	
			
	def exitt(self):
	
		sys.exit()

class HowTo(QtGui.QWidget):

	def __init__(self, parent = None):
		super(HowTo, self).__init__()
		self.initUI()

	def initUI(self):

		self.setWindowTitle("How to use")
		self.setWindowIcon(QtGui.QIcon(".elements/.icon.png"))
		self.resize(800, 280)
		self.center()

		how = QtGui.QPlainTextEdit(self)
		how.resize(780, 200)
		how.move(12, 20)
		ff = open(".elements/doc/tutor.ve").read()
		how.setPlainText(ff)

		quu = QtGui.QPushButton("Close", self)
		quu.setToolTip("Click to Exit guide windows")
		quu.clicked.connect(self.qqq)
		quu.resize(75, 40)
		quu.move(360, 234)

	def qqq(self):

		self.fiu = MainWindows()
		self.fiu.show()
		self.hide()
	def center(self):

		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
class Bug(QtGui.QWidget):
	
	def __init__(self):
		super(Bug, self).__init__()

		self.initUI()

	def initUI(self):

		self.setWindowTitle("Bug list")
		self.setWindowIcon(QtGui.QIcon(".elements/.icon.png"))
		self.resize(800, 280)
		self.center()

		bug = QtGui.QPlainTextEdit(self)
		bug.resize(780, 200)
		bug.move(12, 20)
		ffa = open(".elements/doc/bug.ve").read()
		bug.setPlainText(ffa)

		quud = QtGui.QPushButton("Close", self)
		quud.setToolTip("Click to Exit bug list windows")
		quud.clicked.connect(self.qqd)
		quud.resize(75, 40)
		quud.move(360, 234)

	def qqd(self):

		self.fii = MainWindows()
		self.fii.show()
		self.hide()

	def center(self):

		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class logWindows(QtGui.QWidget):

	def __init__(self, parent = None):
		super(logWindows, self).__init__()
		self.GUI()
		self.center()
		
		
	def GUI(self):
		
		self.setWindowTitle("Activity Log Report")
		self.setWindowIcon(QtGui.QIcon(".elements/.icon.png"))
		self.resize(700, 275)

		report = QtGui.QPlainTextEdit(self)
		report.resize(680, 200)
		report.move(10, 30)
		f = open("log/server-activity.veil").read()	
		report.setPlainText(f)
		

		but1 = QtGui.QPushButton("exit", self)
		but1.setToolTip("Click to exit activity log report")
		but1.resize(75, 40)
		but1.move(305, 234)
		but1.clicked.connect(self.exittme)
	
	def exittme(self):
		
		self.F3 = MainWindows()
		self.F3.show()
		self.hide()

	def center(self):

		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class UpdateList(QtGui.QWidget):

	def __init__(self):

		super(UpdateList, self).__init__()
		self.initUI()

	def initUI(self):

		self.setWindowTitle("Update list")
		self.setWindowIcon(QtGui.QIcon(".elements/.icon.png"))
		self.resize(800, 280)
		self.center()

		bug = QtGui.QPlainTextEdit(self)
		bug.resize(780, 200)
		bug.move(12, 20)
		ffa = open(".elements/doc/update.ve").read()
		bug.setPlainText(ffa)

		quud = QtGui.QPushButton("Close", self)
		quud.setToolTip("Click to Exit bug list windows")
		quud.clicked.connect(self.qqd)
		quud.resize(75, 40)
		quud.move(360, 234)

	def qqd(self):

		self.fiz = MainWindows()
		self.fiz.show()
		self.hide()

	def center(self):

		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class AboutWindows(QtGui.QMainWindow):
	
	def __init__(self):
		super(AboutWindows, self).__init__()
		self.initUI()
		
		
	def initUI(self, parent = None):
		
		self.setWindowTitle("About")
		self.resize(450, 450)
		self.setWindowIcon(QtGui.QIcon('.elements/.icon.png'))
		self.mid()
		
		close = QtGui.QPushButton("Close", self)
		close.setToolTip("Click to Close Window")
		close.resize(90, 40)
		close.move(337, 403)
		close.clicked.connect(self.quitAbout)
		
		lab2 = QtGui.QLabel("<h1>AESPro 1.4.50</h1>", self)
		lab2.move(255, 50)
		lab2.resize(lab2.sizeHint())
				
		mttab = QtGui.QTabWidget(self)
		
		ttab1 = QtGui.QWidget()
		ttab2 = QtGui.QWidget()
		ttab3 = QtGui.QWidget()
		
		mttab.resize(400, 350)
		mttab.move(25, 50)

		vbx1 = QtGui.QVBoxLayout()		
		lab = QtGui.QLabel('<b><center><h2>Python Simple Web Server Project</h2></center></b>\
		<center><b></h3>"AESPro Team 1 Project"</center></b></h3><p>\
		<center><p><p><p><a href = "http://piijii.wordpress.com"><u>http://piijii.wordpress.com</center></p></p></p></a>\
		<center><i><p>Copright (C) 2015 - 2016</i></p></center>\
		<center>Rahmat Hidayat Piji Pirma</center>\
		<center>Khairul Efendi</center>\
		<center>Monalisa</center>\
		<center>Nike Amalia Hidayat</ceneter>\
		<center><p>All rights reserved</p></center>')
		
		vbx1.addWidget(lab)
		ttab1.setLayout(vbx1)
		
		vbx2 = QtGui.QVBoxLayout()		
		txt1 = QtGui.QPlainTextEdit()		
		readon = open('.elements/doc/Developer.veil').read()
		txt1.setPlainText(readon)
		vbx2.addWidget(txt1)
		ttab2.setLayout(vbx2)
		
		vbx3 = QtGui.QVBoxLayout()
		txt2 = QtGui.QPlainTextEdit()
		readon2 = open('.elements/doc/License.veil').read()
		txt2.setPlainText(readon2)
		vbx3.addWidget(txt2)
		ttab3.setLayout(vbx3)
				
		mttab.addTab(ttab1, "Info")
		mttab.addTab(ttab2, "Credits")
		mttab.addTab(ttab3, "License")

		mttab.show()
		self.show()
				
	def mid(self):
		
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def quitAbout(self):
		
		self.Main = MainWindows()
		self.Main.show()
		self.hide()

def run():


	applic = QtGui.QApplication(sys.argv)
	asp = MainWindows()
	asp.show()
	sys.exit(applic.exec_())
	
run()