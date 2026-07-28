# -*- coding: utf-8 -*-
from icons import icon
from hero_art import hero_plate_svg, mini_glow_divider

def body():
    return f'''<!-- ══ HERO ══ -->
<header class="hero">
  <div class="hero-in" id="heroIn">
    <p class="eyebrow">Madrid &middot; Electricidad y mantenimiento</p>
    <h1>
      <span class="ln"><b>Electricidad y mantenimiento</b></span>
      <span class="ln"><b>sin complicaciones.</b></span>
    </h1>
    <p class="hero-sub">Soluciones eléctricas para comunidades, negocios y particulares en Madrid. Presupuesto claro, trabajo documentado y seguimiento real.</p>
    <div class="hero-cta">
      <a class="btn btn-g" href="./contacto/">Solicitar presupuesto <span class="arw">&#8599;</span></a>
      <a class="btn btn-o" href="./servicios/averias-electricas/">Contar una avería</a>
      <a class="btn btn-o" data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero hablar sobre un trabajo eléctrico." href="#">Hablar por WhatsApp</a>
    </div>

    <div class="plate" id="plate">
      {hero_plate_svg()}
    </div>

    <div class="specs">
      <div><b class="lit">Madrid</b><span>Y municipios cercanos</span></div>
      <div><b>Escrito</b><span>Presupuesto siempre por escrito</span></div>
      <div><b>0 &euro;</b><span>Diagnóstico incluido en el presupuesto</span></div>
      <div><b>1 a 1</b><span>Trato directo, sin intermediarios</span></div>
    </div>
  </div>
</header>

{mini_glow_divider()}

<!-- ══ 01 · SERVICIOS ══ -->
<section id="servicios">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>01</i>Servicios</p>
      <h2>Todo lo eléctrico,<br><em>bajo un mismo criterio.</em></h2>
      <div class="sh-side">
        <p class="lede">Desde una avería puntual hasta el mantenimiento continuo de un edificio. Cada trabajo se explica antes de empezar y se documenta al terminar.</p>
        <p style="margin-top:26px"><a href="./servicios/" style="border-bottom:1px solid var(--line-2);padding-bottom:7px;font-size:.92rem;display:inline-flex;gap:34px;align-items:center">Ver todos los servicios <span class="arw">&#8599;</span></a></p>
      </div>
    </div>

    <div class="trio rv">
      <a class="blk" href="./servicios/averias-electricas/">
        {icon('rayo')}
        <h3>Averías y reparaciones</h3>
        <p>Cortes, disparos del diferencial, enchufes o puntos de luz que dejan de funcionar. Diagnóstico y reparación con el problema explicado, no solo solucionado.</p>
      </a>
      <a class="blk" href="./servicios/cuadros-electricos/">
        {icon('cuadro')}
        <h3>Cuadros eléctricos y protecciones</h3>
        <p>Revisión, ampliación o sustitución de cuadros, magnetotérmicos y diferenciales que ya no cumplen con la instalación actual.</p>
      </a>
      <a class="blk" href="./servicios/mantenimiento-electrico/">
        {icon('llave')}
        <h3>Mantenimiento preventivo</h3>
        <p>Revisiones periódicas para detectar antes lo que luego sale caro: conexiones flojas, sobrecargas o material desgastado.</p>
      </a>
      <a class="blk" href="./servicios/boletines-documentacion/">
        {icon('documento')}
        <h3>Revisión y documentación</h3>
        <p>Diagnóstico del estado real de una instalación y gestión de la documentación que corresponda tras la inspección.</p>
      </a>
      <a class="blk" href="./comunidades/">
        {icon('edificio')}
        <h3>Comunidades de propietarios</h3>
        <p>Zonas comunes, portales, garajes y cuartos de instalaciones, coordinado con administradores de fincas.</p>
      </a>
      <a class="blk" href="./negocios/">
        {icon('tienda')}
        <h3>Negocios y locales</h3>
        <p>Instalaciones adaptadas al uso comercial, con los tiempos de parada al mínimo posible.</p>
      </a>
    </div>
  </div>
</section>

<!-- ══ 02 · COMUNIDADES ══ -->
<section id="comunidades" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>02</i>Comunidades de propietarios</p>
      <h2>Un solo contacto<br><em>para todo el edificio.</em></h2>
      <div class="sh-side">
        <p class="lede">Administradores de fincas y presidentes de comunidad necesitan respuestas rápidas y presupuestos que se puedan llevar a junta sin sorpresas. Ese es el trato.</p>
        <div class="chips">
          <span>Zonas comunes</span>
          <span>Portales y garajes</span>
          <span>Cuartos de contadores</span>
          <span>Urgencias coordinadas</span>
        </div>
        <p style="margin-top:22px"><a href="./comunidades/" style="border-bottom:1px solid var(--line-2);padding-bottom:7px;font-size:.92rem;display:inline-flex;gap:34px;align-items:center">Electricidad para comunidades <span class="arw">&#8599;</span></a></p>
      </div>
    </div>
  </div>
</section>

<!-- ══ 03 · NEGOCIOS ══ -->
<section id="negocios">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>03</i>Negocios y locales</p>
      <h2>Menos tiempo parado,<br><em>más tiempo abierto.</em></h2>
      <div class="sh-side">
        <p class="lede">Comercios, oficinas y locales de hostelería trabajan con horarios que no dan margen. Los trabajos se planifican para interferir lo mínimo posible en la actividad.</p>
        <div class="chips">
          <span>Locales comerciales</span>
          <span>Oficinas</span>
          <span>Hostelería</span>
          <span>Reformas de local</span>
        </div>
        <p style="margin-top:22px"><a href="./negocios/" style="border-bottom:1px solid var(--line-2);padding-bottom:7px;font-size:.92rem;display:inline-flex;gap:34px;align-items:center">Electricidad para negocios <span class="arw">&#8599;</span></a></p>
      </div>
    </div>
  </div>
</section>

<!-- ══ 04 · PROCESO ══ -->
<section id="proceso" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="proc">
      <div class="proc-l rv">
        <p class="eyebrow"><i>04</i>Cómo se trabaja</p>
        <h2 style="font-size:clamp(1.8rem,4.2vw,3.2rem);font-weight:600;letter-spacing:-.05em;line-height:1.02;margin-top:18px">Cuatro pasos,<br><em class="it">sin rodeos.</em></h2>
      </div>
      <div class="rail">
        <div class="track"></div><div class="fill" id="fill"></div>
        <div class="step">
          <span class="dot"></span><b class="no">01</b>
          <h3>Cuéntanos el problema</h3>
          <p>Por teléfono, WhatsApp o el formulario de contacto. Con una descripción breve y, si puede ser, alguna foto, ya se puede orientar el trabajo.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">02</b>
          <h3>Revisamos la instalación</h3>
          <p>Diagnóstico en el lugar antes de dar cualquier cifra cerrada. No se presupuesta a ciegas.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">03</b>
          <h3>Recibes un presupuesto claro</h3>
          <p>Por escrito, con el trabajo desglosado, antes de tocar nada.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">04</b>
          <h3>Ejecutamos y documentamos</h3>
          <p>El trabajo se entrega explicado: qué se ha hecho, con qué material y qué queda pendiente, si algo queda pendiente.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══ 05 · VENTAJAS ══ -->
<section id="ventajas">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>05</i>Por qué Voltorum</p>
      <h2>Lo que no<br><em>se negocia.</em></h2>
    </div>
    <div class="adv-grid rv">
      <div class="adv">
        {icon('recibo')}
        <h3>Presupuestos claros</h3>
        <p>Por escrito y desglosados, antes de empezar cualquier trabajo.</p>
      </div>
      <div class="adv">
        {icon('chat')}
        <h3>Atención personalizada</h3>
        <p>Se habla con la misma persona de principio a fin, sin pasar por varios departamentos.</p>
      </div>
      <div class="adv">
        {icon('camara')}
        <h3>Trabajo documentado</h3>
        <p>Registro de lo realizado, útil para actas de comunidad o control interno del negocio.</p>
      </div>
      <div class="adv">
        {icon('reloj')}
        <h3>Seguimiento posterior</h3>
        <p>Disponibilidad para resolver dudas después de la intervención, no solo durante.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ 06 · PROYECTOS ══ -->
<section id="proyectos" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>06</i>Trabajos realizados</p>
      <h2>Casos reales,<br><em>en construcción.</em></h2>
      <div class="sh-side">
        <p class="lede">Esta sección está preparada para mostrar trabajos concretos con fotografías reales una vez estén disponibles. Ver <a href="#" style="text-decoration:underline">PENDIENTES.md</a> para completar esta parte.</p>
      </div>
    </div>
    <div class="guias rv">
      <div class="gc" style="opacity:.5">
        <h3>Próximamente</h3>
        <p>Espacio reservado para un caso real de comunidad de propietarios.</p>
      </div>
      <div class="gc" style="opacity:.5">
        <h3>Próximamente</h3>
        <p>Espacio reservado para un caso real de negocio o local.</p>
      </div>
      <div class="gc" style="opacity:.5">
        <h3>Próximamente</h3>
        <p>Espacio reservado para un caso real de particular.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ 07 · FAQ ══ -->
<section id="faq">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>07</i>Preguntas frecuentes</p>
      <h2>Dudas<br><em>habituales.</em></h2>
    </div>
    <div class="faq rv">
      <div class="faq-item">
        <button class="faq-q">¿Trabajáis para particulares o solo para comunidades y negocios? <span class="px">+</span></button>
        <div class="faq-a"><p>Los tres perfiles. Comunidades de propietarios, negocios y locales, y particulares en Madrid y alrededores.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿El presupuesto tiene algún coste? <span class="px">+</span></button>
        <div class="faq-a"><p>No. El diagnóstico y el presupuesto están incluidos y se entregan por escrito antes de empezar cualquier trabajo.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Todas las instalaciones necesitan un boletín nuevo? <span class="px">+</span></button>
        <div class="faq-a"><p>No necesariamente. Una instalación puede necesitar revisión, adaptación o nueva documentación según su estado, antigüedad, modificaciones realizadas o un requerimiento administrativo concreto. No se afirma que todos los boletines caduquen: cada caso se valora tras inspeccionar la instalación.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Podéis emitir un certificado sin ver la instalación? <span class="px">+</span></button>
        <div class="faq-a"><p>No. Ningún certificado o boletín se promete sin haber inspeccionado antes la instalación en persona.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿Cómo se coordina el trabajo con un administrador de fincas? <span class="px">+</span></button>
        <div class="faq-a"><p>Directamente con el administrador o con quien la comunidad designe: se comparte el diagnóstico, el presupuesto y, si se pide, un informe para la junta de propietarios.</p></div>
      </div>
      <div class="faq-item">
        <button class="faq-q">¿En qué zona trabajáis? <span class="px">+</span></button>
        <div class="faq-a"><p>Madrid capital y municipios cercanos. Escríbenos con tu zona y lo confirmamos.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- ══ 08 · CTA FINAL ══ -->
<section class="cta">
  <div class="wrap">
    <p class="eyebrow rv"><i>08</i>Empezar</p>
    <h2 class="rv">¿Hablamos de<br><em class="it">tu instalación?</em></h2>
    <p class="sub rv">Cuéntanos qué necesitas y te decimos, con la instalación delante, qué tiene sentido hacer.</p>
    <div class="hero-cta rv">
      <a class="btn btn-g" href="./contacto/">Solicitar presupuesto <span class="arw">&#8599;</span></a>
      <a class="btn btn-o" data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero pedir información." href="#">Hablar por WhatsApp</a>
    </div>
  </div>
</section>
'''
