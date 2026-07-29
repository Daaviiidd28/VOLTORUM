# -*- coding: utf-8 -*-
"""Iconos de línea minimalistas (stroke=currentColor), estilo coherente con .ic"""

def _svg(inner, vb="0 0 24 24"):
    return f'<svg class="ic" viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>'

ICONS = {
    "rayo": _svg('<path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z"/>'),
    "cuadro": _svg('<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M8 8h1M8 12h1M8 16h1M12 7v10M16 8h1M16 12h1M16 16h1"/>'),
    "llave": _svg('<path d="M14.5 6.5a4 4 0 1 0-4 6.9L4 20l0 0 2 2 1.4-1.4M9.5 15l2-2"/><path d="M14.5 6.5 18 3l3 3-3.5 3.5"/>'),
    "documento": _svg('<path d="M7 3h7l4 4v14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/><path d="M14 3v4h4"/><path d="m9.5 14 2 2 3.5-4"/>'),
    "edificio": _svg('<path d="M5 21V5a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v16"/><path d="M13 10h5a1 1 0 0 1 1 1v10"/><path d="M8 8h.01M8 11h.01M8 14h.01M8 17h.01M17 14h.01M17 17h.01"/><path d="M3 21h18"/>'),
    "tienda": _svg('<path d="M4 10v10a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V10"/><path d="M2 6h20l-1.5 4a2 2 0 0 1-2 1.5H5.5a2 2 0 0 1-2-1.5L2 6Z"/><path d="M9 21v-6h6v6"/>'),
    "escudo": _svg('<path d="M12 3 4.5 6v5.5C4.5 16.5 7.7 20.4 12 21c4.3-.6 7.5-4.5 7.5-9.5V6L12 3Z"/><path d="m9 12 2 2 4-4.5"/>'),
    "reloj": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.3 2"/>'),
    "check": _svg('<circle cx="12" cy="12" r="9"/><path d="m8.5 12.3 2.4 2.4 4.6-5.4"/>'),
    "chat": _svg('<path d="M4 5h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H9l-4 4v-4H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Z"/>'),
    "lupa": _svg('<circle cx="10.5" cy="10.5" r="6.5"/><path d="m20 20-4.4-4.4"/>'),
    "recibo": _svg('<path d="M6 3h12v18l-2.5-1.5L13 21l-1-1.5L11 21l-2.5-1.5L6 21V3Z"/><path d="M9 8h6M9 12h6M9 16h4"/>'),
    "camara": _svg('<path d="M4 8h3l1.5-2h7L17 8h3a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1Z"/><circle cx="12" cy="13.5" r="3.5"/>'),
    "candado": _svg('<rect x="5" y="11" width="14" height="10" rx="1.5"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),
    "grafico": _svg('<path d="M4 20V4M4 20h16"/><path d="m8 16 3.5-4.5L14 14l5-6"/>'),
    "casa": _svg('<path d="M4 11 12 4l8 7"/><path d="M6 10v10a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V10"/><path d="M10 21v-6h4v6"/>'),
    "bombilla": _svg('<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.45 1 1.15 1.1 1.9l.1.8h5l.1-.8c.1-.75.5-1.45 1.1-1.9A6 6 0 0 0 12 3Z"/>'),
    "enchufe": _svg('<path d="M9 3v5M15 3v5"/><path d="M6 8h12v4a6 6 0 0 1-12 0V8Z"/><path d="M12 18v3"/>'),
    "estrella": _svg('<path d="m12 3 2.6 5.9 6.4.6-4.8 4.3 1.4 6.3L12 17l-5.6 3.1 1.4-6.3-4.8-4.3 6.4-.6L12 3Z"/>'),
    "telefono": _svg('<path d="M6.5 3h3l1.5 4-2 1.5a11 11 0 0 0 5.5 5.5L16 12l4 1.5v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4.5 5.2 2 2 0 0 1 6.5 3Z"/>'),
}

def icon(name):
    return ICONS.get(name, ICONS["rayo"])
