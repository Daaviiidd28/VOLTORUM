# Voltorum — web

Electricidad y mantenimiento en Madrid. Web estática (HTML + CSS + JS, sin
build ni framework), adaptada del sistema visual de TratoClaro a un tema
oscuro con azul eléctrico, para la nueva marca **Voltorum**.

## 1. Antes de publicar — datos pendientes

Este proyecto se entrega con **placeholders** allí donde no había datos
reales confirmados (teléfono, WhatsApp, email, dirección fiscal, dominio
conectado, imágenes de trabajos reales). Lee **`PENDIENTES.md`** y
complétalo antes de publicar la web. El único archivo que hay que tocar
para el contacto es:

```
js/config.js
```

Ahí están centralizados: teléfono, WhatsApp, email, dominio y zona.
Cambiar esos valores actualiza automáticamente todas las páginas (footer,
botón flotante de WhatsApp, formulario de contacto, JSON-LD del negocio).

## 2. Probar la web en local

No hace falta instalar nada. Desde la carpeta del proyecto:

```bash
python3 -m http.server 8000
```

y abre `http://localhost:8000/` en el navegador. También puedes abrir
`index.html` directamente con doble clic, aunque algunos navegadores
restringen `fetch`/módulos al abrir por `file://`, así que se recomienda
usar el servidor local de arriba.

## 3. Publicar la web

**Importante ahora que hay backend de pagos**: GitHub Pages solo sirve
HTML/CSS/JS estático, no puede ejecutar las funciones serverless que
necesita Stripe. Para que `/admin/` y `/pagar/` funcionen, la web tiene
que publicarse en un hosting que sí ejecute funciones — se recomienda
**Netlify** (gratis para este uso, y es justo el que usan los archivos
`netlify.toml` y `netlify/functions/` ya incluidos). El resto del sitio
(las páginas informativas) seguiría funcionando igual en GitHub Pages,
pero entonces los pagos no funcionarían — así que lo más simple es
publicar todo junto en Netlify.

**Pasos para publicar en Netlify:**

1. Sube este proyecto a un repositorio de GitHub (puede ser el mismo que
   ya tienes).
