# -*- coding: utf-8 -*-

def pagar():
    return '''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../">Inicio</a> <span class="mg-sep">/</span> <span>Pagar</span></div></nav>

<main>
<section>
  <div class="wrap" style="max-width:560px">
    <div class="sh rv" style="grid-template-columns:1fr">
      <p class="eyebrow"><i>&#9679;</i>Pago seguro</p>
      <h2>Completar<br><em class="it">el pago.</em></h2>
    </div>

    <div id="pagoBox" class="calc rv" style="text-align:left">
      <p class="calc-k">Concepto</p>
      <p id="pConcepto" style="font-size:1.2rem;font-weight:500;margin-bottom:18px">&mdash;</p>
      <p class="calc-k">Importe</p>
      <p id="pImporte" style="font-family:var(--mono);font-weight:500;font-size:2.2rem;letter-spacing:-.05em;margin-bottom:22px">&mdash;</p>
      <button class="btn btn-g" id="pBtn" style="width:100%">Pagar ahora <span class="arw">&#8599;</span></button>
      <p id="pError" class="note" style="color:#ff8080;display:none;margin-top:16px"></p>
      <p class="note" style="margin-top:18px">Pago procesado de forma segura por Stripe. Voltorum no almacena los datos de tu tarjeta.</p>
    </div>
  </div>
</section>
</main>

<script>
(function () {
  const params = new URLSearchParams(window.location.search);
  const amount = params.get('amount');
  const concepto = params.get('concepto') || 'Servicio Voltorum';
  const email = params.get('email') || '';
  const sig = params.get('sig');

  const pConcepto = document.getElementById('pConcepto');
  const pImporte = document.getElementById('pImporte');
  const pBtn = document.getElementById('pBtn');
  const pError = document.getElementById('pError');

  pConcepto.textContent = concepto;
  if (amount) {
    pImporte.textContent = (parseInt(amount, 10) / 100).toLocaleString('es-ES', { style: 'currency', currency: 'EUR' });
  }

  if (!amount || !sig) {
    pBtn.disabled = true;
    pError.style.display = 'block';
    pError.textContent = 'Este enlace de pago no es válido. Pide a Voltorum que te envíe uno nuevo.';
    return;
  }

  pBtn.addEventListener('click', async function () {
    pBtn.disabled = true;
    pBtn.textContent = 'Redirigiendo a pago seguro…';
    pError.style.display = 'none';
    try {
      const res = await fetch('/.netlify/functions/create-checkout-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount, concepto, email, sig }),
      });
      const data = await res.json();
      if (!res.ok || !data.url) throw new Error(data.error || 'No se pudo iniciar el pago');
      window.location.href = data.url;
    } catch (e) {
      pBtn.disabled = false;
      pBtn.textContent = 'Pagar ahora';
      pError.style.display = 'block';
      pError.textContent = 'No se ha podido iniciar el pago. Inténtalo de nuevo o contacta con Voltorum.';
    }
  });
})();
</script>
'''

def gracias():
    return '''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../../">Inicio</a> <span class="mg-sep">/</span> <span>Pago completado</span></div></nav>

<main>
<section>
  <div class="wrap art" style="text-align:center;max-width:560px">
    <h1 class="rv">Pago recibido</h1>
    <p class="rv" style="color:var(--ink-2);font-size:1.05rem;line-height:1.7">Gracias. Hemos recibido tu pago correctamente. Te confirmaremos por email o WhatsApp los siguientes pasos.</p>
    <p class="rv" style="margin-top:30px"><a href="../../" class="btn btn-o">Volver al inicio</a></p>
  </div>
</section>
</main>
'''

def cancelado():
    return '''<nav class="migas" aria-label="Ruta"><div class="wrap"><a href="../../">Inicio</a> <span class="mg-sep">/</span> <span>Pago cancelado</span></div></nav>

<main>
<section>
  <div class="wrap art" style="text-align:center;max-width:560px">
    <h1 class="rv">Pago cancelado</h1>
    <p class="rv" style="color:var(--ink-2);font-size:1.05rem;line-height:1.7">No se ha completado el pago. Si ha sido un error, puedes volver a intentarlo con el mismo enlace, o contactar con Voltorum si necesitas ayuda.</p>
    <p class="rv" style="margin-top:30px"><a href="../../contacto/" class="btn btn-o">Contactar con Voltorum</a></p>
  </div>
</section>
</main>
'''
