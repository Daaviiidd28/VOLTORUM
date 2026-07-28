# CAMBIOS — de TratoClaro a Voltorum

Resumen de la adaptación realizada sobre una copia de TratoClaro-v14.zip.
El original no se ha tocado; todo el trabajo se hizo en una carpeta nueva
(`voltorum-web/`).

## Identidad y diseño

- **Marca**: TratoClaro → Voltorum, electricidad y mantenimiento en Madrid.
- **Logos**: procesados a partir de los dos PNG proporcionados (isotipo y
  logotipo completo) — fondo gris eliminado y generadas las versiones
  blanca y negra, además de favicons, icono de app y una imagen Open
  Graph propia. En la navegación y el footer se usa **solo el símbolo**
  (isotipo) seguido del nombre "Voltorum" en texto — no el logotipo
  completo con el descriptor "Electricidad y mantenimiento" incrustado
  en la imagen, tal y como pidió David.
- **Paleta**: idéntica a TratoClaro — fondo claro (`#E9EAEC`), tinta casi
  negra, acento azul (`#2F6BF0`), sin modificar. Corregido tras la
  primera entrega: se había interpretado "web oscura" como tema oscuro,
  pero David quería el mismo sistema visual que TratoClaro (colores y
  tipografías idénticos), así que se revirtió al 100%.
- **Tipografías, radios, animaciones de scroll (GSAP), estructura de
  cabecera/tarjetas/CTA**: conservadas de TratoClaro.

## Contenido

- Eliminado por completo: tasador de coches, calculadora de comisión,
  catálogo de vehículos, simulador de financiación, comparativas de
  concesionario, fichas de coche, bio de David Nieto y cualquier mención a
  compraventa de vehículos.
- Creado desde cero: todo el contenido de servicios eléctricos (averías,
  cuadros eléctricos, mantenimiento preventivo, revisión y documentación),
  páginas de audiencia (comunidades de propietarios, negocios y locales),
  proceso de trabajo en 4 pasos, ventajas, FAQ y formulario de contacto
  con los 9 campos solicitados.
- Se ha evitado explícitamente cualquier afirmación no verificable:
  no hay reseñas, número de clientes, años de experiencia, certificaciones,
  disponibilidad 24h, tarifas cerradas ni garantías extraordinarias
  inventadas. La sección de "trabajos realizados" está preparada pero
  vacía, a la espera de casos reales.
- Se explicita que **no todos los boletines caducan** — se explica que la
  necesidad de revisión o nueva documentación depende del estado,
  antigüedad, modificaciones o un requerimiento administrativo concreto,
  tal como pedía el briefing.
- Ningún certificado se promete sin inspección previa (recordado en la
  página de servicio correspondiente con un aviso destacado).

## Estructura técnica

- Mismo stack (HTML + CSS + JS vanilla, sin build), reutilizado tal cual.
- El CSS se limpió de los bloques específicos de coches que ya no se usan
  (calculadora de comisión, tasador, catálogo, ficha de coche,
  comparativa, simulador de financiación, métodos de pago), para no dejar
  código muerto relacionado con vehículos.
- Datos de contacto centralizados en `js/config.js` (nuevo, no existía en
  TratoClaro de esta forma) para que cambiar teléfono/email/WhatsApp/
  dominio se haga en un único sitio.
- No se ha copiado el `CNAME` de `tratoclaro.es`. La web está preparada
  para `voltorum.com` en metadatos (canonical, Open Graph, sitemap) pero
  el dominio no se conecta de forma irreversible — ver `README.md`.

## Backend de pagos (añadido después de la primera entrega)

- Nuevo: cobro de presupuestos con **Stripe Checkout**, mediante
  funciones serverless de Netlify (`netlify/functions/`):
  - `create-checkout-session.js` — crea la sesión de pago en Stripe.
  - `generar-enlace.js` — genera enlaces de pago firmados, protegido por
    contraseña.
  - `stripe-webhook.js` — registra la confirmación real del pago.
- Nuevas páginas: `/pagar/` (pantalla de pago), `/pagar/gracias/`,
  `/pagar/cancelado/`, y `/admin/` (herramienta interna para generar
  enlaces de pago). Ninguna de las cuatro está enlazada desde el menú
  principal ni en `sitemap.xml`, y llevan `noindex`.
- Los importes se firman con HMAC (`PAYMENT_LINK_SECRET`) para que nadie
  pueda cambiar el precio manipulando la URL — probado explícitamente
  (ver `CAMBIOS.md` → verificaciones).
- Nuevos archivos de configuración: `netlify.toml`, `package.json`,
  `.env.example`, `.gitignore`.
- La web sigue sin ningún dato de pago hardcodeado ni ninguna clave
  secreta en el código: todo se lee de variables de entorno de Netlify.

## Rutas creadas

| Ruta | Contenido |
|---|---|
| `/` | Home |
| `/servicios/` | Índice de servicios |
| `/servicios/averias-electricas/` | Averías y reparaciones |
| `/servicios/cuadros-electricos/` | Cuadros eléctricos y protecciones |
| `/servicios/mantenimiento-electrico/` | Mantenimiento preventivo |
| `/servicios/boletines-documentacion/` | Revisión, diagnóstico y documentación |
| `/comunidades/` | Electricidad para comunidades de propietarios |
| `/negocios/` | Electricidad para negocios y locales |
| `/sobre-voltorum/` | Sobre Voltorum |
| `/contacto/` | Formulario de contacto |
| `/aviso-legal/` | Aviso legal |
| `/privacidad/` | Política de privacidad |
| `/cookies/` | Política de cookies |
| `/pagar/` | Pantalla de pago de un presupuesto (Stripe Checkout) |
| `/pagar/gracias/` | Confirmación tras pago completado |
| `/pagar/cancelado/` | Aviso de pago cancelado |
| `/admin/` | Herramienta interna para generar enlaces de pago (no pública en el menú) |

## Verificaciones realizadas

- ✅ Búsqueda global sin resultados de "TratoClaro", "coche", "vehículo",
  "tasación", "financiación", "concesionario", el nombre del fundador
  anterior o su teléfono, salvo una línea de comentario interno en el CSS
  que documenta el origen del sistema visual (permitido por el briefing).
- ✅ 0 enlaces internos rotos en las 13 páginas (comprobado
  automáticamente, incluyendo `href`, y excluyendo los enlaces que se
  rellenan por JavaScript desde `config.js`).
- ✅ Versión móvil comprobada con un navegador headless a 390px de ancho:
  el menú hamburguesa abre y cierra correctamente.
- ✅ Formulario, acordeón de FAQ y botón flotante de WhatsApp probados de
  forma interactiva (clics simulados): funcionan y toman los datos de
  `config.js` correctamente.
- ✅ El logo y el resto de recursos locales cargan sin errores. Los únicos
  avisos detectados en consola corresponden a las fuentes de Google y al
  script de GSAP, bloqueados por la red restringida del entorno de
  desarrollo usado para las pruebas — no son un problema del sitio y
  cargarán con normalidad en un navegador real con acceso a internet.
- ✅ Backend de pagos probado con datos simulados: generación de enlace
  firmado, verificación de firma correcta, y **detección de manipulación
  del importe** (se probó a cambiar el importe en la URL manteniendo la
  firma original y la petición se rechaza con error 403, como se espera).
