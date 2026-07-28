# -*- coding: utf-8 -*-
"""Arte SVG abstracto para la lámina del hero (sin fotografías)."""

def hero_plate_svg():
    return '''<svg class="plate-art" viewBox="0 0 1600 700" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Esquema abstracto de un cuadro eléctrico">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#101218"/>
      <stop offset="100%" stop-color="#06070A"/>
    </linearGradient>
    <radialGradient id="glow" cx="78%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#3D7CFF" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#3D7CFF" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1600" height="700" fill="url(#bgGrad)"/>
  <rect width="1600" height="700" fill="url(#glow)"/>
  <g stroke="#3D7CFF" stroke-opacity="0.35" stroke-width="1">
    <path d="M120 560 H420 V420 H620 V520 H900" fill="none"/>
    <path d="M120 460 H320 V300 H520" fill="none"/>
    <path d="M1180 180 V360 H980 V460 H760" fill="none"/>
    <path d="M1420 140 V300 H1220 V220 H1040" fill="none"/>
    <path d="M1480 500 H1220 V400 H1060" fill="none"/>
  </g>
  <g fill="#3D7CFF">
    <circle cx="120" cy="560" r="4.5"/>
    <circle cx="420" cy="560" r="4.5"/>
    <circle cx="620" cy="420" r="4.5"/>
    <circle cx="900" cy="520" r="5.5"/>
    <circle cx="520" cy="300" r="4.5"/>
    <circle cx="1180" cy="180" r="4.5"/>
    <circle cx="760" cy="460" r="5.5"/>
    <circle cx="1420" cy="140" r="4.5"/>
    <circle cx="1040" cy="220" r="4.5"/>
    <circle cx="1480" cy="500" r="4.5"/>
    <circle cx="1060" cy="400" r="5.5"/>
  </g>
  <g stroke="#E9EBF0" stroke-opacity="0.06">
    <line x1="0" y1="140" x2="1600" y2="140"/>
    <line x1="0" y1="280" x2="1600" y2="280"/>
    <line x1="0" y1="420" x2="1600" y2="420"/>
    <line x1="0" y1="560" x2="1600" y2="560"/>
    <line x1="200" y1="0" x2="200" y2="700"/>
    <line x1="500" y1="0" x2="500" y2="700"/>
    <line x1="800" y1="0" x2="800" y2="700"/>
    <line x1="1100" y1="0" x2="1100" y2="700"/>
    <line x1="1400" y1="0" x2="1400" y2="700"/>
  </g>
  <g transform="translate(1120,190) scale(1.55)" fill="#E9EBF0" fill-opacity="0.9">
    <path d="M52.6 0 24.2 26 6.1 43 0.8 78.3l31.8-30.9c15.6-15.2 15.6-31.4 15.6-43.6L52.6 0Z" fill-opacity="0.14"/>
    <path d="M52.6 22 24.2 48 6.1 65 0.8 100.3l31.8-30.9c15.6-15.2 15.6-31.4 15.6-43.6L52.6 22Z" fill-opacity="0.10"/>
    <path d="M20 100 c-10-6-13-16-13-24 0-9 4-15 13-22 l16-14 v20 c0 13-4 24-16 32l-8 6Z" fill-opacity="0.16"/>
  </g>
</svg>'''

def mini_glow_divider():
    return '''<div class="mq" aria-hidden="true"><div class="mq-t" id="mqt"><span>Cuadros eléctricos</span> <i>&middot;</i> <span>Averías</span> <i>&middot;</i> <span>Mantenimiento preventivo</span> <i>&middot;</i> <span>Comunidades</span> <i>&middot;</i> <span>Negocios y locales</span> <i>&middot;</i> <span>Documentación</span> <i>&middot;</i> <span>Cuadros eléctricos</span> <i>&middot;</i> <span>Averías</span> <i>&middot;</i> <span>Mantenimiento preventivo</span> <i>&middot;</i> <span>Comunidades</span> <i>&middot;</i> <span>Negocios y locales</span> <i>&middot;</i> <span>Documentación</span></div></div>'''
