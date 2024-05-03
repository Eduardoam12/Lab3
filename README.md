# Lab3
Report of third laboratory
# Resumen 
En esta practica se realizo un controlador en el cual la tortuga hace un bucle de control infinito que se ejecuta continuamente mientras el nodo de ROS esté activo. En cada iteración, calculamos la distancia y el ángulo hacia la posición deseada. Utilizando un controlque elegimos, en este caso se proporciona un control (P), convertimos estos errores en velocidades lineal y angular para la tortuga. El controlador ajusta continuamente las velocidades de la tortuga hasta que se alcanza la posición deseada. Además, implementamos una función para hacer spawn de la tortuga en la posición deseada antes de iniciar el movimiento.
# Introduccion
En el ámbito de la robótica, el control de movimiento es un aspecto fundamental para lograr que los robots se desplacen de manera efectiva en su entorno. En este practica, abordamos este desafío utilizando el entorno de Robot Operating System (ROS) y su simulador de robot Turtlesim. La tortuga en Turtlesim sirve como una plataforma de prueba ideal para desarrollar y probar algoritmos de control de movimiento antes de implementarlos en robots físicos.

El objetivo principal de este practica es diseñar un controlador que permita a la tortuga navegar desde su posición actual hasta una posición deseada especificada por el usuario. Para lograr esto, empleamos conceptos de control proporcional (P) y trigonometría para calcular las velocidades lineal y angular necesarias que guíen a la tortuga hacia el objetivo de manera suave y precisa.

Además del control de movimiento, exploramos la funcionalidad de spawn de Turtlesim para colocar la tortuga en la posición deseada antes de iniciar el movimiento. Este aspecto es crucial para garantizar que la tortuga comience su trayectoria desde la ubicación correcta.

En resumen, este practica representa un paso fundamental en el desarrollo de algoritmos de control de movimiento para robots móviles, proporcionando una introducción práctica al diseño y la implementación de controladores en entornos simulados de ROS.
# Conflictos
    1.- Calcular y mostrar en pantalla la DTG y ATG.
    2.- No mover el robot, hacer spawn del mismo en la posición Goal.
    3.- Explicar el mapeo necesario para las velocidades.
    4.- Usar un controlador (libre) para llevar a la tortuga a la posición deseada, hacerlo en bucleinfinito.
# Conclusion
En esta practica, hemos demostrado cómo implementar un controlador efectivo para guiar una tortuga simulada en Turtlesim hacia una posición deseada en el entorno de ROS. Utilizando técnicas de control proporcional y trigonometría, logramos calcular las velocidades lineal y angular necesarias para dirigir suavemente la tortuga hacia el objetivo.

Nuestro enfoque proporciona una base sólida para futuros desarrollos en el control de movimiento de robots móviles. La capacidad de hacer spawn de la tortuga en la posición deseada también garantiza que pueda iniciar su movimiento desde la ubicación correcta, lo que es esencial para una navegación precisa.

En resumen, esta practica ilustra cómo aplicar conceptos teóricos de control en un entorno práctico, proporcionando una valiosa experiencia en el diseño y la implementación de controladores de movimiento en entornos simulados de ROS. Este conocimiento es fundamental para el desarrollo de sistemas robóticos más avanzados en el futuro.

