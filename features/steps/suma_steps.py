from behave import given, when, then

@given('tengo los números {a:d} y {b:d}')
def step_given_numbers(context, a, b):
    context.a = a
    context.b = b

@when('los sumo')
def step_when_sum(context):
    context.resultado = context.a + context.b

@then('el resultado debe ser {esperado:d}')
def step_then_result(context, esperado):
    assert context.resultado == esperado