import time
from plyer import notification

def pomodoro_timer():
    """
    Función para ejecutar el ciclo de estudio Pomodoro durante 25 minutos.
    Envía una notificación al inicio y al final del ciclo.
    """
    user_time = 1500  # 25 minutos en segundos
    notification.notify(
        title="Alerta de pomodoro.",
        message="Comienza el ciclo de estudio.",
        timeout=10
    )
    while user_time > 0:  # Usar '>' en lugar de '>=' para evitar un segundo extra
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        user_time -= 1

    notification.notify(
        title="Alerta de pomodoro.",
        message="Se ha terminado el ciclo de estudio.",
        timeout=10
    )

def rest_timer():
    """
    Función para ejecutar el ciclo de descanso durante 5 minutos.
    Envía una notificación al inicio y al final del ciclo.
    """
    user_time = 300  # 5 minutos en segundos
    notification.notify(
        title="Alerta de pomodoro.",
        message="Comienza el ciclo de descanso.",
        timeout=10
    )
    while user_time > 0:  # Usar '>' en lugar de '>=' para evitar un segundo extra
        mins, secs = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        user_time -= 1

    notification.notify(
        title="Alerta de pomodoro.",
        message="El ciclo de descanso ha terminado.",
        timeout=10
    )

if __name__ == "__main__":
    # Preguntar al usuario la cantidad de ciclos Pomodoro que quiere realizar
    cycles = int(input("Introduzca la cantidad de ciclos pomodoro que quiera realizar: "))
    for cycle in range(cycles):
        pomodoro_timer()
        rest_timer()
