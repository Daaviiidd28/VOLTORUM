# -*- coding: utf-8 -*-
from icons import icon

def body():
    return f'''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../">Inicio</a> <span class="mg-sep">/</span> <span>Sobre Voltorum</span></div></nav>

<main>
<section>
  <div class="wrap art">
    <h1 class="rv">Sobre Voltorum</h1>
    <p class="meta rv">Electricidad y mantenimiento en Madrid</p>
    <p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Voltorum nace con una idea sencilla: que contratar electricidad no dependa de la confianza a ciegas. Cada trabajo se explica antes de empezar, se presupuesta por escrito y se documenta al terminar, tanto si es una avería de una tarde como el mantenimiento continuo de un edificio.</p>

    <h2 class="rv">Cómo se trabaja</h2>
    <ul class="rv">
      <li><b>Diagnóstico antes que presupuesto.</b> No se dan cifras sin haber visto la instalación.</li>
      <li><b>Presupuesto por escrito.</b> Sin sorpresas al terminar el trabajo.</li>
      <li><b>Documentación del trabajo realizado.</b> Útil para comunidades, negocios y particulares por igual.</li>
      <li><b>Trato directo.</b> Un mismo interlocutor de principio a fin.</li>
    </ul>

    <h2 class="rv">A quién atiende Voltorum</h2>
    <ul class="rv">
      <li>Comunidades de propietarios y administradores de fincas.</li>
      <li>Negocios, locales comerciales y oficinas.</li>
      <li>Particulares en Madrid y alrededores.</li>
    </ul>

    <div class="aviso rv">
      <p>Esta página está pensada para ampliarse con la trayectoria, formación y datos de contacto profesional reales del equipo de Voltorum. Ver <code>PENDIENTES.md</code> para completar esta sección con contenido verificado — no se ha rellenado con años de experiencia, certificaciones ni datos que no se hayan confirmado.</p>
    </div>
  </div>
</section>

<section class="cta-mid">
  <div class="wrap">
    <h2 class="d2 rv">¿Hablamos de tu instalación?</h2>
    <p class="rv">Cuéntanos qué necesitas y te decimos qué tiene sentido hacer.</p>
    <div class="cta-btns rv">
      <a href="../contacto/" class="btn btn-g">Solicitar presupuesto</a>
      <a data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero pedir información." href="#" class="btn btn-o">Escribir por WhatsApp</a>
    </div>
  </div>
</section>
</main>
'''
