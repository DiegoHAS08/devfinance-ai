import datetime

def format_currency(value):
    return f"R$ {value:.2f}"

def today_date():
    return datetime.date.today()

def validate_expense(title, amount):
    if not title:
        return False, "Título não pode ser vazio"

    if amount <= 0:
        return False, "Valor precisa ser maior que 0"

    return True, "OK"