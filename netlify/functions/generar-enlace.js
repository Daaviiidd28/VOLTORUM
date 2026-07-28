// netlify/functions/generar-enlace.js
//
// Genera un enlace de pago firmado para enviar a un cliente. Protegido por
// una contraseña de administrador (ADMIN_PASSWORD) para que solo Voltorum
// pueda crear enlaces de cobro. La usa la página /admin/.

const crypto = require('crypto');

const SITE_URL = process.env.SITE_URL || 'https://voltorum.com';

function firmar(amount, concepto) {
  const secret = process.env.PAYMENT_LINK_SECRET;
  return crypto
    .createHmac('sha256', secret)
    .update(`${amount}.${concepto}`)
    .digest('hex')
    .slice(0, 32);
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

  if (!process.env.ADMIN_PASSWORD || data.password !== process.env.ADMIN_PASSWORD) {
    return { statusCode: 401, body: JSON.stringify({ error: 'Contraseña incorrecta' }) };
  }

  const importeEuros = parseFloat(data.importe);
  const concepto = (data.concepto || 'Servicio Voltorum').toString().slice(0, 120);
  const email = data.email ? String(data.email).slice(0, 200) : '';

  if (!importeEuros || importeEuros <= 0) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Importe no válido' }) };
  }

  const amount = Math.round(importeEuros * 100); // a céntimos
  const sig = firmar(amount, concepto);

  const params = new URLSearchParams({ amount: String(amount), concepto, sig });
  if (email) params.set('email', email);

  const enlace = `${SITE_URL}/pagar/?${params.toString()}`;

  return { statusCode: 200, body: JSON.stringify({ enlace }) };
};
