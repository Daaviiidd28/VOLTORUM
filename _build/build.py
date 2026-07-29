# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

import common
import home
import servicios_index
import servicios_detail
import audiencias
import sobre
import contacto
import legal
import pagar

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", relpath)

LD_LOCAL_BUSINESS = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":["LocalBusiness","ElectricalContractor"],"@id":"https://voltorum.com/#negocio","name":"Voltorum","url":"https://voltorum.com/","image":"https://voltorum.com/img/og.jpg","telephone":"+34611066820","email":"info@voltorum.com","priceRange":"€€","description":"Electricistas en Madrid especializados en instalaciones eléctricas, averías, cuadros eléctricos, iluminación LED y mantenimiento, para comunidades, negocios y particulares.","address":{"@type":"PostalAddress","addressLocality":"Madrid","addressRegion":"Madrid","addressCountry":"ES"},"areaServed":{"@type":"AdministrativeArea","name":"Comunidad de Madrid"}}</script>
'''

LD_FAQ_HOME = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"¿El presupuesto tiene algún coste?","acceptedAnswer":{"@type":"Answer","text":"No. El diagnóstico y el presupuesto están incluidos y se entregan por escrito antes de empezar cualquier trabajo."}},{"@type":"Question","name":"¿Todas las instalaciones necesitan un boletín nuevo?","acceptedAnswer":{"@type":"Answer","text":"No necesariamente. Depende del estado, la antigüedad, las modificaciones realizadas o un requerimiento administrativo concreto. Cada caso se valora tras inspeccionar la instalación."}},{"@type":"Question","name":"¿En qué zona trabajáis?","acceptedAnswer":{"@type":"Answer","text":"Madrid capital y municipios cercanos."}}]}</script>
'''

def breadcrumb_ld(items):
    els = []
    for i, (name, url) in enumerate(items, start=1):
        entry = f'{{"@type":"ListItem","position":{i},"name":"{name}"'
        if url:
            entry += f',"item":"{url}"'
        entry += '}'
        els.append(entry)
    return '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[' + ",".join(els) + ']}</script>\n'

# ── / ──────────────────────────────────────────────────────────
write("index.html", common.page(
    depth=0,
    title="Electricistas en Madrid | Voltorum",
    description="Empresa de electricidad en Madrid especializada en instalaciones eléctricas, averías, cuadros eléctricos, iluminación LED, mantenimiento y comunidades de propietarios. Presupuesto gratuito.",
    path="",
    body=home.body(),
    active="",
    extra_ld=LD_LOCAL_BUSINESS + LD_FAQ_HOME,
))

# ── /servicios/ ───────────────────────────────────────────────
write("servicios/index.html", common.page(
    depth=1,
    title="Servicios eléctricos en Madrid | Voltorum",
    description="Averías, cuadros eléctricos, mantenimiento preventivo y documentación eléctrica en Madrid. Presupuesto por escrito tras revisar la instalación.",
    path="servicios/",
    body=servicios_index.body(),
    active="servicios",
    extra_ld=breadcrumb_ld([("Inicio","https://voltorum.com/"),("Servicios",None)]),
))

# ── /servicios/*/  (4 detail pages) ─────────────────────────────
detail_pages = [
    ("servicios/averias-electricas/", "Averías eléctricas en Madrid | Voltorum",
     "Diagnóstico y reparación de averías eléctricas en Madrid: cortes, diferenciales que saltan, enchufes o puntos de luz sin funcionar.",
     servicios_detail.averias()),
    ("servicios/instalaciones-electricas/", "Instalaciones eléctricas en Madrid | Voltorum",
     "Instalaciones eléctricas nuevas y reformas completas en Madrid, para vivienda, negocio o comunidad. Presupuesto gratuito.",
     servicios_detail.instalaciones()),
    ("servicios/cuadros-electricos/", "Cuadros eléctricos y protecciones en Madrid | Voltorum",
     "Revisión, ampliación y sustitución de cuadros eléctricos, magnetotérmicos y diferenciales en Madrid.",
     servicios_detail.cuadros()),
    ("servicios/iluminacion-led/", "Iluminación LED en Madrid | Voltorum",
     "Sustitución e instalación de iluminación LED en Madrid, para reducir el consumo sin perder luz.",
     servicios_detail.iluminacion_led()),
    ("servicios/enchufes-e-interruptores/", "Enchufes e interruptores en Madrid | Voltorum",
     "Cambio, ampliación y reparación de enchufes e interruptores en Madrid.",
     servicios_detail.enchufes()),
    ("servicios/puntos-de-luz/", "Puntos de luz en Madrid | Voltorum",
     "Nuevos puntos de luz o reubicación de los existentes en Madrid, con acabado limpio.",
     servicios_detail.puntos_de_luz()),
    ("servicios/mantenimiento-electrico/", "Mantenimiento eléctrico preventivo en Madrid | Voltorum",
     "Revisiones periódicas para comunidades y negocios en Madrid: detectar antes lo que luego sale caro.",
     servicios_detail.mantenimiento()),
    ("servicios/boletines-documentacion/", "Revisión y documentación eléctrica en Madrid | Voltorum",
     "Diagnóstico del estado real de la instalación y gestión de la documentación eléctrica que corresponda, tras inspección.",
     servicios_detail.boletines()),
]
for path, title, desc, body_html in detail_pages:
    slug = path.rstrip("/").split("/")[-1]
    write(path + "index.html", common.page(
        depth=2,
        title=title,
        description=desc,
        path=path,
        body=body_html,
        active="servicios",
        extra_ld=breadcrumb_ld([("Inicio","https://voltorum.com/"),("Servicios","https://voltorum.com/servicios/"),(title.split(" | ")[0],None)]),
    ))

