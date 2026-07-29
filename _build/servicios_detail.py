# -*- coding: utf-8 -*-
from icons import icon

def _template(titulo, eyebrow, intro, puntos, cuando, extra_html, relacionados):
    puntos_html = "\n".join(f'<li><b>{t}</b> — {d}</li>' for t, d in puntos)
    cuando_html = "\n".join(f'<li>{c}</li>' for c in cuando)
    rel_html = "\n".join(f'<a href="{href}">{label}</a>' for label, href in relacionados)
    return f'''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../../">Inicio</a> <span class="mg-sep">/</span> <a href="../">Servicios</a> <span class="mg-sep">/</span> <span>{titulo}</span></div></nav>

<main>
<section>
  <div class="wrap art">
    <h1 class="rv">{titulo}</h1>
    <p class="meta rv">{eyebrow}</p>
    {intro}

    <h2 class="rv">Qué incluye</h2>
    <ul class="rv">
      {puntos_html}
    </ul>

    <h2 class="rv">Cuándo tiene sentido llamar</h2>
    <ul class="rv">
      {cuando_html}
    </ul>

    {extra_html}

    <div class="aviso rv">
      <p>El presupuesto se entrega por escrito después de revisar la instalación en persona. No se presupuesta a ciegas ni por teléfono para trabajos que lo requieran.</p>
    </div>

    <section class="rel">
      <h2>Servicios relacionados</h2>
      <div class="rel-links">
        {rel_html}
      </div>
    </section>
  </div>
</section>

<section class="cta-mid">
  <div class="wrap">
    <h2 class="d2 rv">¿Empezamos?</h2>
    <p class="rv">Cuéntanos qué está pasando y coordinamos una visita.</p>
    <div class="cta-btns rv">
      <a href="../../contacto/" class="btn btn-g">Solicitar presupuesto</a>
      <a data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero información sobre {titulo.lower()}." href="#" class="btn btn-o">Escribir por WhatsApp</a>
    </div>
  </div>
</section>
</main>
'''

def averias():
    return _template(
        titulo="Averías y reparaciones eléctricas",
        eyebrow="Diagnóstico y reparación",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Un corte que se repite, un diferencial que salta sin motivo aparente o un punto de luz que deja de funcionar. Antes de cambiar nada se localiza el origen del fallo: muchas averías «pequeñas» son síntoma de un problema en otro punto de la instalación.</p>',
        puntos=[
            ("Localización del fallo", "con herramientas de medición, no a base de prueba y error"),
            ("Reparación o sustitución", "del elemento afectado — cableado, mecanismo, protección"),
            ("Explicación del origen", "qué ha fallado y por qué, no solo el arreglo"),
            ("Aviso de riesgos asociados", "si la avería apunta a un problema mayor en la instalación"),
        ],
        cuando=[
            "El diferencial salta de forma repetida sin causa evidente.",
            "Hay enchufes, interruptores o puntos de luz que han dejado de funcionar.",
            "Se detectan chispazos, olor a quemado o calentamiento en mecanismos.",
            "Una zona de la vivienda o el local se queda sin corriente de forma parcial.",
        ],
        extra_html="",
        relacionados=[
            ("Cuadros eléctricos", "../cuadros-electricos/"),
            ("Mantenimiento preventivo", "../mantenimiento-electrico/"),
            ("Comunidades", "../../comunidades/"),
        ],
    )

def cuadros():
    return _template(
        titulo="Cuadros eléctricos y protecciones",
        eyebrow="Revisión, ampliación y sustitución",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">El cuadro eléctrico es el punto donde se decide si una instalación protege de verdad a quien la usa. Muchos cuadros antiguos se quedaron cortos de potencia o de protecciones cuando la vivienda o el local cambiaron de uso.</p>',
        puntos=[
            ("Revisión del cuadro actual", "estado de magnetotérmicos, diferenciales y conexiones"),
            ("Ampliación de circuitos", "cuando se añaden usos que el cuadro original no contemplaba"),
            ("Sustitución completa", "de cuadros obsoletos o que ya no cumplen su función de protección"),
            ("Etiquetado y orden", "de los circuitos, para que se entienda de un vistazo"),
        ],
        cuando=[
            "El cuadro es antiguo y no se sabe con certeza qué protege cada interruptor.",
            "Se ha ampliado la vivienda o el local y faltan circuitos o potencia.",
            "Las protecciones actuales no coinciden con la carga real de la instalación.",
            "Va a pasar una inspección o revisión y el cuadro es un punto de duda.",
        ],
        extra_html="",
        relacionados=[
            ("Averías eléctricas", "../averias-electricas/"),
            ("Revisión y documentación", "../boletines-documentacion/"),
            ("Negocios y locales", "../../negocios/"),
        ],
    )

