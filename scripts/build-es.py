#!/usr/bin/env python3
"""Build the Spanish page (es/index.html) from the English source (index.html).

Each entry is (English fragment, Spanish fragment, expected count). The build stops if a
fragment is missing or appears a different number of times, so an edit to the English
page can never ship half-translated. Run after any change to index.html:

    python3 scripts/build-es.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

T = [
    # ---------- head ----------
    ('<html lang="en">', '<html lang="es">', 1),
    ('<meta name="description" content="Óscar Saboya, product manager in Zaragoza, Spain. Six years writing code, six years leading product. I use AI where it makes sense, and judgment everywhere.">',
     '<meta name="description" content="Óscar Saboya, product manager en Zaragoza. Seis años programando y seis en producto. Uso la IA donde aporta; el criterio, siempre.">', 1),
    ('<link rel="canonical" href="https://oscarsaboya.com/">', '<link rel="canonical" href="https://oscarsaboya.com/es/">', 1),
    ('<meta property="og:url" content="https://oscarsaboya.com/">', '<meta property="og:url" content="https://oscarsaboya.com/es/">\n<meta property="og:locale" content="es_ES">', 1),
    ('content="From writing code to deciding what\'s worth building."', 'content="De escribir código a decidir qué vale la pena construir."', 2),
    ('https://oscarsaboya.com/og-image.jpg', 'https://oscarsaboya.com/og-image-es.jpg', 2),

    # ---------- nav ----------
    ('aria-label="Óscar Saboya, back to top"', 'aria-label="Óscar Saboya, volver arriba"', 1),
    ('<nav class="pill" aria-label="Main"><a href="#journey">journey</a><a href="#side">side project</a><a href="#help">how I help</a><a href="#about">about</a></nav>',
     '<nav class="pill" aria-label="Principal"><a href="#journey">trayectoria</a><a href="#side">proyecto personal</a><a href="#help">cómo ayudo</a><a href="#about">sobre mí</a></nav>', 1),
    ('<nav class="lang" aria-label="Language"><a href="/" hreflang="en" lang="en" aria-current="true">EN</a><a href="/es/" hreflang="es" lang="es">ES</a></nav>',
     '<nav class="lang" aria-label="Idioma"><a href="/" hreflang="en" lang="en">EN</a><a href="/es/" hreflang="es" lang="es" aria-current="true">ES</a></nav>', 1),
    ('<a class="talk" href="#contact">Get in touch</a>', '<a class="talk" href="#contact">Hablemos</a>', 1),

    # ---------- hero ----------
    ('<span>Product manager at <b>Citibox</b></span>', '<span>Product manager en <b>Citibox</b></span>', 1),
    ("Building got cheap. Knowing what's worth building didn't. That's the part I'm good at.",
     'Hoy construir cuesta poco. Lo difícil es saber qué merece la pena. A eso me dedico.', 1),
    ('</i>See the journey</a>', '</i>Ver mi trayectoria</a>', 1),
    ("<h1 class=\"display\">From writing code to deciding what's worth building.</h1>",
     '<h1 class="display">De escribir código a decidir qué vale la pena construir.</h1>', 2),

    # ---------- at a glance ----------
    ('aria-label="At a glance"', 'aria-label="De un vistazo"', 1),
    ('<p class="mono">At a glance</p>', '<p class="mono">De un vistazo</p>', 1),
    ('<p class="brief"><b>Computer engineer</b> by training: <b>six years of code</b>, then <b>six of product</b>. At my best taking things from <b>zero to one</b>, <b>growing</b> them and <b>changing how teams work</b>. Product teams of <b>more than ten people</b> led so far, with <b>AI in the loop every day</b> to research, prototype and ship. Based in <b>Zaragoza, Spain</b>, happy working <b>remote</b>.</p>',
     '<p class="brief"><b>Ingeniero informático</b>. Pasé <b>seis años programando</b> y llevo <b>seis en producto</b>. Lo mío es <b>arrancar productos desde cero</b>, <b>hacerlos crecer</b> y <b>cambiar la forma de trabajar de los equipos</b>. He dirigido equipos de producto de <b>más de diez personas</b> y uso <b>IA a diario</b> para investigar, prototipar y sacar cosas adelante. Vivo en <b>Zaragoza</b> y trabajo <b>en remoto</b> sin problema.</p>', 1),

    # ---------- bands ----------
    ('aria-label="Deciding what\'s worth building, and shipping it"', 'aria-label="Decidir qué construir, y sacarlo adelante"', 1),
    ("<span>deciding what's worth building</span>", '<span>decidir qué construir</span>', 4),
    ('<span>and shipping it</span>', '<span>y sacarlo adelante</span>', 6),

    # ---------- journey ----------
    ('aria-label="Journey"', 'aria-label="Trayectoria"', 1),
    ('Product, <span class="outline">from<br>the code up.</span>', 'Del código<br><span class="outline">al producto.</span>', 1),
    ('<p class="mono">2014 → now</p>', '<p class="mono">2014 → hoy</p>', 1),
    ('<span class="yrs">Before that</span>', '<span class="yrs">Los inicios</span>', 1),
    ('<span class="role">Software developer</span>', '<span class="role">Desarrollador de software</span>', 1),
    ("Three apps in real people's hands before graduating: wearables, physio clinics and citizen science.",
     'Antes de terminar la carrera ya tenía tres apps en uso: wearables para mayores, clínicas de fisio y ciencia ciudadana.', 1),
    ('<span class="role">Product engineer</span>', '<span class="role">Ingeniero de producto</span>', 1),
    ('Corner-shop sales across Latin America, turned into dashboards for brands like Coca-Cola. $15K in its first month.',
     'Convertimos las ventas de tiendas de barrio de toda Latinoamérica en informes para marcas como Coca-Cola. 15.000 $ de facturación el primer mes.', 1),
    ('<span class="end">code</span>', '<span class="end">código</span>', 4),
    ('<span class="end">product</span>', '<span class="end">producto</span>', 4),
    ('<b>Mostly code</b>', '<b>Sobre todo código</b>', 1),
    ('<b>Half and half</b>', '<b>Mitad y mitad</b>', 1),
    ('<b>Product-led</b>', '<b>Más producto</b>', 1),
    ('<b>Mostly product</b>', '<b>Sobre todo producto</b>', 1),
    ('Ideas taken to live products for startups and corporates, from Iberia to Kpler.',
     'Llevé ideas a producto real para startups y grandes empresas como Iberia o Kpler.', 1),
    ('<b>Weeks</b><span>from idea to live MVP, not quarters</span>', '<b>Semanas</b><span>de la idea al MVP en producción. No trimestres.</span>', 1),
    ('SafeDirect: travel insurance that gives guests a reason to book direct, plugged into insurers and PMSs. Plus AI content generation, and KITT, the first AI receptionist for hotels.',
     'Lancé SafeDirect, un seguro de viaje que anima a reservar directamente en la web del hotel, conectado con aseguradoras y PMS. También trabajé en la generación de contenido con IA y en KITT, el primer recepcionista con IA para hoteles.', 1),
    ('<span>SafeDirect revenue in its first year, and +12% conversion for hotels</span>',
     '<span>de crecimiento en SafeDirect en un año, y un 12 % más de conversión para los hoteles</span>', 1),
    ('</i>Now, since 2025</span>', '</i>Ahora, desde 2025</span>', 1),
    ('The product behind 5,000 pick-up stores. A 15-person team that works on metrics, not deadlines, with AI built into how we work.',
     'Llevo el producto de una red de 5.000 puntos de recogida, con un equipo de 15 personas que se guía por métricas y no por fechas, y que usa la IA en su día a día.', 1),
    ('<span>parcels a month across Spain and Portugal</span>', '<span>paquetes al mes en España y Portugal</span>', 1),

    # ---------- how I work ----------
    ('aria-label="How I work"', 'aria-label="Cómo trabajo"', 1),
    ('<p class="mono eyebrow">How I work</p>', '<p class="mono eyebrow">Cómo trabajo</p>', 1),
    ('Tools change.<br><span class="outline">Judgment compounds.</span>', 'Las herramientas caducan.<br><span class="outline">El criterio, no.</span>', 1),
    ("I use AI wherever it makes the work better, and nowhere just to say I do. What it can't replace is what years of shipping taught me.",
     'Uso la IA donde mejora el trabajo, no por moda. Lo que no puede darme es el criterio que he ganado en años lanzando productos y equivocándome por el camino.', 1),
    ('<h3>I hand to AI</h3>', '<h3>Se lo dejo a la IA</h3>', 1),
    ('<li>Research and synthesis</li><li>Prototypes and code</li><li>Crunching the data</li><li>First drafts of specs</li><li>Repetitive work</li>',
     '<li>Investigación y resúmenes</li><li>Prototipos y código</li><li>Análisis de datos</li><li>Primeros borradores</li><li>Tareas repetitivas</li>', 1),
    ('<h3>Stays with me</h3>', '<h3>Me lo quedo yo</h3>', 1),
    ('<li>Which problem is worth solving</li><li>What users actually need</li><li>What to leave out</li><li>The quality bar</li><li>Getting the team behind it</li>',
     '<li>Qué problema merece la pena resolver</li><li>Qué necesita de verdad el usuario</li><li>Qué se queda fuera</li><li>Dónde poner el listón</li><li>Que el equipo se lo crea</li>', 1),
    ('<p class="mono">My workspace</p><p>Meetings, tasks, data and specs, all in one repo with AI on top.</p>',
     '<p class="mono">Mi espacio de trabajo</p><p>Reuniones, tareas, datos y specs, todo en un mismo repo y con la IA a mano.</p>', 1),

    # ---------- zgzbus ----------
    ('aria-label="Side project"', 'aria-label="Proyecto personal"', 1),
    ('>On the side</p>', '>Por mi cuenta</p>', 1),
    ("Zaragoza's transit data is public. A good app to read it wasn't, so I built one in a few weekends. AI wrote every line of code; every product decision, test and deploy was mine.",
     'Los datos del bus y el tranvía de Zaragoza son públicos, pero no había una buena app para consultarlos. Así que me hice una en unos cuantos fines de semana. La IA escribió el código; las decisiones de producto, los tests y los despliegues fueron cosa mía.', 1),
    ('<span class="mono">Available on</span> iOS, Android and web', '<span class="mono">Disponible en</span> iOS, Android y web', 1),
    ('Try it on the web ↗', 'Pruébala en la web ↗', 1),
    ('alt="zgzbus: Plaza Paraíso stop selected on the map, with its next buses"', 'alt="zgzbus: parada de Plaza Paraíso seleccionada en el mapa, con sus próximos autobuses"', 1),
    ('alt="zgzbus: favourite stops with live arrival times"', 'alt="zgzbus: paradas favoritas con tiempos de llegada en directo"', 1),

    # ---------- how I can help ----------
    ('aria-label="How I can help"', 'aria-label="Cómo puedo ayudar"', 1),
    ('How I can <span class="outline">help.</span>', 'Cómo puedo <span class="outline">ayudar.</span>', 1),
    ('<p class="mono">Four things I do best</p>', '<p class="mono">Lo que mejor se me da</p>', 1),
    ('<p class="for mono">For founders and new bets</p><h3>Taking ideas live</h3><p>From a rough idea to a product people actually use. Prototypes in days, and real users deciding what stays.</p>',
     '<p class="for mono">Para fundadores y proyectos nuevos</p><h3>Sacar ideas adelante</h3><p>De una idea a medio cocinar a un producto que la gente usa. Prototipos en días, y que sean los usuarios quienes decidan qué se queda.</p>', 1),
    ("<p class=\"for mono\">For products with traction</p><h3>Growing what's already live</h3><p>Finding what moves conversion and revenue, testing it fast, scaling what works.</p>",
     '<p class="for mono">Para productos que ya tienen usuarios</p><h3>Hacer crecer lo que ya está en marcha</h3><p>Encontrar qué mueve la conversión y los ingresos, probarlo rápido y escalar lo que funciona.</p>', 1),
    ('<p class="proof mono">SafeDirect: 10x revenue in its first year, +12% conversion</p>', '<p class="proof mono">SafeDirect: 10x en ingresos el primer año, +12 % de conversión</p>', 1),
    ('<p class="for mono">For companies adding AI</p><h3>Bringing AI into products</h3><p>Where AI genuinely helps users, shipped and measured. In production, not in a demo.</p><p class="proof mono">The Hotels Network: AI receptionist, AI content</p>',
     '<p class="for mono">Para empresas que quieren sumar IA</p><h3>Llevar la IA al producto</h3><p>Usarla donde de verdad ayuda al usuario y medir si funciona. En producción, no en una demo.</p><p class="proof mono">The Hotels Network: recepcionista y contenido con IA</p>', 1),
    ('<p class="for mono">For teams that need focus</p><h3>Changing how teams work</h3><p>From shipping tasks to shipping results, with goals and metrics everyone can see.</p><p class="proof mono">Citibox: 15 people now run on metrics</p>',
     '<p class="for mono">Para equipos que necesitan foco</p><h3>Cambiar cómo trabaja un equipo</h3><p>Pasar de entregar tareas a conseguir resultados, con objetivos y métricas que todo el mundo ve.</p><p class="proof mono">Citibox: un equipo de 15 que ahora trabaja con métricas</p>', 1),

    # ---------- about ----------
    ('aria-label="About"', 'aria-label="Sobre mí"', 1),
    ('aria-label="Line portrait of Óscar: bald, glasses, short beard, smiling"', 'aria-label="Retrato a línea de Óscar: calvo, con gafas, barba corta y sonriendo"', 1),
    ('>About</p>', '>Sobre mí</p>', 1),
    ('Raised between <span class="outline">paper and pixels.</span>', 'Criado entre <span class="outline">papel y píxeles.</span>', 1),
    ("I grew up in my grandfather's print shop, watching my mum design on the first Macs. That's where I learned that things should work well and look good. I studied computer engineering, wrote code for six years, then moved into product to decide what's worth building.",
     'Me crie en la imprenta de mi abuelo, viendo a mi madre diseñar con los primeros Mac. Ahí aprendí que las cosas tienen que funcionar y, además, verse bien. Estudié Ingeniería Informática, pasé seis años programando y luego di el salto a producto para decidir qué merece la pena construir.', 1),
    ('<span>Based in Zaragoza, Spain</span><span>Spanish &amp; English</span><span>Off screen: drums</span>',
     '<span>Vivo en Zaragoza</span><span>Español e inglés</span><span>Fuera del trabajo: batería</span>', 1),

    # ---------- contact ----------
    ('aria-label="Contact"', 'aria-label="Contacto"', 1),
    ("<span>Let's talk</span>", '<span>Hablemos</span>', 4),
    ("<span class=\"outline\">Let's talk</span>", '<span class="outline">Hablemos</span>', 4),
    ('<span class="mono">Email</span>', '<span class="mono">Correo</span>', 1),
    ('<p class="big">Always up for a good conversation.<br>About roles, collaborations or just good ideas.</p>',
     '<p class="big">Siempre me apetece una buena charla.<br>Sobre trabajo, colaboraciones o, simplemente, buenas ideas.</p>', 1),
    ('<nav aria-label="Footer"><b>Explore</b><b>Elsewhere</b><a href="#journey">Journey</a>', '<nav aria-label="Pie de página"><b>Explorar</b><b>Encuéntrame</b><a href="#journey">Trayectoria</a>', 1),
    ('<a href="#side">Side project</a><a href="#mail">Email</a><a href="#help">How I help</a>', '<a href="#side">Proyecto personal</a><a href="#mail">Correo</a><a href="#help">Cómo ayudo</a>', 1),
    ('<small>© 2026 Óscar Saboya, Zaragoza, Spain</small>', '<small>© 2026 Óscar Saboya, Zaragoza</small>', 1),
]


def build():
    src = (ROOT / 'index.html').read_text(encoding='utf-8')
    out, problems = src, []
    for en, es, n in T:
        found = out.count(en)
        if found != n:
            problems.append(f'expected {n}, found {found}: {en[:80]}')
            continue
        out = out.replace(en, es)
    if problems:
        raise SystemExit('Spanish build stopped, index.html changed:\n  ' + '\n  '.join(problems))
    dest = ROOT / 'es' / 'index.html'
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(out, encoding='utf-8')
    print(f'wrote {dest.relative_to(ROOT)} ({len(T)} fragments)')


if __name__ == '__main__':
    build()
