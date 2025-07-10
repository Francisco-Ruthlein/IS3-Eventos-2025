from behave import given, when, then
from funciones import multiplicacion

@given('tengo los números {num1:d} y {num2:d}')
def step_given_numeros(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('los multiplico')
def step_when_multiplico(context):
    context.resultado = multiplicacion(context.num1, context.num2)

@then('el resultado debe ser {esperado:d}')
def step_then_resultado(context, esperado):
    assert context.resultado == esperado, f"Error: Esperado {esperado}, obtuvo {context.resultado}"