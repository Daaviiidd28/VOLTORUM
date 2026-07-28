# -*- coding: utf-8 -*-

def body():
    return '''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../">Inicio</a> <span class="mg-sep">/</span> <span>Contacto</span></div></nav>

<main>
<section>
  <div class="wrap">
    <div class="sh rv">
      <p class="eyebrow"><i>&#9679;</i>Contacto</p>
      <h2>Cuéntanos<br><em class="it">qué necesitas.</em></h2>
      <div class="sh-side">
        <p class="lede">Rellena el formulario con el mayor detalle posible o escribe directamente. Se responde revisando cada caso, no con respuestas automáticas.</p>
        <ul class="pts" style="margin-top:22px">
          <li><b>Teléfono</b><br><a data-cfg-href="tel" data-cfg="telefono_visible" href="#">[TELÉFONO]</a></li>
          <li><b>WhatsApp</b><br><a data-cfg-href="whatsapp" data-wa-msg="Hola Voltorum, quiero pedir información." href="#">Escribir por WhatsApp</a></li>
          <li><b>Email</b><br><a data-cfg-href="email" data-cfg="email" href="#">[EMAIL]</a></li>
          <li><b>Zona</b><br>Madrid y alrededores</li>
        </ul>
      </div>
    </div>

    <form class="formu rv" id="contactoForm">
      <div class="f"><span>Nombre</span><input type="text" name="nombre" autocomplete="name" required></div>
      <div class="f"><span>Teléfono</span><input type="tel" name="telefono" autocomplete="tel" required></div>
      <div class="f"><span>Correo electrónico</span><input type="email" name="email" autocomplete="email"></div>
      <div class="f">
        <span>Tipo de cliente</span>
        <select name="tipo_cliente">
          <option value="Particular">Particular</option>
          <option value="Comunidad de propietarios">Comunidad de propietarios</option>
          <option value="Administrador de fincas">Administrador de fincas</option>
          <option value="Negocio o local">Negocio o local</option>
        </select>
      </div>
      <div class="f"><span>Municipio o zona</span><input type="text" name="zona" placeholder="p. ej. Madrid — San Blas-Canillejas"></div>
      <div class="f">
        <span>Servicio solicitado</span>
        <select name="servicio">
          <option value="Avería o reparación">Avería o reparación</option>
          <option value="Cuadro eléctrico">Cuadro eléctrico</option>
          <option value="Mantenimiento preventivo">Mantenimiento preventivo</option>
          <option value="Boletín / documentación">Boletín / documentación</option>
          <option value="Otro / no lo sé aún">Otro / no lo sé aún</option>
        </select>
      </div>
      <div class="f">
        <span>Nivel de urgencia</span>
        <select name="urgencia">
          <option value="Urgente (hoy o mañana)">Urgente (hoy o mañana)</option>
          <option value="Esta semana">Esta semana</option>
          <option value="Sin prisa, quiero presupuesto">Sin prisa, quiero presupuesto</option>
        </select>
      </div>
      <div class="f w">
        <span>Descripción del trabajo</span>
        <textarea name="descripcion" placeholder="Cuéntanos qué está pasando o qué necesitas, con el mayor detalle posible."></textarea>
      </div>
      <label class="chk">
        <input type="checkbox" required>
        <span>He leído y acepto la <a href="../privacidad/" style="text-decoration:underline">política de privacidad</a>.</span>
      </label>
      <div class="f w">
        <button type="submit" class="btn btn-g">Enviar solicitud <span class="arw">&#8599;</span></button>
      </div>
    </form>
    <p class="form-estado" id="formEstado" hidden></p>
    <p class="note rv" style="margin-top:18px">Este formulario todavía no está conectado a un procesador de envíos: al enviarlo se abre WhatsApp con el mensaje ya redactado. Ver <code>PENDIENTES.md</code> para conectar un backend de formularios real.</p>
  </div>
</section>
</main>
'''
