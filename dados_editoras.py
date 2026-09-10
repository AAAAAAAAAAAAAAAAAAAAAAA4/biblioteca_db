import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela editoras
conn.execute("DROP TABLE IF EXISTS editoras")

<<<<<<< HEAD
#cria a tabela editoras
=======
#cria a tabela esditoras
>>>>>>> 6a9659fd7abacd3afae1464ca75e701ddb0ba2d2
conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#inserindo os registros na tabela editoras
conn.executemany("INSERT INTO editoras(nome) VALUES(?)",
                 [("Moderna",), ("Nova",)])

#confirmando a criação e os inserts da tabela editoras.
<<<<<<< HEAD
conn.commit()
=======
conn.commit()

>>>>>>> 6a9659fd7abacd3afae1464ca75e701ddb0ba2d2
