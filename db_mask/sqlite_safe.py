import sqlitecloud
from password_utils import get_decrypt_password


def connect():
    return sqlitecloud.connect("sqlitecloud://cp2dejwkvz.g5.sqlite.cloud:8860/coffee-shop?apikey=A0eyHwO1z6rgD77c5tRAZyb1bZ8LvJ75Vmlrnc9saAY")

connection = connect()
connection.execute("SELECT datetime('now');")
print(get_decrypt_password())        