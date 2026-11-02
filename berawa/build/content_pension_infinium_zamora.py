# Contenido de la demo Infinium Zamora Suites (Zamora) (es/en/fr/de). Hechos de infiniumzamora.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitaciones Deluxe, Doble Superior y Triple Deluxe','Apartamentos Deluxe'],'en':['Deluxe, Superior Double and Triple Deluxe rooms','Deluxe apartments'],'fr':['Chambres Deluxe, Double Supérieure et Triple Deluxe','Appartements Deluxe'],'de':['Zimmer Deluxe, Doppel Superior und Triple Deluxe','Deluxe-Apartments']}
RD={
'es':['Con Smart TV con Netflix, wifi de fibra gratuito y aire acondicionado. Las Deluxe tienen vista a la ciudad y ducha hidromasaje; hay versión con balcón.','Con salón diáfano, cocina equipada con menaje y electrodomésticos de alta gama, sofá con chaise longue y dos habitaciones con cama de matrimonio.'],
'en':['With Smart TV with Netflix, free fibre wifi and air conditioning. Deluxe rooms have city views and a hydromassage shower; there is a version with balcony.','With an open-plan living room, a kitchen equipped with utensils and high-end appliances, a chaise-longue sofa and two bedrooms with a double bed.'],
'fr':['Avec Smart TV et Netflix, wifi fibre gratuit et climatisation. Les Deluxe ont vue sur la ville et douche hydromassante ; il existe une version avec balcon.','Avec séjour ouvert, cuisine équipée d’ustensiles et d’électroménager haut de gamme, canapé méridienne et deux chambres avec lit double.'],
'de':['Mit Smart-TV mit Netflix, kostenlosem Glasfaser-WLAN und Klimaanlage. Die Deluxe-Zimmer haben Stadtblick und eine Massagedusche; es gibt eine Variante mit Balkon.','Mit offenem Wohnraum, Küche mit Geschirr und hochwertigen Geräten, Sofa mit Chaiselongue und zwei Schlafzimmern mit Doppelbett.']}
ART={
'hero':('skyline',4411,['#1b1d24','#b0814e','#eee0c8','#5a5560','#38353d','#17181d']),
'intro':('columns',4412,['#f2eee8','#faf8f3','#7d5a33','#56505c','#26242a']),
'r1':('arches',4421,['#eee9e1','#d9b07c','#7d5a33','#56505c','#26242a']),
'r2':('columns',4422,['#1b1d24','#bb8a55','#f0e3cd','#615b67','#3d3a43','#1a1b20']),
'g1':('waves',4431,['#1b1d24','#b0814e','#eee0c8','#5a5560','#38353d','#17181d']),
'g2':('arches',4432,['#f2eee8','#faf8f3','#7d5a33','#56505c','#26242a']),
'g3':('hills',4433,['#e8e4dc','#ecdcc2','#d9b07c','#918a86','#68625f','#433f3e']),
'g4':('skyline',4434,['#1b1d24','#bb8a55','#f0e3cd','#615b67','#3d3a43','#1a1b20'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Infinium Zamora Suites · Suites y apartamentos en el centro de Zamora',see_rooms='Ver habitaciones y apartamentos',hero_k='Zamora · Calle Regimiento de Toledo, 21',hero_t='Tu rincón en Zamora',hero_s='Suites y apartamentos en pleno centro, diseñados para el confort de sus huéspedes.',
 intro_t='Delicadeza, diseño y confort',intro_p1='Un nuevo concepto de alojamiento en Zamora: habitaciones deluxe y apartamentos completos que unen la esencia del pasado con la modernidad del presente, en la cuna del románico.',
 intro_p2='Las reservas directas en su web incluyen durante toda la estancia un desayuno continental por huésped en una chocolatería y cafetería a 90 metros, de 7:30 a 10:30.',
 stats=['Centro de Zamora','Habitaciones y apartamentos','Wifi de fibra gratuito','Desayuno incluido reservando directo'],nav_rooms='Alojamientos',rooms_t='Habitaciones y apartamentos',rooms_s='Todos con baño privado, Smart TV con Netflix y wifi gratuito.',
 svcs=['Desayuno continental incluido en reservas directas','Parking privado propio (consultar disponibilidad)','Smart TV con Netflix','Wifi de fibra gratuito','Aire acondicionado frío y calor','Alquiler de apartamentos de temporada'],
 loc_p='Calle Regimiento de Toledo, 21 · 49011 Zamora. Teléfono: 655 295 878. Correo: direccion@infiniumzamora.com.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis apartamentos?','¿Está incluido el desayuno?','¿Cómo reservo?']),
'en':dict(title='Infinium Zamora Suites · Suites and apartments in central Zamora',see_rooms='See rooms and apartments',hero_k='Zamora · Calle Regimiento de Toledo, 21',hero_t='Your corner in Zamora',hero_s='Suites and apartments right in the centre, designed for their guests’ comfort.',
 intro_t='Delicacy, design and comfort',intro_p1='A new concept of accommodation in Zamora: deluxe rooms and full apartments combining the essence of the past with the modernity of the present, in the cradle of the Romanesque.',
 intro_p2='Direct bookings on their website include, for the whole stay, a continental breakfast per guest at a chocolate shop and café 90 metres away, from 7:30 to 10:30.',
 stats=['Central Zamora','Rooms and apartments','Free fibre wifi','Breakfast included when booking direct'],nav_rooms='Accommodation',rooms_t='Rooms and apartments',rooms_s='All with private bathroom, Smart TV with Netflix and free wifi.',
 svcs=['Continental breakfast included in direct bookings','Own private parking (ask for availability)','Smart TV with Netflix','Free fibre wifi','Air conditioning, cooling and heating','Seasonal apartment rentals'],
 loc_p='Calle Regimiento de Toledo, 21 · 49011 Zamora. Phone: +34 655 295 878. Email: direccion@infiniumzamora.com.',
 chips=['Which rooms do you have?','Do you have apartments?','Is breakfast included?','How do I book?']),
'fr':dict(title='Infinium Zamora Suites · Suites et appartements au centre de Zamora',see_rooms='Voir chambres et appartements',hero_k='Zamora · Calle Regimiento de Toledo, 21',hero_t='Votre coin à Zamora',hero_s='Suites et appartements en plein centre, conçus pour le confort de leurs hôtes.',
 intro_t='Délicatesse, design et confort',intro_p1='Un nouveau concept d’hébergement à Zamora : chambres deluxe et appartements complets qui unissent l’essence du passé et la modernité du présent, dans le berceau du roman.',
 intro_p2='Les réservations directes sur leur site incluent, pendant tout le séjour, un petit-déjeuner continental par client dans une chocolaterie-cafétéria à 90 mètres, de 7h30 à 10h30.',
 stats=['Centre de Zamora','Chambres et appartements','Wifi fibre gratuit','Petit-déjeuner inclus en direct'],nav_rooms='Hébergements',rooms_t='Chambres et appartements',rooms_s='Tous avec salle de bains privée, Smart TV avec Netflix et wifi gratuit.',
 svcs=['Petit-déjeuner continental inclus en réservation directe','Parking privé (disponibilité sur demande)','Smart TV avec Netflix','Wifi fibre gratuit','Climatisation chaud et froid','Location d’appartements à la saison'],
 loc_p='Calle Regimiento de Toledo, 21 · 49011 Zamora. Téléphone : +34 655 295 878. E-mail : direccion@infiniumzamora.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous des appartements ?','Le petit-déjeuner est-il inclus ?','Comment réserver ?']),
