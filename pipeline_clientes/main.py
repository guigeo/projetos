# -*- coding: utf-8 -*-
"""Módulo principal.
"""
from src.clientes import gera_clientes
import timeit
import datetime

# Recupera Anomes Dia
dt = datetime.date.today()
dt_str = dt.strftime('%Y%m%d')

path="C:/meu_git/projetos/pipeline_clientes/data/"

def main():
    start_time = timeit.default_timer()
    gera_clientes(path, dt_str)

    elapsed = timeit.default_timer() - start_time
    time_end = (elapsed / 60)
    print("Processo finalizado em: {:.2f} minutos".format(time_end))
    print("Arquivo do dia: " + dt_str + " gerado com sucesso!")

if __name__ == "__main__":
    main()