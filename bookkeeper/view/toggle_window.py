"""
Функция переключения экрана. Используется для скрытия данных
"""

def toggle_window(window):
    if window.isVisible():
        window.hide()
    else:
        window.show()