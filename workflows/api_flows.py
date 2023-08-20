import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data('Url_Api')
user = get_data('UserName_Api')
password = get_data('Password_Api')


class APIFlows:
    @staticmethod
    @allure.step('Get value from grafana api flow')
    def get_value_from_api(nodes):
        response = APIActions.get(url + 'api/teams/search', user, password)
        return APIActions.extract_value_from_response(response, nodes)

    @staticmethod
    @allure.step('Create new team in Grafana flow')
    def create_team(name, email):
        payload = {'name': name, 'email': email}
        status_code = APIActions.post(url + 'api/teams', payload, user, password)
        return status_code

    @staticmethod
    @allure.step('Update team in Grafana flow')
    def update_team(name, email, id):
        payload = {'name': name, 'email': email}
        status_code = APIActions.put(url + 'api/teams/' + str(id), payload, user, password)
        return status_code

    @staticmethod
    @allure.step('Delete team in Grafana flow')
    def delete_team(id):
        status_code = APIActions.delete(url + 'api/teams/' + str(id), user, password)
        return status_code