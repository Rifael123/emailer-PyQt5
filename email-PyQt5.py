from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
class KirimEmail(QWidget):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		vb = QVBoxLayout()
		self.setLayout(vb)
		self.label = QLabel("G M A I L  A C C O U N T", objectName="Label")
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setFont(QFont("Times",32))
		vb.addWidget(self.label)
		
		
		hb = QHBoxLayout()
		vb.addLayout(hb)
		
		self.toAddr = QLabel("To        :    ", objectName="to")
		hb.addWidget(self.toAddr)
		
		self.toLine= QLineEdit()
		hb.addWidget(self.toLine)
		
		hb2 = QHBoxLayout()
		vb.addLayout(hb2)
		
		self.fromAddr = QLabel("From   :    ", objectName="from")
		hb2.addWidget(self.fromAddr)
		
		self.fromLine = QLineEdit()
		hb2.addWidget(self.fromLine)
		
		hb3 = QHBoxLayout()
		vb.addLayout(hb3)
		self.subjek = QLabel("Subjek :   ", objectName="subjek")
		hb3.addWidget(self.subjek)
		
		self.subjekLine = QLineEdit()
		hb3.addWidget(self.subjekLine)
		
		
		self.text = QLabel("Pesan : ", objectName="pesan")
		self.text.setAlignment(Qt.AlignCenter)
		vb.addWidget(self.text)
		
		self.textLine = QTextEdit()
		vb.addWidget(self.textLine)
		
		self.buttonKirim = QPushButton("Kirim", objectName = "kirim")
		vb.addWidget(self.buttonKirim)
		self.buttonKirim.clicked.connect(self.kirim)
	def kirim(self):
		fromaddr = self.fromLine.text()
		toaddr = self.toLine.text()
		pesan = self.textLine.toPlainText()
		subjek = self.subjekLine.text()
		
		try:
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = subjek
			msg.attach(MIMEText(pesan, 'plain'))
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			password = "PASSWORD ANDA "
			server.login(fromaddr, password)
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			self.berhasil()
		except:
			self.gagal()
			
			
		
		
		
			
	def gagal(self):
		msg = QMessageBox()
		msg.setWindowTitle("Gagal !!")
		msg.setText("Gagal Mengirim ..")
		msg.exec_()
	
	def berhasil(self):
		msg = QMessageBox()
		msg.setWindowTitle("Berhasil !!")
		msg.setText("Berhasil Mengirim")
		msg.exec_()
		



		
		



stylesheet="""
#Label{
   color:red;
   font-weight:bold;
}
#kirim{
	color:darkred;
	background-color:lightblue;
	padding:20;
}
#to{
	color:blue;
}
#from{
	color:blue;

}

#pesan{
	font-weight=bold;
	color:blue;
	background-color:lightblue;
	padding:20;
	font-size:50px;
}
#subjek{
	color:blue;
}
"""


def main():
	app = QApplication(sys.argv)
	app.setStyleSheet(stylesheet)
	gui = KirimEmail()
	gui.show()
	
	
	app.exec_()


if __name__ == "__main__":
	main()