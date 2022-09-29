export DJANGO_READ_DOT_ENV_FILE=True
python manage.py shell_plus
python manage.py runserver 7070

[1]

pg_dump --schema=common $DB_DATABASE > common.sql
pg_dump --schema=$DB_SCHEMA $DB_DATABASE > $DB_SCHEMA.sql

[2]
# REPLACE "common." by "public."
sed "s/common\./public\./g" common.sql common-replaced.sql

# REPLACE "$DB_SCHEMA." by "public."
sed "s/dbtest\./public\./g" $DB_SCHEMA.sql $DB_SCHEMA-replaced.sql

# restore to database
psql -d $DB_DATABASE < common-replaced.sql
psql -d $DB_DATABASE < $DB_SCHEMA-replaced.sql



## References
[1] DB dump & restore: https://www.dbrnd.com/2017/07/postgresql-take-schema-backup-or-copy-schema-into-another-server-pg_dump-restore/
[2] Sed replace: https://net2.com/how-to-replace-a-string-in-files-in-linux-the-simple-way/#using-sed-utility



## Django inspectdb
1. Configure DATABASES to connect to a custom schema (by default is `public`):
```python
DH_DATABASE_SCHEMA = "dbtest"
DATABASES["default"]["OPTIONS"] = {
    "options": "-c search_path=" + DH_DATABASE_SCHEMA
}
```
2. Run inspectdb and store it to a file (e.g. models.py):
```
./manage.py inspectdb > models.py
```

3. Run again with `common` schema
```
./manage.py inspectdb > models_common.py
```

4. Update Meta.db_table on all models according to their schema:
e.g. db_table = f'dbtest\".\"action_component'
e.g. db_table = f'common\".\"manufacturer'

Find & replace:
    match --> db_table = '
    replace --> db_table = f'{DH_SCHEMA}\".\"

Once you have finished inspecting database, remove schema option on DATABASES setting.

### Use shell_plus to query models
python manage.py shell_plus:
```
from dhango.models_common import *
```
