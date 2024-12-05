import re
from validate_docbr import CPF
from validate_email import validate_email

def validate_cpf(number_cpf):
    cpf = CPF()
    cpf_valid = cpf.validate(number_cpf)
    return cpf_valid

def validate_email(email):
    email = 'example@example.com'
    email_valid = validate_email(email)
    return email_valid

def validate_username(username):
    return not username.isalpha()

def celular_invalido(phone_number):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, phone_number)
    return not response