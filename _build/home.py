# -*- coding: utf-8 -*-
from icons import icon
from hero_art import hero_plate_svg, mini_glow_divider

def body():
    return f'''<!-- ══ HERO ══ -->
<header class="hero">
  <div class="hero-in" id="heroIn">
    <p class="eyebrow">Madrid &middot; Electricistas profesionales</p>
    <h1>
      <span class="ln"><b>Electricistas en Madrid.</b></span>
      <span class="ln"><b>Instalaciones, averías y mantenimiento.</b></span>
    </h1>
    <p class="hero-sub">Ofrecemos instalaciones eléctricas, averías urgentes, cuadros eléctricos, iluminación LED, enchufes, puntos de luz y mantenimiento para viviendas, empresas y comunidades de propietarios. Presupuesto gratuito y atención rápida.</p>
    <div class="hero-cta">
      <a class="btn btn-g" href="./contacto/">Solicitar presupuesto <span class="arw">&#8599;</span></a>
      <a class="btn btn-o" data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero pedir un presupuesto." href="#">Pedir presupuesto por WhatsApp</a>
    </div>

    <div class="plate" id="plate">
      {hero_plate_svg()}
    </div>

    <div class="specs">
      <div><b class="lit">Madrid</b><span>Y toda la Comunidad de Madrid</span></div>
      <div><b>Escrito</b><span>Presupuesto siempre por escrito</span></div>
      <div><b>0 &euro;</b><span>Diagnóstico incluido en el presupuesto</span></div>
      <div><b>1 a 1</b><span>Trato directo, sin intermediarios</span></div>
    </div>
  </div>
</header>

<!-- ══ BARRA DE CONFIANZA ══ -->
<section class="trust rv" aria-label="Por qué confiar en Voltorum">
  <div class="wrap trust-in">
    <div><span class="trust-check">&#10003;</span>Presupuesto gratuito</div>
    <div><span class="trust-check">&#10003;</span>Atención rápida</div>
    <div><span class="trust-check">&#10003;</span>Electricistas cualificados</div>
    <div><span class="trust-check">&#10003;</span>Servicio en toda la Comunidad de Madrid</div>
  </div>
</section>

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
        <h3>Averías eléctricas</h3>
        <p>Cortes, disparos del diferencial, enchufes o puntos de luz que dejan de funcionar. Diagnóstico y reparación urgente.</p>
      </a>
      <a class="blk" href="./servicios/instalaciones-electricas/">
        {icon('llave')}
        <h3>Instalaciones eléctricas</h3>
        <p>Instalaciones nuevas o reformas completas, adaptadas a vivienda, negocio o comunidad.</p>
      </a>
      <a class="blk" href="./servicios/cuadros-electricos/">
        {icon('cuadro')}
        <h3>Cuadros eléctricos</h3>
        <p>Revisión, ampliación o sustitución de cuadros, magnetotérmicos y diferenciales.</p>
      </a>
      <a class="blk" href="./servicios/iluminacion-led/">
        {icon('bombilla')}
        <h3>Iluminación LED</h3>
        <p>Sustitución e instalación de iluminación LED para ahorrar en consumo sin perder luz.</p>
      </a>
      <a class="blk" href="./servicios/enchufes-e-interruptores/">
        {icon('enchufe')}
        <h3>Enchufes e interruptores</h3>
        <p>Cambio, ampliación o reparación de enchufes e interruptores en cualquier estancia.</p>
      </a>
      <a class="blk" href="./servicios/puntos-de-luz/">
        {icon('rayo')}
        <h3>Puntos de luz</h3>
        <p>Nuevos puntos de luz o reubicación de los existentes, con acabado limpio.</p>
      </a>
      <a class="blk" href="./servicios/mantenimiento-electrico/">
        {icon('reloj')}
        <h3>Mantenimiento preventivo</h3>
        <p>Revisiones periódicas para detectar antes lo que luego sale caro.</p>
      </a>
      <a class="blk" href="./comunidades/">
        {icon('edificio')}
        <h3>Comunidades de propietarios</h3>
        <p>Zonas comunes, portales, garajes y cuartos de instalaciones, coordinado con administradores de fincas.</p>
      </a>
      <a class="blk" href="./negocios/">
        {icon('tienda')}
        <h3>Negocios y locales comerciales</h3>
        <p>Instalaciones adaptadas al uso comercial, con los tiempos de parada al mínimo posible.</p>
      </a>
    </div>
  </div>
</section>

<!-- ══ 02 · POR QUÉ ELEGIRNOS ══ -->
<section id="ventajas" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>02</i>Por qué elegirnos</p>
      <h2>Lo que no<br><em>se negocia.</em></h2>
    </div>
    <div class="adv-grid rv">
      <div class="adv">
        {icon('reloj')}
        <h3>Atención rápida</h3>
        <p>Respuesta ágil ante averías y urgencias, sin dejarte esperando.</p>
      </div>
      <div class="adv">
        {icon('recibo')}
        <h3>Presupuestos transparentes</h3>
        <p>Por escrito y desglosados, antes de empezar cualquier trabajo.</p>
      </div>
      <div class="adv">
        {icon('check')}
        <h3>Materiales de calidad</h3>
        <p>Componentes homologados, pensados para durar, no para salir del paso.</p>
      </div>
      <div class="adv">
        {icon('llave')}
        <h3>Soluciones adaptadas</h3>
        <p>Cada instalación es distinta: la solución se ajusta a tu caso, no al revés.</p>
      </div>
      <div class="adv">
        {icon('escudo')}
        <h3>Trabajo limpio</h3>
        <p>Se deja el espacio como estaba, o mejor, al terminar la intervención.</p>
      </div>
      <div class="adv">
        {icon('candado')}
        <h3>Garantía en nuestros trabajos</h3>
        <p>Respaldo sobre lo realizado, con seguimiento si surge cualquier duda.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ 03 · PROCESO ══ -->
<section id="proceso">
  <div class="wrap">
    <div class="proc">
      <div class="proc-l rv">
        <p class="eyebrow"><i>03</i>Cómo se trabaja</p>
        <h2 style="font-size:clamp(1.8rem,4.2vw,3.2rem);font-weight:600;letter-spacing:-.05em;line-height:1.02;margin-top:18px">Cinco pasos,<br><em class="it">sin rodeos.</em></h2>
      </div>
      <div class="rail">
        <div class="track"></div><div class="fill" id="fill"></div>
        <div class="step">
          <span class="dot"></span><b class="no">01</b>
          <h3>Contactas con nosotros</h3>
          <p>Por teléfono, WhatsApp o el formulario de contacto. Con una descripción breve y, si puede ser, alguna foto, ya se puede orientar el trabajo.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">02</b>
          <h3>Analizamos tu necesidad</h3>
          <p>Diagnóstico en el lugar antes de dar cualquier cifra cerrada. No se presupuesta a ciegas.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">03</b>
          <h3>Recibes presupuesto gratuito</h3>
          <p>Por escrito, con el trabajo desglosado, antes de tocar nada.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">04</b>
          <h3>Realizamos el trabajo</h3>
          <p>Con materiales de calidad y el espacio recogido al terminar.</p>
        </div>
        <div class="step">
          <span class="dot"></span><b class="no">05</b>
          <h3>Seguimiento y soporte</h3>
          <p>Disponibilidad para resolver dudas después de la intervención, no solo durante.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══ 06 · OPINIONES ══ -->
<section id="opiniones" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>04</i>Opiniones</p>
      <h2>Lo que dicen<br><em>nuestros clientes.</em></h2>
      <div class="sh-side">
        <p class="lede">Este espacio está preparado para mostrar las reseñas reales de Google de Voltorum en cuanto estén disponibles.</p>
      </div>
    </div>
    <div class="reviews rv" aria-live="polite">
      <div class="review-card ph">
        <div class="review-stars" aria-hidden="true">{icon('estrella')}{icon('estrella')}{icon('estrella')}{icon('estrella')}{icon('estrella')}</div>
        <p class="review-txt">Aquí aparecerá una reseña real de Google cuando esté disponible.</p>
        <p class="review-who">&mdash;</p>
      </div>
      <div class="review-card ph">
        <div class="review-stars" aria-hidden="true">{icon('estrella')}{icon('estrella')}{icon('estrella')}{icon('estrella')}{icon('estrella')}</div>
        <p class="review-txt">Aquí aparecerá una reseña real de Google cuando esté disponible.</p>
        <p class="review-who">&mdash;</p>
      </div>
      <div class="review-card ph">
        <div class="review-stars" aria-hidden="true">{icon('estrella')}{icon('estrella')}{icon('estrella')}{icon('estrella')}{icon('estrella')}</div>
        <p class="review-txt">Aquí aparecerá una reseña real de Google cuando esté disponible.</p>
        <p class="review-who">&mdash;</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ 05 · FAQ ══ -->
<section id="faq">
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>05</i>Preguntas frecuentes</p>
      <h2>Dudas<br><em>habituales.</em></h2>
    </div>
    <div class="faq rv">
      <div class="faq-item">
        <button class="faq-q">¿Trabajáis para particulares o solo para comunidades y negocios? <span class="px">+</span></button>
        <div class="faq-a"><p>Los tres perfiles. Comunidades de propietarios, negocios y locales, y particulares en Madrid y toda la Comunidad de Madrid.</p></div>
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
        <div class="faq-a"><p>Madrid capital y toda la Comunidad de Madrid. Escríbenos con tu zona y lo confirmamos.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- ══ 09 · CONTACTO ══ -->
<section class="cta" id="contacto">
  <div class="wrap">
    <p class="eyebrow rv"><i>06</i>Contacto</p>
    <h2 class="rv">¿Hablamos de<br><em class="it">tu instalación?</em></h2>
    <p class="sub rv">Cuéntanos qué necesitas y te decimos, con la instalación delante, qué tiene sentido hacer.</p>

    <div class="contact-block rv">
      <a class="contact-phone" data-cfg-href="tel" href="#">
        {icon('telefono')}
        <span data-cfg="telefono_visible">611 066 820</span>
      </a>
      <div class="hero-cta" style="margin-top:0">
        <a class="btn btn-g" data-cfg-href="tel" href="#">Llamar ahora</a>
        <a class="btn btn-o" data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero pedir información." href="#">Escribir por WhatsApp</a>
        <a class="btn btn-o" href="./contacto/">Rellenar formulario</a>
      </div>
    </div>
  </div>
</section>
'''
