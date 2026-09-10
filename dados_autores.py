import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

<<<<<<< HEAD
#apaga a tabela editoras
=======
#apaga a tabela autores
>>>>>>> 6a9659fd7abacd3afae1464ca75e701ddb0ba2d2
conn.execute("DROP TABLE IF EXISTS autores")

#cria a tabela autores
conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#inserindo os registros na tabela autores
conn.executemany("INSERT INTO autores(nome) VALUES(?)",
<<<<<<< HEAD
                 [("Horstman",), ("Deitel",)])

#confirmando a criação e os inserts da tabela autores.
conn.commit()
#
=======
                 [("Kamome Shirahama",), ("Minhau",)])

#confirmando a criação e os inserts da tabela autores.
conn.commit()

>>>>>>> 6a9659fd7abacd3afae1464ca75e701ddb0ba2d2
