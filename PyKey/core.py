import ComicScript # Requisito de Emiliano
import keyboard
import threading
import time

class PyKeySystem:
    def __init__(self):
        self._keys_pressed_order = [] 
        self.key = ""
        self.F = ""
        self.hotkey = ""
        
        self._monitor_active = True
        self._running = True
        # Lista de control extendida
        self.especiales = ['ctrl', 'alt', 'shift', 'windows', 'tab', 'esc', 'delete', 'insert', 'alt gr']
        
        self._thread = threading.Thread(target=self._update_loop, daemon=True)
        self._thread.start()

    def _update_loop(self):
        while self._running:
            if self._monitor_active:
                try:
                    evento = keyboard.read_event()
                    name = evento.name.lower()

                    if evento.event_type == keyboard.KEY_DOWN:
                        if name not in self._keys_pressed_order:
                            self._keys_pressed_order.append(name)
                    
                    elif evento.event_type == keyboard.KEY_UP:
                        if name in self._keys_pressed_order:
                            self._keys_pressed_order.remove(name)

                    self._actualizar_variables()
                except:
                    pass
            time.sleep(0.001)

    def _actualizar_variables(self):
        actuales = list(self._keys_pressed_order)
        
        # 1. Identificamos qué tipo de teclas hay en la lista
        modificadores = [t for t in actuales if t in self.especiales]
        efes_list = [t.upper() for t in actuales if t.startswith('f') and len(t) > 1]
        
        # Teclas normales: NO son especiales, NO son Efes
        normales = [t for t in actuales if t not in self.especiales and t.upper() not in efes_list]

        # --- LÓGICA DE ASIGNACIÓN EXCLUSIVA ---

        # 1. Prioridad Efes: Siempre a su variable
        self.F = ", ".join(efes_list)

        # 2. Lógica de Hotkey vs Key
        if any(m in ['ctrl', 'alt', 'windows', 'shift'] for m in modificadores):
            # Si hay un modificador de "combos", TODO se va a hotkey
            self.hotkey = ", ".join(actuales)
            self.key = "" 
        else:
            # Si no hay combo, las especiales solas (Esc, Space) van a hotkey
            self.hotkey = ", ".join(modificadores)
            # Y las normales van a key (Aquí ya no entran las Efes por el filtro anterior)
            self.key = ", ".join(normales)

    def Monitor(self, state: bool):
        self._monitor_active = state
        if not state:
            self._keys_pressed_order = []
            self.key = self.F = self.hotkey = ""

PyKey = PyKeySystem()