"""
modules/common.py - Functions globais
    
"""

from datetime import datetime


def display_error_message(message):
    print(f"Erro: {message}")


def format_currency(value):
    return f"R$ {value:.2f}"


def get_current_date():
    """
    Retorna a data e hora atual formatada.

    Returns:
        str: Data e hora atual no formato "dd/mm/aaaa HH:MM:SS"
    """
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return current_date
