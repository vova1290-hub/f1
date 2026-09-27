"""Начальная версия системы учёта коммерческих предложений."""

from datetime import date, timedelta


def calculate_final_amount(amount, discount_percent):
    """Рассчитать итоговую сумму предложения с учётом скидки."""
    if discount_percent < 0 or discount_percent > 100:
        return amount

    discount_amount = amount * discount_percent / 100
    return amount - discount_amount


def get_proposal_status(is_approved):
    """Вернуть статус коммерческого предложения."""
    if is_approved:
        return "Согласовано"

    return "Ожидает согласования"


def calculate_expiration_date(created_date, validity_days):
    """Рассчитать дату окончания действия предложения."""
    return created_date + timedelta(days=validity_days)


proposal_number = "КП-001"
client_name = "ООО Альфа"
amount = 150000.0
discount_percent = 10.0
created_date = date.today()
validity_days = 14
is_approved = False

final_amount = calculate_final_amount(amount, discount_percent)
status = get_proposal_status(is_approved)
expiration_date = calculate_expiration_date(created_date, validity_days)

print("СИСТЕМА УЧЁТА КОММЕРЧЕСКИХ ПРЕДЛОЖЕНИЙ")
print(f"Номер предложения: {proposal_number}")
print(f"Клиент: {client_name}")
print(f"Исходная сумма: {amount:.2f} руб.")
print(f"Скидка: {discount_percent}%")
print(f"Итоговая сумма: {final_amount:.2f} руб.")
print(f"Дата создания: {created_date}")
print(f"Действует до: {expiration_date}")
print(f"Статус: {status}")