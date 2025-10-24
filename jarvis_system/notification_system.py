from plyer import notification

def notify_start():
    notification.notify(
        title="Jarvis",
        message="Jarvis is listening!\nSay 'jarvis' to start and 'stop jarvis' to stop.",
        timeout=5
    )

def notify_timeout():
    notification.notify(
        title="Jarvis",
        message="No activity detected. Shutting down Jarvis.",
        timeout=5
    )
    print("No activity detected. Shutting down Jarvis.")

def notify_stop():
    notification.notify(
        title="Jarvis",
        message="Jarvis closed.",
        timeout=5
    )
    print("Jarvis closed")