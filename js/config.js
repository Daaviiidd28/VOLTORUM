/* ════════════════════════════════════════════════════════════════
   VOLTORUM · CONFIGURACIÓN CENTRAL
   Edita SOLO este archivo para cambiar teléfono, email, WhatsApp,
   dominio o dirección en toda la web. Todas las páginas leen estos
   valores automáticamente a través de site.js.

   Los valores entre corchetes [ ] son placeholders: sustitúyelos
   por los datos reales de Voltorum antes de publicar. Mientras no
   se cambien, la web funciona pero muestra el texto entre corchetes
   tal cual, para que sea imposible publicarlos por error sin verlos.
   ════════════════════════════════════════════════════════════════ */
window.VOLTORUM_CONFIG = {
  nombre: "Voltorum",
  descriptor: "Electricidad y mantenimiento",
  dominio: "voltorum.com",

  telefono_visible: "[TELÉFONO]",       // ej. "910 000 000"
  telefono_href: "[TELEFONO_SIN_ESPACIOS]", // ej. "tel:+34910000000"

  whatsapp_numero: "[WHATSAPP_NUMERO]", // formato internacional sin '+', ej. "34600000000"
  whatsapp_texto_defecto: "Hola Voltorum, quiero pedir información.",

  email: "[EMAIL]",                      // ej. "info@voltorum.com"

  zona: "Madrid y alrededores",
  direccion_fiscal: "[DIRECCIÓN FISCAL]", // solo si aplica, para aviso legal

  horario: "[HORARIO DE ATENCIÓN]"
};