2. Entra en [netlify.com](https://netlify.com) → **Add new site → Import
   an existing project** → conecta tu cuenta de GitHub → elige el
   repositorio.
3. Netlify detectará `netlify.toml` automáticamente (build vacío,
   `publish = "."`, funciones en `netlify/functions`). No hace falta
   tocar nada en ese paso.
4. Antes del primer deploy útil, añade las variables de entorno en
   **Site configuration → Environment variables** (ver `PENDIENTES.md`,
   punto 0).
5. Cuando el dominio `voltorum.com` esté listo, conéctalo desde
   **Domain management** dentro de Netlify — Netlify gestiona el HTTPS
   automáticamente.

Si en algún momento se prefiere quitar los pagos y volver a una web
puramente informativa, sí se puede publicar en GitHub Pages sin más
(simplemente las páginas `/admin/` y `/pagar/` no funcionarían).

**Pasos generales si NO se necesitan pagos** (GitHub Pages, Vercel
estático, hosting compartido, etc.):

1. Sube el contenido completo de esta carpeta (`voltorum-web/`) a la raíz
   del hosting elegido.
2. Configura el dominio `voltorum.com` cuando esté listo. **No se ha
   incluido ningún archivo `CNAME`** a propósito, para no dejar el dominio
   conectado de forma irreversible antes de que esté decidido. Si usas
   GitHub Pages, crea un archivo `CNAME` en la raíz con el contenido
   `voltorum.com` cuando quieras activarlo.
3. Verifica que `sitemap.xml` y `robots.txt` apuntan al dominio correcto
   (ya están preparados para `https://voltorum.com`).
4. Revisa `js/config.js` una última vez para confirmar que no queda
   ningún placeholder entre corchetes (`[TELÉFONO]`, `[EMAIL]`, etc.).

## 3.5. Backend de pagos (Stripe)

Se ha añadido un backend mínimo con **funciones serverless de Netlify**
para cobrar presupuestos. No hay servidor propio que mantener: Netlify
las ejecuta bajo demanda.

**Cómo funciona el flujo completo:**

1. Se acuerda un presupuesto con el cliente (por WhatsApp, email, etc.).
2. Voltorum entra en `https://TUDOMINIO/admin/`, mete la contraseña de
   administrador, el importe y el concepto, y pulsa "Generar enlace".
   Esto llama a la función `generar-enlace`, que firma el importe con
   `PAYMENT_LINK_SECRET` para que no se pueda manipular.
3. Se copia el enlace generado (algo como
   `https://voltorum.com/pagar/?amount=18000&concepto=...&sig=...`) y se
   envía al cliente por WhatsApp o email.
4. El cliente abre el enlace, ve el importe y el concepto, y pulsa
   "Pagar ahora". Esto llama a la función `create-checkout-session`, que
   comprueba la firma y crea una sesión de **Stripe Checkout** — la
   página de pago oficial de Stripe, donde el cliente introduce su
   tarjeta. Voltorum nunca ve ni almacena los datos de la tarjeta.
5. Tras pagar, Stripe redirige a `/pagar/gracias/`. Si cancela, vuelve a
   `/pagar/cancelado/`.
6. (Opcional) El webhook `stripe-webhook` recibe la confirmación real del
   pago directamente desde Stripe y la registra en los logs de Netlify —
   más fiable que fiarse solo de la página de "gracias", que en teoría
   cualquiera podría visitar sin haber pagado.

**Antes de poder usarlo hay que configurar las variables de entorno en
Netlify** (`STRIPE_SECRET_KEY`, `PAYMENT_LINK_SECRET`, `ADMIN_PASSWORD`,
`SITE_URL`, y opcionalmente `STRIPE_WEBHOOK_SECRET`). Ver el punto 0 de
`PENDIENTES.md` para el paso a paso.

`/admin/` y `/pagar/` no están enlazadas desde el menú del sitio ni
aparecen en `sitemap.xml`, y llevan `noindex` para que Google no las
indexe.

## 4. Estructura del proyecto

```
voltorum-web/
├── index.html
├── servicios/
│   ├── index.html
│   ├── averias-electricas/index.html
│   ├── cuadros-electricos/index.html
│   ├── mantenimiento-electrico/index.html
│   └── boletines-documentacion/index.html
├── comunidades/index.html
├── negocios/index.html
├── sobre-voltorum/index.html
├── contacto/index.html
├── aviso-legal/index.html
├── privacidad/index.html
├── cookies/index.html
├── css/voltorum.css
├── js/config.js        ← datos editables (teléfono, email, WhatsApp, dominio)
├── js/site.js           ← navegación, animaciones, FAQ, formulario
├── img/                  ← logos, favicons, og.jpg, ilustraciones
├── robots.txt
├── sitemap.xml
└── site.webmanifest
```

El código fuente que genera estas páginas (por si hay que volver a
regenerarlas tras cambiar textos) está en `_build/` — no forma parte del
sitio publicado, es solo la herramienta interna usada para construirlo.
Para regenerar la web tras editar el contenido de `_build/*.py`:

```bash
cd _build && python3 build.py
```

## 5. Formulario de contacto

El formulario de `/contacto/` **no está conectado a ningún backend
todavía**. Al enviarlo, se abre WhatsApp con el mensaje ya redactado a
partir de los campos rellenados, para no perder ningún contacto mientras
se decide un procesador de formularios real (Formspree, un pequeño
backend propio, integración con email, etc.). Ver `PENDIENTES.md`.

## 6. Tecnología

- HTML + CSS + JavaScript vanilla, sin build ni dependencias de paquetes.
- Fuentes: Geist, IBM Plex Mono, Instrument Serif (Google Fonts, vía CDN).
- Animaciones: GSAP + ScrollTrigger (vía CDN, con respeto a
  `prefers-reduced-motion`).
- Sin frameworks, sin Node, sin paso de compilación.

## 7. Rutas creadas

Ver la lista completa en `CAMBIOS.md`.
