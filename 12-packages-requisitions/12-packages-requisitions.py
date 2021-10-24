import requests


def get_cep(cep):
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    response = requests.get(url).json()
    print(response)


if __name__ == '__main__':
    get_cep('13210906')

