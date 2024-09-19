from faker import Faker
import random
import pandas as pd


def gera_clientes(data_dia):

    fake = Faker("pt_BR") 
    concatid = 'ID'
    idcode,name, phone_number, company, city, state, job, age = [[] for k in range(0,8)] 

    for row in range(0,1000):
        idcode.append(concatid + str(fake.unique.random_int(min=111111, max=999999)))
        name.append(fake.name())
        city.append(fake.city())
        state.append(fake.state())
        job.append(fake.job())
        company.append(fake.company())
        phone_number.append(fake.phone_number())
        age.append(random.randint(20,80))

    d = {"ID_CODE":idcode,"NOME":name,"CIDADE":city,"UF":state,"IDADE":age,"TELEFONE":phone_number,"CARGO":job,"EMPRESA":company}
    df = pd.DataFrame(d)
    df.to_csv('Clientes_' + data_dia + '.csv', index = False, sep=';')

if __name__ == "__main__":
    gera_clientes()