def mantenimiento():
    return _template(
        titulo="Mantenimiento eléctrico preventivo",
        eyebrow="Revisiones periódicas",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">La mayoría de averías serias se anuncian antes: una conexión que se calienta, un cable que ha perdido aislamiento, una protección que ya no responde como debería. El mantenimiento preventivo consiste en encontrar eso antes de que se convierta en un problema.</p>',
        puntos=[
            ("Revisión periódica programada", "con la frecuencia que tenga sentido según el uso del inmueble"),
            ("Comprobación de conexiones y protecciones", "puntos habituales de fallo por desgaste o mal uso"),
            ("Informe de estado", "con lo revisado y, si procede, lo recomendado a corto y medio plazo"),
            ("Prioridad ante avería", "para quien ya tiene un mantenimiento contratado"),
        ],
        cuando=[
            "Comunidades de propietarios con zonas comunes de uso constante.",
            "Negocios y locales donde una avería eléctrica implica cerrar.",
            "Instalaciones con cierta antigüedad sin revisión reciente.",
            "Después de una reforma, para verificar que todo quedó correctamente ejecutado.",
        ],
        extra_html="",
        relacionados=[
            ("Cuadros eléctricos", "../cuadros-electricos/"),
            ("Comunidades", "../../comunidades/"),
            ("Negocios", "../../negocios/"),
        ],
    )

def boletines():
    extra = '''<div class="warn-box rv">
      <p><b>Sobre boletines y certificados:</b> no todas las instalaciones necesitan un boletín nuevo. Una instalación puede requerir revisión, adaptación o nueva documentación dependiendo de su estado, antigüedad, modificaciones realizadas o un requerimiento administrativo concreto. Ningún certificado se promete sin inspeccionar antes la instalación en persona.</p>
    </div>'''
    return _template(
        titulo="Revisión, diagnóstico y documentación eléctrica",
        eyebrow="Boletines y trámites, cuando corresponda",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Antes de hablar de papeles, se revisa la instalación. A partir de ahí se explica con claridad si hace falta actuar, qué tipo de documentación corresponde y por qué — sin plazos inventados ni tarifas cerradas antes de ver el caso.</p>',
        puntos=[
            ("Diagnóstico del estado real", "de la instalación, con evidencia de lo encontrado"),
            ("Explicación de qué documentación aplica", "según el estado, uso y antigüedad de la instalación"),
            ("Coordinación de la tramitación", "cuando legalmente corresponda emitir boletín u otro documento"),
            ("Informe entendible", "sin tecnicismos innecesarios, útil también para administradores de fincas"),
        ],
        cuando=[
            "Se va a vender o alquilar un inmueble y piden documentación eléctrica.",
            "La instalación ha sido modificada y no está claro si necesita nuevo boletín.",
            "Un seguro o una administración ha solicitado documentación específica.",
            "Simplemente no se sabe en qué estado de regularización está la instalación.",
        ],
        extra_html=extra,
        relacionados=[
            ("Cuadros eléctricos", "../cuadros-electricos/"),
            ("Mantenimiento preventivo", "../mantenimiento-electrico/"),
            ("Comunidades", "../../comunidades/"),
        ],
    )

def instalaciones():
    return _template(
        titulo="Instalaciones eléctricas",
        eyebrow="Instalación nueva o reforma completa",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Una reforma, una obra nueva o una instalación que ha quedado corta con el tiempo. Se estudia el uso real del espacio antes de tirar un solo metro de cable, para no repetir en unos años lo que se hace ahora.</p>',
        puntos=[
            ("Proyecto de la instalación", "adaptado al uso real de la vivienda, negocio o comunidad"),
            ("Ejecución completa", "desde el cuadro hasta el último punto de luz o enchufe"),
            ("Materiales homologados", "pensados para durar, no para salir del paso"),
            ("Entrega documentada", "con lo instalado explicado, útil de cara a futuras revisiones"),
        ],
        cuando=[
            "Obra nueva o reforma integral de vivienda, local o negocio.",
            "La instalación actual se ha quedado corta de circuitos o potencia.",
            "Se cambia el uso del espacio y la instalación no se ajusta al nuevo uso.",
            "Se quiere modernizar una instalación antigua de forma completa, no solo parchearla.",
        ],
        extra_html="",
        relacionados=[
            ("Cuadros eléctricos", "../cuadros-electricos/"),
            ("Iluminación LED", "../iluminacion-led/"),
            ("Negocios y locales", "../../negocios/"),
        ],
    )