'de':dict(title='Infinium Zamora Suites · Suiten und Apartments im Zentrum von Zamora',see_rooms='Zimmer und Apartments ansehen',hero_k='Zamora · Calle Regimiento de Toledo, 21',hero_t='Ihr Rückzugsort in Zamora',hero_s='Suiten und Apartments mitten im Zentrum, gestaltet für den Komfort der Gäste.',
 intro_t='Feingefühl, Design und Komfort',intro_p1='Ein neues Unterkunftskonzept in Zamora: Deluxe-Zimmer und komplette Apartments, die die Essenz der Vergangenheit mit der Moderne verbinden, in der Wiege der Romanik.',
 intro_p2='Direktbuchungen über die Website enthalten während des gesamten Aufenthalts ein kontinentales Frühstück pro Gast in einer Chocolatería mit Café 90 Meter entfernt, von 7:30 bis 10:30 Uhr.',
 stats=['Zentrum von Zamora','Zimmer und Apartments','Kostenloses Glasfaser-WLAN','Frühstück inklusive bei Direktbuchung'],nav_rooms='Unterkünfte',rooms_t='Zimmer und Apartments',rooms_s='Alle mit eigenem Bad, Smart-TV mit Netflix und kostenlosem WLAN.',
 svcs=['Kontinentales Frühstück bei Direktbuchung inklusive','Eigener Privatparkplatz (Verfügbarkeit anfragen)','Smart-TV mit Netflix','Kostenloses Glasfaser-WLAN','Klimaanlage mit Kühl- und Heizfunktion','Apartments zur Saisonmiete'],
 loc_p='Calle Regimiento de Toledo, 21 · 49011 Zamora. Telefon: +34 655 295 878. E-Mail: direccion@infiniumzamora.com.',
 chips=['Welche Zimmer gibt es?','Haben Sie Apartments?','Ist das Frühstück inklusive?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://infiniumzamora.com/ohbe/?ohbe=booking'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Infinium Zamora Suites',ac='#1b1d24',ac2='#7d5a33',ac2_a11y='#654625',book=BOOK,around=[],foot=FOOT,
 address='Calle Regimiento de Toledo, 21 · 49011 Zamora',phones=['+34 655 295 878'],emails=['direccion@infiniumzamora.com'],maps='Infinium Zamora Suites, Calle Regimiento de Toledo 21, 49011 Zamora',t=T)
META=dict(repo='demo-pension-infinium-zamora',name='Infinium Zamora Suites',legal_name='NEW ERA APARTAMENTS S.L.U., NIF B49299621 (aviso legal de su web)',registry_ids=['B49299621'],
 url='https://infiniumzamora.com/',domain='infiniumzamora.com',municipality='Zamora',province='Zamora',sector='suites y apartamentos en el centro de Zamora',
 read_at='2026-11-02T09:05:00+01:00',created_at='2026-11-02T09:04:00+01:00',built_at='2026-11-02T09:15:00+01:00',audit_date='2026-11-02T09:05:00+01:00',
 rating=dict(value=4.4,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Pensi%C3%B3n+Infinium+Zamora+Suites+Zamora'),
 book=dict(mode='engine',url=R,note='motor propio de su web (boton Reservar Ahora): https://infiniumzamora.com/ohbe/?ohbe=booking, HTTP 200 (02/11/2026 09:05). Solo en espanol, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis apartamentos?','K02'),('¿Qué tienen las habitaciones?','K03'),('¿Está incluido el desayuno?','K04'),('¿A qué hora es el desayuno?','K04'),('¿Hay parking?','K05'),('¿Dónde estáis?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Alquiláis por temporada?','K08'),('¿Qué ver en Zamora?','K09'),('¿Cuál es vuestro teléfono?','K10'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have apartments?','K02'),('What do the rooms include?','K03'),('Is breakfast included?','K04'),('What time is breakfast?','K04'),('Is there parking?','K05'),('Where are you?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Do you offer seasonal rentals?','K08'),('What to see in Zamora?','K09'),('What is your phone number?','K10'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous des appartements ?','K02'),('Que comprennent les chambres ?','K03'),('Le petit-déjeuner est-il inclus ?','K04'),('À quelle heure est le petit-déjeuner ?','K04'),('Y a-t-il un parking ?','K05'),('Où êtes-vous ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Louez-vous à la saison ?','K08'),('Que voir à Zamora ?','K09'),('Quel est votre numéro de téléphone ?','K10'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie Apartments?','K02'),('Was bieten die Zimmer?','K03'),('Ist das Frühstück inklusive?','K04'),('Wann gibt es Frühstück?','K04'),('Gibt es einen Parkplatz?','K05'),('Wo liegt die Unterkunft?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Vermieten Sie saisonal?','K08'),('Was kann man in Zamora besichtigen?','K09'),('Wie ist Ihre Telefonnummer?','K10'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
