# -*- coding: utf-8 -*-
from icons import icon

def body():
    return f'''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../">Inicio</a> <span class="mg-sep">/</span> <span>Servicios</span></div></nav>

<main>
<section>
  <div class="wrap art">
    <h1 class="rv">Servicios eléctricos en Madrid</h1>
    <p class="meta rv">Averías, cuadros, mantenimiento y documentación</p>
    <p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Cada instalación es distinta, pero el criterio es siempre el mismo: diagnóstico antes de presupuestar, presupuesto por escrito antes de trabajar, y todo documentado al terminar.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="trio rv">
      <a class="blk" href="./averias-electricas/">
        {icon('rayo')}
        <h3>Averías y reparaciones eléctricas</h3>
        <p>Cortes de luz, disparos del diferencial, enchufes o puntos de luz que dejan de funcionar.</p>
      </a>
      <a class="blk" href="./cuadros-electricos/">
        {icon('cuadro')}
        <h3>Cuadros eléctricos y protecciones</h3>
        <p>Revisión, ampliación o sustitución de cuadros, magnetotérmicos y diferenciales.</p>
      </a>
      <a class="blk" href="./mantenimiento-electrico/">
        {icon('llave')}
        <h3>Mantenimiento eléctrico preventivo</h3>
        <p>Revisiones periódicas para detectar antes lo que luego sale caro.</p>
      </a>
      <a class="blk" href="./boletines-documentacion/">
        {icon('documento')}
        <h3>Revisión, diagnóstico y documentación</h3>
        <p>Estado real de la instalación y gestión de la documentación que corresponda.</p>
      </a>
      <a class="blk" href="../comunidades/">
        {icon('edificio')}
        <h3>Electricidad para comunidades</h3>
        <p>Zonas comunes, portales, garajes y cuartos de instalaciones.</p>
      </a>
      <a class="blk" href="../negocios/">
        {icon('tienda')}
        <h3>Electricidad para negocios y locales</h3>
        <p>Instalaciones adaptadas al uso comercial, con los tiempos de parada al mínimo.</p>
      </a>
    </div>
  </div>
</section>

<section class="cta-mid">
  <div class="wrap">
    <h2 class="d2 rv">¿No sabes cuál necesitas?</h2>
    <p class="rv">Cuéntanos qué está pasando y te decimos qué servicio encaja.</p>
    <div class="cta-btns rv">
      <a href="../contacto/" class="btn btn-g">Solicitar presupuesto</a>
      <a data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, no sé qué servicio necesito, ¿me ayudáis?" href="#" class="btn btn-o">Escribir por WhatsApp</a>
    </div>
  </div>
</section>
</main>
'''
