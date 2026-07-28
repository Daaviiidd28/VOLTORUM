// netlify/functions/stripe-webhook.js
//
// Webhook de Stripe: confirma que un pago se ha completado de verdad
// (no basta con la página de "gracias", que cualquiera podría visitar
// sin haber pagado). De momento solo registra el evento en los logs de
// Netlify. Ver PENDIENTES.md para añadir un aviso por email cuando
// entre un pago, si se quiere.

const Stripe = require('stripe');
const stripe = Stripe(process.env.STRIPE_SECRET_KEY);

exports.handler = async function (event) {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method not allowed' };
  }

  const sig = event.headers['stripe-signature'];
  let stripeEvent;

  try {
    stripeEvent = stripe.webhooks.constructEvent(
      event.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    console.error('Firma de webhook inválida:', err.message);
    return { statusCode: 400, body: `Webhook Error: ${err.message}` };
  }

  if (stripeEvent.type === 'checkout.session.completed') {
    const session = stripeEvent.data.object;
    console.log('Pago completado:', {
      id: session.id,
      importe: session.amount_total,
      moneda: session.currency,
      email: session.customer_details && session.customer_details.email,
    });
    // PENDIENTE: aquí se podría enviar un email o notificación de WhatsApp
    // avisando de que ha entrado un pago (ver PENDIENTES.md).
  }

  return { statusCode: 200, body: JSON.stringify({ received: true }) };
};
