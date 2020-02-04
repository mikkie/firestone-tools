REM mongo 127.0.0.1/firestone --eval "db.getCollection('concepts').drop();"
src\LoadConcepts.py
mongoexport -d firestone -c concepts -o ../firestone-server/install/concepts.json