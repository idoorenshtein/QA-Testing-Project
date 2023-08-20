import allure
import test_cases.conftest as conf


class DBActions:
    @staticmethod
    @allure.step('Query Builder')
    # Example: "Select user,password FROM Employees WHERE comments = 'correct'
    def query_builder(columns, table, where_name, where_value):
        cols = ','.join(columns)
        query = "SELECT " + cols + " FROM " + table + " WHERE " + where_name + " = '" + where_value + "'"
        return query

    @staticmethod
    @allure.step('Get Query Result')
    def get_query_result(columns, table, where_name, where_value):
        query = DBActions.query_builder(columns, table, where_name, where_value)
        db_cursor = conf.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fetchall()
        return result  # Returns List of Tuples
