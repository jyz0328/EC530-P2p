import sqlite3

# 连接到SQLite数据库
# 如果文件不存在，会自动在当前目录创建一个名为 'database.db' 的文件
conn = sqlite3.connect('database.db')

# 创建一个Cursor对象并通过它执行SQL语句
cursor = conn.cursor()

# 创建一个表，用于存储消息
# 包括消息ID、发送者、接收者和消息内容
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages(
    message_id INTEGER PRIMARY KEY,
    sender TEXT,
    receiver TEXT,
    message BLOB
);
''')

# 提交事务
conn.commit()

# 关闭Cursor和连接
cursor.close()
conn.close()

print("数据库已生成，并创建了必要的表。")

