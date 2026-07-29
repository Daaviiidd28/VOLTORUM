# -*- coding: utf-8 -*-
"""Componentes compartidos para generar las páginas de voltorum-web."""

SITE_NAME = "Voltorum"
DOMAIN = "https://voltorum.com"

def rel(depth, path=""):
    """Prefijo relativo según profundidad (0 = raíz)."""
    return ("../" * depth) if depth else "./"

NAV_LINKS = [
    ("servicios/", "Servicios"),
    ("comunidades/", "Comunidades"),
    ("negocios/", "Negocios"),
    ("sobre-voltorum/", "Sobre Voltorum"),
    ("contacto/", "Contacto"),
]

def nav_html(depth, active=""):
    r = rel(depth)
    links = []
    for href, label in NAV_LINKS:
        full = r + href
        cls = ' class="on-page"' if href.rstrip("/") == active else ""
        links.append(f'    <a href="{full}"{cls}>{label}</a>')
    links_html = "\n".join(links)
    logo = r + "img/isotipo-negro.png"
    home = r
    return f'''<nav class="nav" id="nav">
  <a href="{home}" class="brand"><img src="{logo}" width="1044" height="1476" alt="Voltorum"><span>Voltorum</span></a>
  <button class="burger" id="burger" aria-label="Menú" aria-expanded="false"><i></i><i></i><i></i></button>
  <div class="nav-r" id="navr">
{links_html}
    <a class="pill" href="{r}contacto/">Solicitar presupuesto</a>
  </div>
</nav>'''

def breadcrumbs_html(depth, items):
    """items: list of (label, href_or_None) — último sin href."""
    r = rel(depth)
    parts = []
    for i, (label, href) in enumerate(items):
        if href:
            parts.append(f'<a href="{r}{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
        if i < len(items) - 1:
            parts.append('<span class="mg-sep">/</span>')
    return f'<nav class="migas" aria-label="Ruta"><div class="wrap">{" ".join(parts)}</div></nav>'

def footer_html(depth):
    r = rel(depth)
    logo = r + "img/isotipo-negro.png"
    return f'''<footer>
  <div class="wrap">
    <div class="f-top">
      <div>
        <a href="{r}" class="brand"><img src="{logo}" width="1044" height="1476" alt="Voltorum"><span>Voltorum</span></a>
        <p style="color:var(--ink-2);font-size:.86rem;max-width:32ch;margin-top:12px">Electricistas en Madrid: instalaciones, averías y mantenimiento.</p>
      </div>
    </div>
    <div class="f-cols">
        <div>
          <h4>Servicios</h4>
          <ul>
            <li><a href="{r}servicios/averias-electricas/">Averías eléctricas</a></li>
            <li><a href="{r}servicios/instalaciones-electricas/">Instalaciones eléctricas</a></li>
            <li><a href="{r}servicios/cuadros-electricos/">Cuadros eléctricos</a></li>
            <li><a href="{r}servicios/iluminacion-led/">Iluminación LED</a></li>
            <li><a href="{r}servicios/">Ver todos los servicios</a></li>
          </ul>
        </div>
        <div>
          <h4>Clientes</h4>
          <ul>
            <li><a href="{r}comunidades/">Comunidades</a></li>
            <li><a href="{r}negocios/">Negocios y locales</a></li>
            <li><a href="{r}sobre-voltorum/">Sobre Voltorum</a></li>
            <li><a href="{r}contacto/">Contacto</a></li>
          </ul>
        </div>
        <div>
          <h4>Contacto</h4>
          <ul>
            <li><a data-cfg-href="tel" data-cfg="telefono_visible" href="#">[TELÉFONO]</a></li>
            <li><a data-cfg-href="whatsapp" href="#">WhatsApp</a></li>
            <li><a data-cfg-href="email" data-cfg="email" href="#">[EMAIL]</a></li>
            <li><span>Madrid</span></li>
          </ul>
        </div>
        <div>
          <h4>Legal</h4>
          <ul>
            <li><a href="{r}aviso-legal/">Aviso legal</a></li>
            <li><a href="{r}privacidad/">Privacidad</a></li>
            <li><a href="{r}cookies/">Cookies</a></li>
          </ul>
        </div>
    </div>
    <div class="f-bot">
      <span>&copy; <span id="anio"></span> Voltorum &middot; Electricidad y mantenimiento</span>
      <span>Madrid</span>
    </div>
  </div>
</footer>'''

WA_FLOAT = '''<a class="wa" data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero pedir información." href="#" aria-label="Escribir por WhatsApp">
  <svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.1.2-.3.3-.4.1-.2 0-.4 0-.5C10 9 9.4 7.6 9.1 7c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-1 1-1 2.4s1 2.8 1.1 3c.1.2 2 3 4.8 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3z"/><path d="M12 2C6.5 2 2 6.5 2 12c0 1.9.5 3.6 1.5 5.2L2 22l4.9-1.3C8.4 21.5 10.1 22 12 22c5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.7 0-3.3-.5-4.7-1.3l-.3-.2-3.5.9.9-3.4-.2-.3C3.5 14.4 3 12.7 3 11c0-5 4-9 9-9s9 4 9 9-4 10-9 10z"/></svg>
  <span data-cfg="telefono_visible">[TELÉFONO]</span>
</a>'''

def gsap_scripts():
    return '''<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>'''

def head_html(depth, title, description, path, extra_ld="", noindex=False):
    r = rel(depth)
    canonical = f"{DOMAIN}/{path}"
    og_image = f"{DOMAIN}/img/og.jpg"
    robots = "noindex,nofollow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1"
    return f'''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0B0C0E">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Voltorum">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{r}img/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="{r}img/favicon-48.png">
<link rel="apple-touch-icon" href="{r}img/apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
{extra_ld}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/voltorum.css">
<script src="{r}js/config.js"></script>'''

def page(depth, title, description, path, body, active="", extra_ld="", extra_scripts="", noindex=False):
    r = rel(depth)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
{head_html(depth, title, description, path, extra_ld, noindex)}
</head>
<body id="top">

{nav_html(depth, active)}

{body}

{footer_html(depth)}
{WA_FLOAT}

{gsap_scripts()}
<script src="{r}js/site.js"></script>
<script>document.getElementById('anio').textContent = new Date().getFullYear();</script>
{extra_scripts}
</body>
</html>
'''
