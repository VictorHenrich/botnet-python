from start import server


@server.start
def run_api():
    import controllers

    server.http.start()

#@server.start
def migrate_database():
    import models

    server.database.migrate()


server.start_server()





