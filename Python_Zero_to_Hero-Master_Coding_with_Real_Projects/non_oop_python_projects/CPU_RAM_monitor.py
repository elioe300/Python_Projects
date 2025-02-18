import psutil
from plyer import notification
from time import sleep

def monitor_system_usage():
    """
    Monitorea el uso del CPU y la RAM, y envía notificaciones si los valores superan ciertos umbrales.

    El bucle se ejecuta continuamente y verifica el uso del CPU y la RAM. 
    Si el uso del CPU supera el 85%, envía una notificación. 
    Si el uso de la RAM supera el 90%, envía una notificación y luego espera 50 segundos antes de continuar.

    Args:
        None

    Returns:
        None
    """
    while True:
        CPU_usage = psutil.cpu_percent()
        RAM_usage = psutil.virtual_memory().percent

        if CPU_usage > 85:
            notification.notify(
                title="High CPU", 
                message=f"CPU usage is at {CPU_usage}%. Consider optimizing your analysis.", 
                timeout=10
            )
        elif RAM_usage > 90:
            notification.notify(
                title="High RAM", 
                message=f"RAM usage is at {RAM_usage}%. You might need more memory.", 
                timeout=10
            )
            