# ── /comunidades/ ────────────────────────────────────────────
write("comunidades/index.html", common.page(
    depth=1,
    title="Electricidad para comunidades de propietarios | Voltorum",
    description="Electricidad para comunidades de propietarios en Madrid: zonas comunes, garajes y cuartos de instalaciones, coordinado con administradores de fincas.",
    path="comunidades/",
    body=audiencias.comunidades(),
    active="comunidades",
    extra_ld=breadcrumb_ld([("Inicio","https://voltorum.com/"),("Comunidades",None)]),
))

# ── /negocios/ ────────────────────────────────────────────────
write("negocios/index.html", common.page(
    depth=1,
    title="Electricidad para negocios y locales | Voltorum",
    description="Electricidad para negocios, locales y oficinas en Madrid, con los trabajos planificados para no interrumpir la actividad.",
    path="negocios/",
    body=audiencias.negocios(),
    active="negocios",
    extra_ld=breadcrumb_ld([("Inicio","https://voltorum.com/"),("Negocios",None)]),
))

# ── /sobre-voltorum/ ──────────────────────────────────────────
write("sobre-voltorum/index.html", common.page(
    depth=1,
    title="Sobre Voltorum | Electricidad y mantenimiento en Madrid",
    description="Voltorum: electricidad y mantenimiento en Madrid, con diagnóstico antes de presupuestar y trabajo documentado.",
    path="sobre-voltorum/",
    body=sobre.body(),
    active="sobre-voltorum",
    extra_ld=breadcrumb_ld([("Inicio","https://voltorum.com/"),("Sobre Voltorum",None)]),
))

# ── /contacto/ ────────────────────────────────────────────────
write("contacto/index.html", common.page(
    depth=1,
    title="Contacto | Voltorum — Electricidad y mantenimiento",
    description="Solicita presupuesto o cuenta tu avería eléctrica en Madrid. Respuesta revisando cada caso, sin respuestas automáticas.",
    path="contacto/",
    body=contacto.body(),
    active="contacto",
    extra_ld=breadcrumb_ld([("Inicio","https://voltorum.com/"),("Contacto",None)]),
))

# ── legales ───────────────────────────────────────────────────
write("aviso-legal/index.html", common.page(
    depth=1, title="Aviso legal | Voltorum", description="Aviso legal del sitio web de Voltorum.",
    path="aviso-legal/", body=legal.aviso_legal(), active="",
))
write("privacidad/index.html", common.page(
    depth=1, title="Política de privacidad | Voltorum", description="Política de privacidad y tratamiento de datos de Voltorum.",
    path="privacidad/", body=legal.privacidad(), active="",
))
write("cookies/index.html", common.page(
    depth=1, title="Política de cookies | Voltorum", description="Política de cookies del sitio web de Voltorum.",
    path="cookies/", body=legal.cookies(), active="",
))

# ── /pagar/ (pago de presupuestos con Stripe) ─────────────────
write("pagar/index.html", common.page(
    depth=1, title="Pagar presupuesto | Voltorum", description="Completa el pago de tu presupuesto con Voltorum de forma segura.",
    path="pagar/", body=pagar.pagar(), active="", noindex=True,
))
write("pagar/gracias/index.html", common.page(
    depth=2, title="Pago recibido | Voltorum", description="Pago recibido correctamente.",
    path="pagar/gracias/", body=pagar.gracias(), active="", noindex=True,
))
write("pagar/cancelado/index.html", common.page(
    depth=2, title="Pago cancelado | Voltorum", description="El pago no se ha completado.",
    path="pagar/cancelado/", body=pagar.cancelado(), active="", noindex=True,
))

# ── robots.txt ────────────────────────────────────────────────
write("robots.txt", "User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /pagar/\nSitemap: https://voltorum.com/sitemap.xml\n")

# ── sitemap.xml ───────────────────────────────────────────────
routes = [""] + [p for p, *_ in [("servicios/",)]] + \
         [p for p, *_ in detail_pages] + \
         ["comunidades/", "negocios/", "sobre-voltorum/", "contacto/", "aviso-legal/", "privacidad/", "cookies/"]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for r in routes:
    sm.append(f'  <url><loc>https://voltorum.com/{r}</loc></url>')
sm.append('</urlset>')
write("sitemap.xml", "\n".join(sm) + "\n")

# ── site.webmanifest ─────────────────────────────────────────
manifest = '''{
  "name": "Voltorum — Electricidad y mantenimiento",
  "short_name": "Voltorum",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0B0C0E",
  "theme_color": "#0B0C0E",
  "icons": [
    {"src": "/img/favicon-180.png", "sizes": "180x180", "type": "image/png"},
    {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}
  ]
}
'''
write("site.webmanifest", manifest)

print("\nBuild completo.")
