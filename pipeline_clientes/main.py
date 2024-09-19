# -*- coding: utf-8 -*-
"""Módulo principal.
"""
from src.clientes import gera_clientes
import timeit
import datetime

# Recupera Anomes Dia
dt = datetime.date.today()
dt_str = dt.strftime('%Y%m%d')

def main():
    start_time = timeit.default_timer()
    gera_clientes(dt_str)

    elapsed = timeit.default_timer() - start_time
    time_end = (elapsed / 60)
    print("Processo finalizado em: {:.2f} minutos".format(time_end))

if __name__ == "__main__":
    main()