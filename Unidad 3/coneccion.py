db_connection = "127.0.0.1","5432","root","nomina"

for parametro in db_connection:
    print(parametro)
else:
    print("""El comando PostgreSQL es: 
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
        server=db_connection[0], port=db_connection[1], 
        user=db_connection[2], db_name=db_connection[3]))