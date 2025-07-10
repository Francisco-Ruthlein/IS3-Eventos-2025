Feature: Multiplicación de dos números
  Scenario: Multiplicar dos números positivos
    Given tengo los números 4 y 5
    When los multiplico
    Then el resultado debe ser 20

  Scenario: Multiplicar por cero
    Given tengo los números 7 y 0
    When los multiplico
    Then el resultado debe ser 0