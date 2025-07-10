Feature: Resta de dos números
  Como usuario
  Quiero restar dos números
  Para obtener el resultado correcto

  Scenario: Restar dos números positivos
    Given tengo los números 10 y 4
    When los resto
    Then el resultado debe ser 6

  Scenario: Restar un positivo y un negativo
    Given tengo los números 5 y -3
    When los resto
    Then el resultado debe ser 8