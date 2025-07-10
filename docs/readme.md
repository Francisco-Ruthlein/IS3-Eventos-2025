# Reporte de Behave - Suma, Resta y Multiplicación

## Feature: Multiplicación de dos números

### Scenario: Multiplicar dos números positivos ✔️
- **Given:** tengo los números 4 y 5
- **When:** los multiplico
- **Then:** el resultado debe ser 20

### Scenario: Multiplicar por cero ✔️
- **Given:** tengo los números 7 y 0
- **When:** los multiplico
- **Then:** el resultado debe ser 0

---

## Feature: Resta de dos números

### Scenario: Restar dos números positivos ✔️
- **Given:** tengo los números 10 y 4
- **When:** los resto
- **Then:** el resultado debe ser 6

### Scenario: Restar un positivo y un negativo ✔️
- **Given:** tengo los números 5 y -3
- **When:** los resto
- **Then:** el resultado debe ser 8

---

## Feature: Suma de dos números

### Scenario: Sumar dos números positivos ❌
- **Given:** tengo los números 3 y 5
- **When:** los sumo
- **Then:** el resultado debe ser 8
- **Error:** `AttributeError: 'Context' object has no attribute 'a'`

### Scenario: Sumar un número positivo y un número negativo ❌
- **Given:** tengo los números 7 y -2
- **When:** los sumo
- **Then:** el resultado debe ser 5
- **Error:** `AttributeError: 'Context' object has no attribute 'a'`

### Scenario: Sumar dos números negativos ❌
- **Given:** tengo los números -4 y -6
- **When:** los sumo
- **Then:** el resultado debe ser -10
- **Error:** `AttributeError: 'Context' object has no attribute 'a'`