
def get_sql_select_string(table, params):
    return ', '.join([f"{table}.{key}" for key in params.keys()])


def get_sql_where_string(table, params):
    return ' AND '.join([f"{table}.{key} = ?" for key in params.keys()])


def get_sql_join_string(table, join_tables, params):
    join_string = []
    for i, join_table in enumerate(join_tables): # merged table
        foreign_key = list(params.keys())[i]  # foreign key
        join_id = list(params.values())[i]  # join_id
        join_str = f"{join_table} ON {table}.{foreign_key} = {join_table}.{join_id}"
        join_string.append(join_str)

    return ' JOIN '.join(join_string)

def generate_select_sql_query(table, params, where_conditions):
    select_string = get_sql_select_string(table, params)
    where_string = get_sql_where_string(table, where_conditions)
    query = f"SELECT {select_string} FROM {table} WHERE {where_string}"
    values = list(where_conditions.values())
    return query, values
