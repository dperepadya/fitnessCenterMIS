class QueryGenerator:
    def __init__(self):
        pass

    @staticmethod
    def format_value(value):
        if isinstance(value, str):
            return f"'{value}'"
        return str(value)

    # SELECT users.id AS user_id, users.name AS user_name
    # get_sql_select_query('users', {'id': 'user_id', 'name': 'user_name'}):
    @staticmethod
    def get_sql_select_query(table, params):
        result = " * "
        if params is not None and len(params) > 0:
            select_query = []
            for param, alias in params.items():
                select_str = f"{table}.{param} AS {alias}"
                select_query.append(select_str)
            result = ', '.join(select_query)
        return result

    # SELECT orders.id AS order_id, services.id AS service_id, fitness_centers.id AS fitness_center_id
    # get_sql_select_multitable_query({orders.id: order_id, services.id: service_id }):
    @staticmethod
    def get_sql_select_multi_query(params):
        result = " * "
        if params is not None and len(params) > 0:
            select_query = []
            for param, alias in params.items():
                select_str = f"{param} AS {alias}"
                select_query.append(select_str)
            result = ', '.join(select_query)
        return result

    # get_sql_where_query('users', {'id': 1, 'name': 'Tom'})
    @staticmethod
    def get_sql_where_query(table, params):
        where_conditions = [f"{table}.{key} = {QueryGenerator.format_value(value)}"
                            for key, value in params.items()]
        return ' AND '.join(where_conditions)

    # get_sql_where_query({'users.id': 1, 'users.name': 'Tom'})
    @staticmethod
    def get_sql_where_multi_query(params):
        where_conditions = [f"{key} = {QueryGenerator.format_value(value)}"
                            for key, value in params.items()]
        return ' AND '.join(where_conditions)

    # JOIN services ON orders.service_id = services.id
    # JOIN fitness_centers ON services.fitness_center_id = fitness_centers.id
    # get_sql_join_query('credentials', ['users', ...], {'client_id': 'id', ...})
    @staticmethod
    def get_sql_join_query(table, join_tables, params):
        result = ""
        if params is not None and len(params) > 0:
            join_query = []
            for i, join_table in enumerate(join_tables): # merged table
                foreign_key = list(params.keys())[i]  # foreign key
                join_id = list(params.values())[i]  # join_id
                join_str = f"{join_table} ON {table}.{foreign_key} = {join_table}.{join_id}"
                join_query.append(join_str)
            result = ' JOIN ' + ' JOIN '.join(join_query)
        return result

    @staticmethod
    def get_select_sql_query(table, params=None, where_conditions=None):
        select_query = '*'
        if params is not None:
            select_query = QueryGenerator.get_sql_select_query(table, params)
        query = f"SELECT {select_query} FROM {table}"
        if where_conditions is not None:
            where_query = QueryGenerator.get_sql_where_query(table, where_conditions)
            query += f" WHERE {where_query}"
        return query

    # get_select_sql_join_query('credentials', {'users.name': 'user_name'},
    # ['clients'], {'client_id': 'id'}, {'clients.id':1})
    @staticmethod
    def get_select_sql_join_query(table, params=None, join_tables=None, join_params=None,
                                  where_conditions=None):
        select_query = '*'
        if params is not None:
            select_query = QueryGenerator.get_sql_select_multi_query(params)
        join_query = ""
        if join_tables is not None and join_params is not None:
            join_query = QueryGenerator.get_sql_join_query(table, join_tables, join_params)
        query = f"SELECT {select_query} FROM {table}{join_query}"
        if where_conditions is not None:
            where_query = QueryGenerator.get_sql_where_multi_query(where_conditions)
            query += f" WHERE {where_query}"
        return query

    @staticmethod
    def get_insert_sql_query(table, params):
        columns = ', '.join(params.keys())
        values = [f"{QueryGenerator.format_value(value)}" for _, value in params.items()]
        insert_query = f"INSERT INTO {table} ({columns}) VALUES ({' , '.join(values)})"
        return insert_query

    @staticmethod
    def get_update_sql_query(table, params, where_conditions):
        # columns = ', '.join(params.keys())
        # values = [f"{QueryGenerator.format_value(value)}" for _, value in params.items()]
        set_query = []
        for i, join_table in enumerate(params):  # merged table
            param = list(params.keys())[i]
            value = list(params.values())[i]
            set_str = f"{param} = {QueryGenerator.format_value(value)}"
            set_query.append(set_str)
        set_result = ' SET ' + ' , '.join(set_query)

        update_query = f'UPDATE {table}' + set_result
        if where_conditions is not None:
            where_query = QueryGenerator.get_sql_where_query(table, where_conditions)
            update_query += f" WHERE {where_query}"

        return update_query

    @staticmethod
    def get_delete_sql_query(table, where_conditions):
        if table is not None and where_conditions is not None:
            where_query = QueryGenerator.get_sql_where_query(table, where_conditions)
            delete_query = f"DELETE FROM {table} WHERE {where_query}"
            return delete_query
        return None
