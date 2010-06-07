# TODO: ...
class SQLCompiler(object):
    def __init__(self, query, connection, using):
        self.query = query
        self.connection = connection
        self.using = using


class SQLInsertCompiler(SQLCompiler):
    def insert(self, return_id=False):
        values = dict([
            (c, v)
            for c, v in zip(self.query.columns, self.query.params)
        ])
        if self.query.model._meta.pk.column in values:
            values["_id"] = values.pop(self.query.model._meta.pk.column)
        return self.connection.db[self.query.model._meta.db_table].insert(values)