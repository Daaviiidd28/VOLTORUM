# PENDIENTES — antes de publicar

Todo lo que sigue es contenido **deliberadamente incompleto** porque no se
disponía del dato real y no se quería inventarlo. Búscalo con Ctrl+F por
`[` en cada archivo si quieres localizar cada placeholder exacto.

## 0. Backend de pagos (Stripe) — nuevo, hay que configurarlo

Se ha añadido un backend mínimo (funciones serverless de Netlify) para
cobrar presupuestos con Stripe. Antes de poder usarlo hay que:

1. Crear una cuenta en [stripe.com](https://stripe.com) (o usar la que ya
   tengas) y activarla para cobros reales cuando quieras pasar de pruebas
   a producción.
2. Copiar la **clave secreta** (Developers → API keys → Secret key) y
   configurarla como variable de entorno `STRIPE_SECRET_KEY` en Netlify
   (Site configuration → Environment variables). Empieza usando la clave
   de **test** (`sk_test_...`) hasta comprobar que todo funciona.
3. Generar dos secretos propios y configurarlos también como variables de
   entorno en Netlify:
   - `PAYMENT_LINK_SECRET`: cualquier cadena aleatoria larga (por ejemplo,
     con `openssl rand -hex 32`). Protege los enlaces de pago para que
     nadie pueda cambiar el importe editando la URL.
   - `ADMIN_PASSWORD`: la contraseña que se pedirá en `/admin/` para
     generar enlaces de pago.
4. Configurar `SITE_URL` = `https://voltorum.com` (o el dominio que se use
   mientras tanto, ej. la URL que da Netlify).
5. (Opcional pero recomendado) Configurar el webhook de Stripe: en el
   panel de Stripe, Developers → Webhooks → Add endpoint, con la URL
   `https://TUDOMINIO/.netlify/functions/stripe-webhook` y el evento
   `checkout.session.completed`. Copiar el "Signing secret" que te da
   Stripe (`whsec_...`) a la variable `STRIPE_WEBHOOK_SECRET`. Sin esto,
   los pagos se cobran igual, pero no queda registro automático del
   evento en los logs.
6. Ver `README.md`, sección "Backend de pagos", para el flujo completo de
   cómo generar y enviar un enlace de pago a un cliente.

**Importante**: mientras `STRIPE_SECRET_KEY` sea una clave de test
(`sk_test_...`), los pagos son simulados y no se cobra dinero real — útil
para probar todo el flujo antes de activarlo de verdad.

## 1. Datos de contacto (`js/config.js`) — obligatorio antes de publicar

- [ ] `telefono_visible` y `telefono_href`
- [ ] `whatsapp_numero` (formato internacional sin el `+`, ej. `34600000000`)
- [ ] `email`
- [ ] `direccion_fiscal` (solo si se va a mostrar públicamente)
- [ ] `horario` (si se quiere mostrar un horario de atención)

Al cambiar estos valores en un único archivo, se actualizan automáticamente
el footer, el botón flotante de WhatsApp, el formulario de contacto y los
datos estructurados (JSON-LD) de todas las páginas.

## 2. Páginas legales

- `aviso-legal/index.html` y `privacidad/index.html`: falta la
  **denominación social o nombre comercial exacto, NIF/CIF y domicilio
  fiscal** de Voltorum. Están marcados con `[DENOMINACIÓN SOCIAL...]`,
  `[NIF O CIF]`, `[DIRECCIÓN FISCAL]`.
- `cookies/index.html`: falta detallar qué cookies se usan realmente
  (analítica, publicidad, etc.) una vez se decida si se instala algo más
  que cookies técnicas.
- Las tres páginas legales tienen `[FECHA]` al final — sustituir por la
  fecha real de publicación.
- Revisar con un profesional si el texto legal genérico incluido cubre
  las necesidades reales de Voltorum (esto es un borrador funcional, no
  asesoría legal).

## 3. Imágenes y contenido visual

- El hero y las secciones no usan fotografías reales (no se disponía de
  ninguna con derechos claros de uso), sino una ilustración SVG propia
  con motivo de cuadro eléctrico/circuito. Si se quieren fotos reales de
  instalaciones, cuadros, técnicos trabajando, etc., colocarlas en
  `img/electricidad/` (carpeta ya creada y vacía) y sustituir el bloque
  `.plate` de `index.html`.
- La sección "Trabajos realizados" de la home (`#proyectos`) está
  preparada con tres tarjetas vacías ("Próximamente"). Sustituir por
  casos reales con fotografías cuando estén disponibles.
- `sobre-voltorum/index.html` no incluye biografía, años de experiencia
  ni foto del equipo — deliberadamente, para no inventar nada. Completar
  con información real si se quiere una página "sobre nosotros" más
  personal.

## 4. Formulario de contacto

- El formulario de `/contacto/` no está conectado a ningún backend: al
  enviarlo, abre WhatsApp con el mensaje ya redactado. Esto evita perder
  contactos, pero conviene sustituirlo por un envío real (por email, a un
  CRM, a Formspree/similar, o a un backend propio) antes de depender de
  la web para captar clientes en serio.

## 5. Analítica y cookies

- No se ha incluido ningún script de analítica (tipo Plausible, que sí
  tenía TratoClaro) para no asumir qué herramienta se quiere usar. Si se
  añade una, actualizar también `cookies/index.html` en consecuencia.

## 6. Dominio

- El sitio está preparado en metadatos para `voltorum.com` (canonical,
  Open Graph, `sitemap.xml`), pero no se ha creado ningún archivo `CNAME`
  a propósito, para no conectar el dominio de forma irreversible. Ver el
  punto 2 de `README.md` cuando el dominio esté decidido y listo.

## 7. Activos de marca no recibidos

El briefing original mencionaba estos archivos, pero solo se recibieron
los dos PNG (isotipo y logotipo completo) adjuntos al mensaje:

- `Voltorum_Logo_Corporativo.svg`
- `Voltorum_Logo_Negativo.svg`
- `Voltorum_Isotipo.svg`
- `Voltorum_Avatar_Negro.png`

Se ha trabajado a partir de los dos PNG recibidos, generando desde ahí
las versiones en blanco/negro, favicons y el icono de Open Graph. Si más
adelante existen los SVG vectoriales originales, sustituir los PNG en
`img/` por esas versiones dará más nitidez a cualquier tamaño.
