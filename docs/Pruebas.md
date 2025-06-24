# Gestión de calidad del producto software: pruebas

Ingeniería de Software III / Actualidad Informática  
Lic. en Sistemas de Información / Analista en Sistemas de Computación  
FCEQyN - UNaM

## Introducción

La mayoría de los lenguajes tienen una (o más librerías) para realizar pruebas vía código.
En este caso, se va a continuar trabajando bajo Python utilizando la librería PyTest.

Referencia: [Effective Python Testing With pytest](https://realpython.com/pytest-python-testing/)

## Tests unitarios y de integración

Los archivos de **test** tienen que estar en una carpeta con ese mismo nombre para que puedan ser identificados y ejecutados de forma automática. Además de tener en su nombre de archivo el prefijo "test_". Tanto esta carpeta como la del código a probar deberían ser módulos por lo que se agrega un archivo **__init__.py**.

Los tests en sí van a ser funciones que van a hacer la invocación a una función (para el caso de tests unitarios) o varias funciones entrelazadas (para el caso de tests de integración). En cualquier caso, se busca que se obtenga el valor correcto al ejecutar la función en sí, para ello se utiliza la instrucción **assert** que realiza esta comparación y, en caso correcto, el test _pasa_ (PASS) y en caso que la comparación no sea correcta _falla_ (FAIL).

En el ejemplo se hace uso de un decorador de funciones para parametrizar un test con varios casos de entradas de datos.

## Aplicacción de BDD

El Desarrollo Guiado por Comportamiento es una extensión de TDD (_Test Driven Development_) que, en este escenario, permite escribir especificaciones en lenguaje natural y ejecutar pruebas automatizadas basadas en ellas. Para ello se utiliza un DLS (_Domain Specific Language_) como **Gherkin** que podría ser utiilzado para re-escribir los criterios de aceptación de una historia de usuario.