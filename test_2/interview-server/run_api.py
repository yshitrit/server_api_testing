import requests

class api_run():
    def __init__(self , i_url , i_pload):
        self.basic_url = i_url
        # Check if initial username & password are correct
        if not i_pload['username'] == 'test' and i_pload['password'] == '1234':
            raise KeyError("There is a problem with initial 'username' and 'password'!")
        self.pload = i_pload
        self.token = self.initial_connection_get_token()
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.token)}
        # self.get_list_of_polydata()
        # self.create_new_object()
        # self.get_object_by_id_number(2)
        # self.delete_object_by_id_number(3)
        # self.get_list_of_polydata()

    def initial_connection_get_token(self):
        endpoint = '/api/auth'
        r = requests.post(self.basic_url + endpoint, json = self.pload)
        # print(r.text)
        if r.ok:
            r_dictionary = r.json()
            print("r_dictionary = {}".format(r_dictionary))
            token_pass = r_dictionary['access_token']
            print("token_pass :{}".format(token_pass))
            return token_pass
        else:
            raise ValueError("Problem receiving Token")


    def get_list_of_polydata(self):
        endpoint = '/api/poly'
        self.list_of_polydata = requests.get(self.basic_url + endpoint , headers=self.headers)
        print(self.list_of_polydata.json())
        return self.list_of_polydata.json()


    def create_new_object(self):
        endpoint = '/api/poly'
        pload = { "data": [{"key": "key1","val": "val1","valType": "str"}]}
        r = requests.post(self.basic_url + endpoint, json=pload)
        self.new_object = r.json()
        print(self.new_object)
        return self.new_object


    def get_object_by_id_number(self, i_object_number):
        endpoint = '/api/poly/{}'.format(i_object_number)
        object = requests.get(self.basic_url + endpoint, headers=self.headers)
        print (object.json())
        return object.json()

    def delete_object_by_id_number(self, i_object_number):
        endpoint = '/api/poly/{}'.format(i_object_number)
        object = requests.delete(self.basic_url + endpoint, headers=self.headers)
        print(object.json())
        return object.json()


#----------------------------------------------------------------------------------
if __name__ == "__main__":
    pload = {'username': 'test', 'password': '1234'}
    basic_url = 'http://localhost:8000'
    api = api_run(i_url=basic_url ,i_pload= pload)





