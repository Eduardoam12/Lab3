#!/usr/bin/env python 3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleController:
    def __init__(self):
        # Inicialización del nodo de ROS
        rospy.init_node('turtle_controller', anonymous=True)

        # Suscribirse al topic de la posición de la tortuga
        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)

        # Publicar al topic de comandos de velocidad de la tortuga
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # Variables para la posición deseada
        self.desired_x = 0.0
        self.desired_y = 0.0

        # Constantes del controlador proporcional
        self.Kp_linear = 1.0  # Ganancia proporcional lineal
        self.Kp_angular = 4.0  # Ganancia proporcional angular

        # Variables para la posición y orientación actual de la tortuga
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_theta = 0.0

    def pose_callback(self, data):
        # Callback para actualizar la posición y orientación actual de la tortuga
        self.current_x = data.x
        self.current_y = data.y
        self.current_theta = data.theta

    def get_desired_position(self):
        # Función para solicitar al usuario las coordenadas de la posición deseada
        self.desired_x = float(input("Ingrese la coordenada x de la posición deseada: "))
        self.desired_y = float(input("Ingrese la coordenada y de la posición deseada: "))

    def move_towards_desired_position(self):
        # Bucle infinito para controlar el movimiento de la tortuga
        while True:
            # Solicitar las coordenadas de la posición deseada al usuario
            self.get_desired_position()

            # Bucle infinito para alcanzar la posición deseada
            rate = rospy.Rate(10)  # 10 Hz
            while not rospy.is_shutdown():
                # Calcular el error de posición
                error_x = self.desired_x - self.current_x
                error_y = self.desired_y - self.current_y

                # Calcular la distancia y el ángulo hacia la posición deseada
                distance_to_goal = math.sqrt(error_x ** 2 + error_y ** 2)
                angle_to_goal = math.atan2(error_y, error_x)

                # Control proporcional (P) para la velocidad lineal
                linear_velocity = self.Kp_linear * distance_to_goal

                # Control proporcional (P) para la velocidad angular
                angular_velocity = self.Kp_angular * (angle_to_goal - self.current_theta)

                # Crear el mensaje Twist para enviar comandos de velocidad
                vel_msg = Twist()
                vel_msg.linear.x = linear_velocity
                vel_msg.angular.z = angular_velocity

                # Publicar el mensaje Twist
                self.velocity_publisher.publish(vel_msg)

                # Mostrar información de depuración
                rospy.loginfo("Distance to goal: {}, Angle to goal: {}".format(distance_to_goal, angle_to_goal))

                # Esperar antes de la próxima iteración
                rate.sleep()

if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.move_towards_desired_position()
    except rospy.ROSInterruptException:
        pass


