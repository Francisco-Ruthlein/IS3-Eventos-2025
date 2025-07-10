from behave import given, when, then
from funciones import resta

@given('tengo los números {num1:d} y {num2:d}')
def step_given_numeros(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('los resto')
def step_when_resto(context):
    context.resultado = resta(context.num1, context.num2)

@then('el resultado debe ser {esperado:d}')
def step_then_resultado(context, esperado):
    assert context.resultado == esperado, f"Error: Esperado {esperado}, obtuvo {context.resultado}"