from PyQt5 import uic, QtWidgets
import mysql.connector
from random import randint

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='phrases'
)


def get_random_phrase():
    cursor = db.cursor()
    comand = 'SELECT * FROM phrases;'
    cursor.execute(comand)
    cursor.fetchall()
    total = cursor.rowcount
    random = randint(1, total)
    comand = f'SELECT sentence from phrases WHERE id = {random};'
    cursor.execute(comand)
    phrase = cursor.fetchall()[0][0]
    main_window.label.setText(phrase)


def write():
    write_window.show()

    write_window.pushButton.clicked.connect(set_text)
    write_window.pushButton_2.clicked.connect(close)


def set_text():
    text = write_window.textEdit.toPlainText()
    cursor = db.cursor()
    comand = f'INSERT INTO phrases (sentence) VALUES ("{text}");'
    cursor.execute(comand)
    db.commit()
    close()


def close():
    write_window.close()


app = QtWidgets.QApplication([])

main_window = uic.loadUi('main_window.ui')
write_window = uic.loadUi('write.ui')


main_window.pushButton.clicked.connect(get_random_phrase)
main_window.pushButton_2.clicked.connect(write)
main_window.show()
try:
    app.exec()
except FileNotFoundError:
    print('error')
