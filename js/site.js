document.addEventListener('DOMContentLoaded', function () {
  const CFG = window.VOLTORUM_CONFIG || {};
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ══ INYECCIÓN DE CONFIGURACIÓN ══════════════════════════════
     Cualquier elemento con data-cfg="campo" recibe ese texto.
     Cualquier <a> con data-cfg-href="tel|whatsapp|email" recibe
     el enlace correspondiente construido a partir de config.js. */
  document.querySelectorAll('[data-cfg]').forEach(el => {
    const key = el.getAttribute('data-cfg');
    if (CFG[key] !== undefined) el.textContent = CFG[key];
  });
  document.querySelectorAll('[data-cfg-href]').forEach(el => {
    const kind = el.getAttribute('data-cfg-href');
    if (kind === 'tel') {
      el.href = 'tel:' + (CFG.telefono_href || '');
    } else if (kind === 'email') {
      el.href = 'mailto:' + (CFG.email || '');
    } else if (kind === 'whatsapp') {
      const msg = el.getAttribute('data-wa-msg') || CFG.whatsapp_texto_defecto || '';
      el.href = 'https://wa.me/' + (CFG.whatsapp_numero || '') + '?text=' + encodeURIComponent(msg);
      el.target = '_blank';
      el.rel = 'noopener';
    }
  });

  /* ══ NAV: fondo al hacer scroll + menú móvil ═════════════════ */
  const nav = document.getElementById('nav');
  const onScroll = () => { if (nav) nav.classList.toggle('on', window.scrollY > 8); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const burger = document.getElementById('burger');
  const navr = document.getElementById('navr');
  if (burger && navr) {
    burger.addEventListener('click', () => {
      const open = navr.classList.toggle('open');
      burger.classList.toggle('x', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    navr.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      navr.classList.remove('open');
      burger.classList.remove('x');
      burger.setAttribute('aria-expanded', 'false');
    }));
  }

  /* ══ FAQ acordeón ═════════════════════════════════════════ */
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      item.closest('.faq')?.querySelectorAll('.faq-item.open').forEach(o => { if (o !== item) o.classList.remove('open'); });
      item.classList.toggle('open', !isOpen);
    });
  });

  /* ══ FORMULARIO DE CONTACTO ═══════════════════════════════
     No hay backend conectado todavía (ver PENDIENTES.md).
     De momento el formulario abre WhatsApp con los datos
     rellenados, para no perder ningún lead mientras se conecta
     un procesador de formularios real. */
  const form = document.getElementById('contactoForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const d = Object.fromEntries(new FormData(form).entries());
      const partes = [
        'Hola Voltorum, os escribo desde la web.',
        d.nombre ? 'Nombre: ' + d.nombre : '',
        d.telefono ? 'Teléfono: ' + d.telefono : '',
        d.email ? 'Email: ' + d.email : '',
        d.tipo_cliente ? 'Tipo de cliente: ' + d.tipo_cliente : '',
        d.zona ? 'Municipio/zona: ' + d.zona : '',
        d.servicio ? 'Servicio: ' + d.servicio : '',
        d.urgencia ? 'Urgencia: ' + d.urgencia : '',
        d.descripcion ? 'Descripción: ' + d.descripcion : ''
      ].filter(Boolean).join('\n');
      const wa = 'https://wa.me/' + (CFG.whatsapp_numero || '') + '?text=' + encodeURIComponent(partes);
      const estado = document.getElementById('formEstado');
      if (estado) {
        estado.hidden = false;
        estado.textContent = 'Gracias. Te hemos preparado el mensaje — ábrelo en WhatsApp para enviarlo, o escríbenos directamente a ' + (CFG.email || '[EMAIL]') + '.';
      }
      window.open(wa, '_blank', 'noopener');
    });
  }

  /* ══ MOVIMIENTO ═══════════════════════════════════════════ */
  if (!reduced && window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);

    if (document.querySelector('.hero h1 .ln b')) {
      gsap.from('.hero h1 .ln b', { yPercent: 112, duration: 1.3, ease: 'expo.out', stagger: .085, delay: .2 });
    }
    const intro = ['.hero .eyebrow', '.hero-sub', '.hero-cta', '.specs div'].filter(s => document.querySelector(s));
    if (intro.length) gsap.from(intro, { y: 22, opacity: 0, duration: .95, ease: 'power3.out', stagger: .07, delay: .7 });

    if (document.getElementById('plate')) {
      gsap.to('#plate svg, #plate .plate-art', { scale: 1.08, yPercent: 3, ease: 'none',
        scrollTrigger: { trigger: '#plate', start: 'top bottom', end: 'bottom top', scrub: true } });
    }

    gsap.utils.toArray('.rv').forEach(el => {
      gsap.from(el, { y: 34, opacity: 0, duration: 1, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 88%' } });
    });

    if (document.getElementById('fill') && document.querySelector('.rail')) {
      gsap.to('#fill', { height: '100%', ease: 'none',
        scrollTrigger: { trigger: '.rail', start: 'top 62%', end: 'bottom 72%', scrub: .5 } });
    }
    gsap.utils.toArray('.step').forEach(s => {
      gsap.from(s, { x: -22, opacity: 0, duration: .9, ease: 'power3.out',
        scrollTrigger: { trigger: s, start: 'top 86%' } });
      ScrollTrigger.create({ trigger: s, start: 'top 68%', end: 'bottom 42%',
        onToggle: self => s.classList.toggle('hit', self.isActive) });
    });

    gsap.utils.toArray('.trio .blk, .cat .cc, .guias .gc').forEach((c, i) => {
      gsap.from(c, { y: 28, opacity: 0, duration: .8, ease: 'power3.out', delay: (i % 6) * .06,
        scrollTrigger: { trigger: c, start: 'top 90%' } });
    });
  } else {
    document.querySelectorAll('.step').forEach(s => s.classList.add('hit'));
    const f = document.getElementById('fill'); if (f) f.style.height = '100%';
  }
});
