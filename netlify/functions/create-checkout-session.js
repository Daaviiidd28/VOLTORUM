// netlify/functions/create-checkout-session.js
//
// Crea una sesión de Stripe Checkout para cobrar un presupuesto concreto.
// Recibe el importe y el concepto FIRMADOS (ver generar-enlace.js) para que
// nadie pueda cambiar el importe manipulando la URL: si la firma no
// coincide, se rechaza la petición.

const Stripe = require('stripe');
const crypto = require('crypto');

const stripe = Stripe(process.env.STRIPE_SECRET_KEY);
const SITE_URL = process.env.SITE_URL || 'https://voltorum.com';

function firmaValida(amount, concepto, sig) {
  const secret = process.env.PAYMENT_LINK_SECRET;
  if (!secret) return false;
  const esperado = crypto
    .createHmac('sha256', secret)
    .update(`${amount}.${concepto}`)
    .digest('hex')
    .slice(0, 32);
  try {
    return crypto.timingSafeEqual(Buffer.from(esperado), Buffer.from(sig || ''));
  } catch {
    return false;
  }
}

exports.handler = async function (event) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method not allowed' };
  }

  let data;
  try {
    data = JSON.parse(event.body || '{}');
  } catch {
    return { statusCode: 400, body: JSON.stringify({ error: 'JSON inválido' }) };
  }

  const amount = parseInt(data.amount, 10); // céntimos de euro
  const concepto = (data.concepto || 'Servicio Voltorum').toString().slice(0, 120);
  const email = data.email ? String(data.email).slice(0, 200) : undefined;
  const sig = data.sig;

  if (!amount || amount < 50) { // Stripe exige un mínimo (~0,50 €)
    return { statusCode: 400, body: JSON.stringify({ error: 'Importe no válido' }) };
  }

  if (!firmaValida(amount, concepto, sig)) {
    return { statusCode: 403, body: JSON.stringify({ error: 'Enlace de pago no válido o caducado' }) };
  }

  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      payment_method_types: ['card'],
      customer_email: email,
      line_items: [
        {
          price_data: {
            currency: 'eur',
            product_data: { name: concepto },
            unit_amount: amount,
          },
          quantity: 1,
        },
      ],
      success_url: `${SITE_URL}/pagar/gracias/?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${SITE_URL}/pagar/cancelado/`,
    });

    return {
      statusCode: 200,
      body: JSON.stringify({ url: session.url }),
    };
  } catch (err) {
    console.error('Error creando sesión de Stripe:', err.message);
    return { statusCode: 500, body: JSON.stringify({ error: 'No se pudo iniciar el pago' }) };
  }
};