def iluminacion_led():
    return _template(
        titulo="Iluminación LED",
        eyebrow="Menos consumo, misma luz",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Cambiar a iluminación LED suele ser de las intervenciones que más se nota en la factura con menos obra por medio. Se valora punto por punto qué sustituir y con qué temperatura de luz, en vez de cambiar todo por cambiar.</p>',
        puntos=[
            ("Sustitución de luminarias", "por equivalentes LED, sin perder nivel de luz"),
            ("Nuevos puntos LED", "cuando el proyecto lo pide, integrados con el resto de la instalación"),
            ("Elección de temperatura de color", "según el uso de cada estancia o zona"),
            ("Cálculo de ahorro estimado", "orientativo, antes de decidir el alcance del cambio"),
        ],
        cuando=[
            "La factura de la luz sube y la iluminación es antigua (halógenos, fluorescentes).",
            "Un negocio quiere mejorar la iluminación de cara al cliente sin disparar el consumo.",
            "Una comunidad quiere reducir el gasto de zonas comunes con luz permanente.",
            "Se reforma un espacio y toca decidir el tipo de iluminación desde cero.",
        ],
        extra_html="",
        relacionados=[
            ("Puntos de luz", "../puntos-de-luz/"),
            ("Instalaciones eléctricas", "../instalaciones-electricas/"),
            ("Mantenimiento preventivo", "../mantenimiento-electrico/"),
        ],
    )

def enchufes():
    return _template(
        titulo="Enchufes e interruptores",
        eyebrow="Cambio, ampliación y reparación",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Un enchufe suelto, un interruptor que ya no hace buen contacto, o simplemente faltan tomas donde hacen falta de verdad. Trabajo puntual, pero con el mismo criterio que cualquier otro: revisar antes de cambiar.</p>',
        puntos=[
            ("Sustitución de mecanismos", "enchufes, interruptores y conmutadores dañados o anticuados"),
            ("Ampliación de tomas", "donde el uso real del espacio lo pide"),
            ("Revisión de conexiones", "un mecanismo flojo puede ser síntoma de algo más, se comprueba"),
            ("Acabado a juego", "con el resto de mecanismos de la estancia"),
        ],
        cuando=[
            "Un enchufe o interruptor no hace buen contacto o se calienta.",
            "Faltan tomas de corriente donde realmente se necesitan.",
            "Se renueva la decoración y se aprovecha para cambiar los mecanismos.",
            "Los mecanismos actuales son antiguos y no cumplen la normativa vigente.",
        ],
        extra_html="",
        relacionados=[
            ("Puntos de luz", "../puntos-de-luz/"),
            ("Averías eléctricas", "../averias-electricas/"),
            ("Instalaciones eléctricas", "../instalaciones-electricas/"),
        ],
    )

def puntos_de_luz():
    return _template(
        titulo="Puntos de luz",
        eyebrow="Nuevos puntos o reubicación",
        intro='<p class="rv" style="color:var(--ink-2);max-width:64ch;font-size:1.02rem;line-height:1.72">Un punto de luz mal colocado se nota cada día. Ya sea añadir uno nuevo o mover el que hay, el trabajo se hace con acabado limpio, sin dejar el techo o la pared peor de como estaban.</p>',
        puntos=[
            ("Nuevos puntos de luz", "donde el espacio lo necesite, con el circuito adecuado"),
            ("Reubicación de puntos existentes", "cuando la distribución actual no funciona"),
            ("Instalación de mecanismos de control", "interruptores simples, conmutados o regulables"),
            ("Acabado cuidado", "en pared o techo, sin dejar marcas visibles del trabajo"),
        ],
        cuando=[
            "Falta luz en una zona concreta de la vivienda, negocio o local.",
            "Un punto de luz está mal colocado y molesta al uso diario del espacio.",
            "Se reforma una estancia y toca replantear dónde va cada punto de luz.",
            "Se añade una zona nueva (trastero, buhardilla, terraza cubierta) sin puntos de luz.",
        ],
        extra_html="",
        relacionados=[
            ("Iluminación LED", "../iluminacion-led/"),
            ("Enchufes e interruptores", "../enchufes-e-interruptores/"),
            ("Instalaciones eléctricas", "../instalaciones-electricas/"),
        ],
    )
