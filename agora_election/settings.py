import os
import re
import logging
ROOT_PATH = os.path.dirname(__file__)

########### agora-election

SITE_NAME = "Agora-Election"

# change for each election
CURRENT_ELECTION_ID = 0

ADMINS = (
    ('Bob Marley', 'bob@example.com'),
)

# delay tasks if needed. sqlite needs it
TASKS_DELAY = 1

# registration will only allow numbers with this format
ALLOWED_TLF_NUMS_RX = "^\+34[67]\\d{8}$"

# checks pipeline for sending an sms, you can modify and tune it at will
SMS_CHECKS_PIPELINE = (
    ("checks.check_has_not_voted", None),
    ("checks.check_tlf_whitelisted", None),
    ("checks.check_ip_whitelisted", None),
    ("checks.check_blacklisted", None),
    ("checks.check_ip_total_max", dict(total_max=8)),
    ("checks.check_tlf_total_max", dict(total_max=7)),
    ("checks.check_tlf_day_max", dict(day_max=5)),
    ("checks.check_tlf_hour_max", dict(hour_max=3)),
    ("checks.check_tlf_expire_max", None),
)

# timeframe within the SMS message should either be sent or we should give up
# sending a specific SMS. it's also used so that an user have to wait
# SMS_EXPIRE_SECS to send the next sms message
SMS_EXPIRE_SECS = 120

# format the sms message
SMS_MESSAGE = "%(server_name)s: your token is: %(token)s"

# number of guesses for one token
MAX_TOKEN_GUESSES = 5

# timeframe within which a token is said to be valid
SMS_TOKEN_EXPIRE_SECS = 60*10

AGORA_SHARED_SECRET_KEY = "<shared key>"

########### data

AGORA_ELECTION_DATA = dict(
    parent_site=dict(
        name="www.podemos.info",
        url="//www.podemos.info",
    ),
    election_url='https://local.dev/edulix/hola/election/primarias-de-la-confederacion-pirata-para-el-parlamento-europeo15/vote',
    title="Primarias abiertas al Parlamento Europeo",
    subtitle="Una candidatura popular y ciudadana",
    short_description="Es la hora del protagonismo popular y ciudadano. Ayúdanos a confeccionar la lista electoral, votando en 3 sencillos pasos: regístrate, verifica un código que te llegará por SMS, y accede a la cabina de votación donde podrás seleccionar hasta 3 candidatos.",
    start_voting="20 marzo, 10:00",
    end_voting="27 marzo, 10:00",
    num_seats="55",
    tlf_no_rx=ALLOWED_TLF_NUMS_RX,
    candidates=[
                {
                    "a": "ballot/answer",
                    "value": "Juan Bautista Esteve Ramos",
                    "details": "Soy recién estudiante de derecho, con inglés superior y técnico de informática. Actualmente trabajo en la Administración de Justicia en Vinaroz.<p></p>Hace años que me introduje en el movimiento Pirata y mi primera acción importante fue llevar la territorial de Castellón a las generales dentro del Partido Pirata. Creo en el movimiento, no en unas siglas, por lo que cualquier cosa que entorpezca el crecimiento de este movimiento, para mí es prescindible. Creo en la unión y no en que cada cual vaya por su lado.<p></p>Me mueve sobretodo esta guerra cibernética contra la neutralidad en la red que se vive desde hace unos años. Sin una información libre, no hay una democracia real, por lo tanto, creo firmemente en la necesidad de que la gente pueda disponer de unos medios para comunicarse libremente, ya sea con mala o buena información, y donde pueda expresarse sin tapujos.<p></p>También veo que la casta política que nos gobierna hoy en día no tiene conciencia sobre los derechos humanos, sino sobre el dinero que pueden ganar con ello.<p></p>Creo que la gente ha de tener el derecho a decidir y a equivocarse, por ello creo en una democracia directa. Pero me vale cualquier tipo de democracia que mejore la actual, de momento.<p></p>No sé si seré el más indicado para estar como candidato principal, pero sí creo que ha de haber diversidad para que la gente pueda opinar sobre lo que quiere.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/46.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/46"
                        },
                        {
                            "title": "@jbesteve",
                            "url": "https://www.twitter.com/jbesteve"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/Izgraull"
                        },
                        {
                            "title": "Web",
                            "url": "https://pensamientosbajocero.blogspot.com/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Pedro Vera Blanco",
                    "details": "Solo soy un joven, que a punto de acabar su carrera de Derecho, quiere hacer algo por los que lo rodean. Me apasiona la política y que si no he entrado antes en ella es porque me asquea el funcionamiento de los partidos convencionales.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/7.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/7"
                        },
                        {
                            "title": "@PedroVeB",
                            "url": "https://twitter.com/PedroVeB"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/pedro.verablanco?fref=ts"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Juan Jesus Lopez Aguilar",
                    "details": "Soy conductor de camión en transporte internacional. Tengo 48 años y tres hijos.<p></p>Preocupado siempre por conocer las diferentes propuestas posibles a todos los temas que afectan al funcionamiento de la sociedad, porque al final son los que afectan al día a día de todos nosotros.<p></p>Entiendo que el futuro está en una sociedad informada e implicada, donde lo más importante sea escuchar a la ciudadanía en todos los temas, y sobre todo no actuar por dogmas preestablecidos. Vivimos en un mundo en constante cambio, donde es muy importante aprender de tiempos pasados, sobre todo para no repetir errores.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/34.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/34"
                        },
                        {
                            "title": "@lopezaguilarjj",
                            "url": "https://twitter.com/lopezaguilarjj"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/animalenmoto"
                        },
                        {
                            "title": "Web",
                            "url": "https://www.facebook.com/LiberemosElFuturo"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Eduardo Bondad Jañez",
                    "details": "Nací y me eduqué en el País Vasco. Vivo en Galicia desde hace más de 30 años. Trabajé más de 16 para la Administración Central, \"jubilado\" a los 44 por protocolo anti-filtraciones: asuntos inabarcables desde España, posible financiación irregular de partidos. \"Conoce a tu enemigo\".",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/38"
                        },
                        {
                            "title": "@eduarbj",
                            "url": "https://twitter.com/eduarbj"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Andrés Roca Pascual",
                    "details": "Nací en 1983 en el seno de una familia obrera: mi madre trabajaba en un videoclub y mi padre era el sargento más joven de la Guardia Urbana de Barcelona. A los 9 años mi padre abandonó a mi madre, y dos años más tarde fue despedido fulminantemente de su empleo por... bueno, básicamente por corrupto e imbécil.<p></p>Mientras tanto mi madre nos sacó adelante a mi hermano siete años menor y a mí, trabajando horas y horas, pasando hambre muchas veces, trabajando y trabajando para pasar el día a día, para cubrir las deudas que mi padre dejó, para pagar como podía la luz, el agua, etc.<p></p>Ello me enseñó como nada podría enseñar lo importante que es ser responsable, honesto e íntegro. Cada vez que alguien hace algo deshonesto hace daño a otra persona. Crea una pirámide de dolor que puede y debe evitarse.<p></p>Con su actitud mi madre también me enseñó a ser consecuente, fiel, a ver las cosas con actitud lógica y fría, pero al mismo tiempo a buscar la calidez y la humanidad de cada acción. A amar cada acción que emprendo, a luchar por aquello en lo que creo y a no ser cerrado de mente.<p></p>Ese soy yo: la consecuencia de mis elecciones, el resultado de mi lucha y la de otros. Y creo que ahora me toca a mí luchar para que otros se puedan beneficiar de mi experiencia sin tener que sufrirla.<p></p>Creo en un mundo mejor. Y creo que puedo y debo ayudar a construirlo.",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/44"
                        },
                        {
                            "title": "@AndresPRoca",
                            "url": "https://twitter.com/AndresPRoca"
                        },
                        {
                            "title": "Facebook",
                            "url": "http://www.facebook.es/AndresPRoca"
                        },
                        {
                            "title": "Web",
                            "url": "http://www.andresproca.com/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Lorena Müller",
                    "details": "Nací en Buenos Aires, Argentina en septiembre de 1975; desde el 2002 vivo en Madrid, España. Soy fotógrafa profesional especializada en artes visuales.<p></p>Participo en diversas plataformas o grupos de arte y política. Fui co-coordinadora de \"Inside Out Project | Be the Change\" en España durante 2012 y 2013. Además, coordino el área de Formación para \"Geneación eMe\" (asociación fotográfica), desde 2012.<p></p>Soy militante de Derechos Humanos desde mi paso por la universidad y he pertenecido a una agrupación estudiantil en Argentina durante esa época. Soy activista en la Plataforma Democracia real YA! y 15Mayista.<p></p>Participo en Toma los Medios. También soy streamer para DRY Madrid: http://bambuser.com/channel/DRYMadrid. Durante mi corta estancia en Catalunya, junto a otras personas, creamos el nodo de Democracia real YA! en Girona (nodo al que sigo vinculada).<p></p>Trabajo como Community Manager para dos colectivos y en muchos otros proyectos o acciones como \"Renta Básica de 2013\" y \"Let me vote!\", ambos Iniciativas Ciudadanas Europeas. Además soy socia de Greenpeace Argentina y España.<p></p>Me incorporé a la Confederación Pirata atraída por la posibilidad de colaborar en el programa europeo y estoy interesada en la Democracia Directa , la Igualdad y la defensa de los Derechos Humanos. Hace pocos días me afilié a Piratas de Madrid.<p></p>En cuanto a ideología política, soy de izquierdas y antifascista.<p></p>At the begining, I've made my presentation in Spanish and English... but, you know... I found the 1400 characters limit so I've deleted the English part.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/42.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/42"
                        },
                        {
                            "title": "@lmn_ar",
                            "url": "https://twitter.com/lmn_ar"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Ruben Romero Berrocal",
                    "details": "Me llamo Rubén Romero Berrocal, nacido el 22 de mayo de 1987, casado y con dos hijos. Resido en la población de Onda (Castellón).<p></p>Mis estudios son los de haber cursado dos ciclos formativos (electrónica, comercio y marketing) sin haberlos finalizado.<p></p>En idiomas, hablo castellano y valenciano nativos e ingles en nivel elemental.<p></p>Trabajo en el sector azulejero de operario de esmaltadoras y KERAJET INK en Azulev S.A.U. Actualmente estoy afiliado al sindicato USO en mi empresa, siendo enlace sindical del mismo.<p></p>Mi motivación es la de llevar al movimiento pirata de España a ser tan fuerte como para plantar cara en una eurocamara.<p></p>Mi vinculación al movimiento pirata: oy el presidente del partido pirata de Onda y en un año pasamos de no ser nada a estar al mismo nivel, en reconocimiento mediático, que PSOE Y PP en Onda, creando departamentos explícitos para materia de prensa, actuaciones, merchandising y demás con el \"sistema de avales\" que creé.<p></p>¿Que podría aportar? Lo que he ido aprendiendo a lo largo de mi vida de las personas que he tratado y trasladar todas sus necesidades, desde el autónomo ahogado con los módulos y pagos, pasando por los currantes de a pie hasta las personas que no tienen donde vivir. Mi experiencia a la hora de formar un grupo estable de trabajo y poder darle alas para poder trabajar de forma eficiente.<p></p>Salud y Ron.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/14.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/14"
                        },
                        {
                            "title": "@lmn_ar",
                            "url": "https://twitter.com/R_de_romero"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/ruben.romeroberrocal"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Borja Bethencourt Muñoz",
                    "details": "Mi nombre es Borja Bethencourt Muñoz. Nací en Las Palmas de Gran Canaria hace 29 años. Crecí en un colegio de Jesuitas y estudié Periodismo en la Complutense (Madrid). Luego comencé mi vida laboral en la capital de España, pero muy pronto (2009) me fui a Berlín, donde he desempeñado todo tipo de trabajos.<p></p>Me defino como una persona con gran capacidad para comunicar, humilde, muy abierto y curioso. Me interesan las culturas, el conocimiento, las lenguas, las personas. Me gusta observar todas las realidades posibles antes de tomar una decisión o de realizar un juicio. No entiendo de etiquetas y sí creo en una política nueva, humana (y no por y para las grandes empresas), de progreso, orientada hacia las nuevas tecnologías, las cuales, sin duda alguna y si entre todos ponemos un poco de empeño, nos podrán llevar avante a toda vela.<p></p>Conozco al partido Pirata porque lo voté en las últimas elecciones a la alcaldía de Berlín. Sin duda alguna, los \"Piraten\" fueron el partido con el que mejor me identificaba. Jóvenes, de ideas de futuro y atendiendo a los problemas del siglo XXI, fuera de toda red de corruptelas, tristemente tan incrustadas e instaladas en los grandes partidos. Ahora que existe la oportunidad, me gustaría representar a los Piratas, con ilusión, ganas y sobre todo mucha humildad.<p></p>Agradecido por brindarme la oportunidad de presentar mi candidatura,<p></p>Borja.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/9.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/9"
                        },
                        {
                            "title": "@Canariae",
                            "url": "https://twitter.com/Canariae"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/borjachussets.oregon"
                        },
                        {
                            "title": "Web",
                            "url": "http://bbethencourt.wordpress.com/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Carlos González Iglesias",
                    "details": "Charro. Nacido en Salamanca y residente en Alcoletge, Lleida. Nacido en el 77 y de estudios, Empresariales. Funcionario de la AGE. De idiomas, domino el castellano con tacos, nivel medio en Inglés y catalán, bajo en Francés.<p></p>Me gustaba la política, pero ahora creo que mi formación y conocimientos pueden ayudar a cambiar, poco a poco, el sistema democrático de la Unión Europea. Consciente de los sacrificios que debiera hacer en caso de ser finalmente elegido eurodiputado, y que estos sacrificios serán para 5 años.<p></p>El Europarlamento genera o verifica el 70% de la legislación que afecta a los Españoles y por ello mi voto, será el que los españoles digan, conforme al sistema Pirata-Europeo que se decida.<p></p>Experiencia en elecciones: interventor del Estado en Elecciones 2011 (ambas) y primero de la Candidatura de Pirates de Catalunya en Lleida. Hasta el 8 Febrero miembro de la Junta de PIRATA.CAT.<p></p>No pertenezco a ningún movimiento social, ni afiliado a ningún gran sindicato. Poco amante de las manifestaciones, porque de poco sirven. Y respecto de la economía, opino que el sistema actual \"necesita\" paraísos fiscales, entre otras cosas porque Chipre, Malta y Luxemburgo, lo son. Seducido por la Renta Básica Universal.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/20.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/20"
                        },
                        {
                            "title": "@carlos_1377",
                            "url": "https://twitter.com/carlos_1377"
                        },
                        {
                            "title": "Web",
                            "url": "http://elotrodogc.blogspot.com.es/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Jose Andrés Diz Alonso",
                    "details": "Soy un ciudadano interesado en temas de cultura libre, conocimiento compartido, autogestión, reciclaje y reutilización (en particular recuperación y transformación de objetos en desuso u obsolescencia), en general la cultura hacker y DIY. Soy licenciado en informática y estoy comprometido, en mayor o menor grado, en iniciativas de software libre y open hardware.<p></p>Mi contacto con el movimiento pirata se inició a través de The Pirate Bay y sus iniciativas, así como el seguimiento de diversos activistas vinculados de una forma u otra al partido pirata y al mundo del FLOSS|H.",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/30"
                        },
                        {
                            "title": "@pepdiz",
                            "url": "https://twitter.com/pepdiz"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/pep.diz"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Renato Domínguez Presa",
                    "details": "Nací en Río de Janeiro (Brasil) en 1978. Hijo (y nieto) de emigrantes gallegos, volví a estas tierras, Europa, en el 1988.<p></p>Académicamente, tengo el título de Ingeniero de Telecomunicación por la Universidade de Vigo.<p></p>Personalmente, a lo largo del tiempo, estas son algunas de las inquietudes que cultivé: malabarista, payaso, eco-agricultor, acompañante en una escuela libre, libertario, dibujante, matemático, filósofo, humanista, aprendiz.<p></p>La principal motivación para presentarme a la candidatura es activar a la gente hacia el optimismo y la alegría de ver que nos estamos moviendo, que el cambio es continuo, y que lo que tenemos es lo que escogemos. También me mueven las ganas de aprender de la política, algo que en este momento, considero un deber para mí.<p></p>Conocí el movimiento pirata en el año 2007, recién llegado de un viaje a Brasil y recién empezado estaba el movimiento. El año pasado me pongo en contacto con los piratas gallegos, y ahora soy el secretario general del partido Piratas de Galicia.<p></p>Espero y confío dar lo mejor de mí mismo. Como decíamos en el patio de juego: \"¡por mí y por todos mis compañeros!\"",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/36.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/36"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/rena.renato.3"
                        },
                        {
                            "title": "Web",
                            "url": "http://www.tururuvigo.blogspot.com.es/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Iván Eguiguren Martín",
                    "details": "Nací en Madrid hace 40 años. Soy administrador de sistemas GNU/Linux. Tengo la suerte de poder trabajar con sistemas no privativos desde hace más de 12 años y en casa tampoco lo más parecido son los androids.<p></p>Conocí el partido pirata hace años y, pensando que sólo trataba el tema de internet, quedó en una parte de mi memoria con una etiqueta de simpatía hacia él. A día de hoy tengo dos hijos pequeños y me alegró ver que este partido se preocupa de un pilar tan importante para una sociedad como la educación, y después la cultura y después la democracia directa.<p></p>El caso es que no pude evitar afiliarme viendo que soy tan afín a toda su ideología y, precisamente por eso, no quiero que no podamos presentarnos al parlamento europeo porque no haya suficientes candidat@s.",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/51"
                        },
                        {
                            "title": "@ivan_eguiguren",
                            "url": "https://twitter.com/ivan_eguiguren"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Luis Cuerdo Galarraga",
                    "details": "Hola, soy de Tolosa, Gipuzkoa, tengo 34 años y soy traductor autónomo, actualmente resido en Inglaterra.<p></p>Quiero vivir de primera mano el proceso de primarias en la Confederación, mi principal interés es la democracia directa y el desarrollo de herramientas para la mejorar de la participación, comunicación y colaboración ciudadana de manera horizontal.<p></p>Estoy vinculado a Piratas de Madrid, Piratas de Reino Unido, colaboro con Pirate Times, también soy miembro del Partido de Internet.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/10.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/10"
                        },
                        {
                            "title": "@luis_cuerdo",
                            "url": "https://twitter.com/luis_cuerdo"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/luis.cuerdo"
                        },
                        {
                            "title": "Web",
                            "url": "https://www.luiscuerdo.com/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Gonzalo Heredia Borreguero",
                    "details": "Tengo 25 años, he nacido en Salta, Argentina, de padre argentino y madre barcelonesa. Llevo viviendo en Barcelona desde los dos años, pese haber residido en otros países de forma temporal: Erasmus, prácticas laborales, etc.<p></p>Actualmente estoy acabando la carrera de arquitectura en la UPC (Barcelona).<p></p>He formado parte de varias asociaciones estudiantiles y actualmente soy miembro de la comisión permanente en catalunya de IAESTE (international association for the exchange of students for technical experience): http://www.iaeste.org<p></p>Conocí el Partido Pirata hace tiempo en otros países de la UE y en las anteriores elecciones autonómicas me interesé por el partido pirata en Catalunya, tras leer el programa y conocer la manera de proceder del mismo decidí darle mi apoyo en las elecciones ya que consideró que el actual sistema de partidos y la organización política general del país se encuentra totalmente obsoleta.<p></p>Tengo grandes esperanzas en que la forma de hacer del partido pirata, centrada en la participación directa de la ciudadanía, sea los cimientos de la democracia del sigo XXI, ya que si continúa el sistema de partidos actual tendremos en un futuro próximo una sociedad cada vez más injusta fruto de una estructura de poder desligada de los ciudadanos.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/8.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/8"
                        },
                        {
                            "title": "Facebook",
                            "url": "http://facebook.com/gon.heredia"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Javier León Gómez",
                    "details": "Javier León reside en Madrid. Nació en Barcelona en 1973. Diplomado en Trabajo Social y Licenciado en Antropología por la Universidad Autónoma de Barcelona, realiza desde la Universidad de Sevilla su tesis doctoral sobre comunidades utópicas, apoyo mutuo y cooperación..<p></p>Antropólogo y editor de varios sellos editoriales (Dharana, Séneca y Nous), presidente de la fundación Dharana, la cual promueve la construcción de comunidades de vida alternativa, ha publicado más de siete libros de temáticas sociales y culturales y participa activamente dando conferencias, colaborando en libros de diferentes temáticas o coordinando proyectos de apoyo mutuo y cooperación. En su blog www.creandoutopias.net escribe diariamente, de forma crítica y a veces polémica sobre cuestiones sociales y culturales..<p></p>Ha participado activamente en política teniendo algunos cargos que le dotan de experiencia suficiente. Vinculado desde hace años a movimientos sociales y culturales, ha luchado desde diferentes frentes por crear una sociedad más justa y positiva. Insumiso al servicio militar, estuvo cuatro años en caza y captura hasta que llegó la amnistía general. Recientemente vinculado al movimiento pirata, desea contribuir a crear alternativas políticas alejadas de lo rancio y tradicional. ",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/52.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/52"
                        },
                        {
                            "title": "@XJavierLeon",
                            "url": "https://twitter.com/XJavierLeon"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/xavileongomez"
                        },
                        {
                            "title": "Web",
                            "url": "http://creandoutopias.net/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Joan Carles Hinojosa Galisteo",
                    "details": "Nací en un pueblo de la provincia de Lleida (Tàrrega), donde cursé mis estudios obligatorios y el bachillerato. Tengo 20 años y estoy estudiando biotecnología en la Universitat de Lleida.<p></p>Siempre he estado interesado en la economía, política e historia (además de en la ciencia); autodidacta, me he informado a diario sobre el mundo gracias a muchas fuentes que proporciona Internet, \"lugar\" en el que he crecido. Todo ello me ha llevado a adquirir una consciencia global y a tener ideas a largo plazo.<p></p>Se necesita un cambio decidido, centrado en el bienestar y la sostenibilidad ambiental, factores que solamente se pueden mejorar mediante al desarrollo de la cientificoténico. Los partidos gobernantes siguen siendo tradicionalistas al respecto, no se preocupan por hacer un cambio real, ya que estaríamos hablando de una renovación política, social y económica. El Partido Pirata puede ofrecer a la población ese cambio, siempre respetando la propia opinión del pueblo expresada a través de distintos mecanismos democráticos.<p></p>Soy firme defensor de la libertad en Internet, opino que debe funcionar como lo que es: un mundo en sí mismo, independiente. Esta es la única forma para que nos pueda ser útiles a las personas. Internet es y será por mucho tiempo una herramienta primordial para todos los aspectos de nuestras vidas, también la principal para llevar a cabo la gran renovación.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/16.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/16"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Jonattan Nieto Sánchez",
                    "details": "Estudiante de Ingeniería Informática, nacido en 1992 en Salamanca. Residente en Cataluña desde 1998.<p></p>Busco en el movimiento pirata una representación de la sociedad real, a favor de la justicia y la igualdad social.",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/45"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Alejandro Lebrero Climent",
                    "details": "Hola, mi nombre es Alex, aunque en internet me conocen como Fireman, tengo muchos seguidores puesto que he sido varias veces campeón de Europa y España de modding. Tengo 39 años y soy de Barcelona. Ingeniero de sistemas y soltero ;)<p></p>Creo que el partido pirata es el único que ahora mismo da la seguridad de ser un partido honesto y sin engaños.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/43.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/43"
                        },
                        {
                            "title": "Facebook",
                            "url": "http://www.facebook.com/alex.lebrero"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Rubèn-Dario Castañé Carmona",
                    "details": "Cosecha del 85, catalán con ascendencia andaluza y espíritu pirata, me presento para construir una nueva Europa desde dentro.<p></p>Profesionalmente soy administrador de sistemas y una de mis pasiones es la política, acompañada por un sentimiento de deber ante las injusticias y el expolio que sufrimos.<p></p>Quiero una política de la ciudadanía, por y para el pueblo. Creo en una nueva Unión Europea. Una federal que reconozca a todos sus pueblos, culturas y lenguas. Una que no priorice los datos económicos por encima los datos sociales.<p></p>Y creo que esto sólo es posible con un cambio de paradigma como el que supone la Confederación Pirata, una red ciudadana unida por un ideario muy sencillo pero poderoso.<p></p>Hablo castellano, catalán, inglés y un poco de francés y soy una mente inquieta, ávida de conocimiento.<p></p>He trabajado en Pirates de Catalunya desde 2010, realizando desde tareas técnicas hasta campañas completas. He coordinado las últimas campañas electorales, además de colaborar en Yo Avalo, Megacomplaint, la creación de la Confederación Pirata, etc. Actualmente coordino y creo infraestructura, y gestiono las redes sociales.<p></p>También he desarrollado proyectos como Qomun (cultura libre), socvot (información electoral) y la coordinación/portavocía de la ECI por la Renta Básica.<p></p>Ahora quiero trabajar por una Europa de las personas, no de los mercados.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/18.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/18"
                        },
                        {
                            "title": "@im_dario",
                            "url": "https://twitter.com/im_dario"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://facebook.com/im.dario"
                        },
                        {
                            "title": "Web",
                            "url": "http://thinkship.cc/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Fabián Plaza Miranda",
                    "details": "Me llamo Fabián Plaza. Tengo 40 años, estoy casado y tengo una hija. Soy abogado especializado en Nuevas Tecnologías y escritor semiprofesional. Y un orgulloso Pirata.<p></p>Es importante que cada uno ofrezca al movimiento Pirata las habilidades que posea. Me presento como candidato porque creo que tengo ciertas aptitudes que nos pueden ser útiles.<p></p>Al ser abogado conozco cómo funcionan las leyes. Además, en mi etapa de opositor al Cuerpo Diplomático obtuve amplios conocimientos y títulos centrados en Derecho Internacional (ideal para la Unión Europea).<p></p>Hablo varios idiomas, entre ellos inglés y francés a nivel de Cuerpo Diplomático (cercano a traducción/interpretación).<p></p>El ser escritor me permite frenar argumentos tipo “no pensáis en los autores” . En general, me considero buen divulgador y comunicador. Un ejemplo de esto es que un artículo mío del Pirate Times fue el más leído de su primer año de vida.<p></p>He colaborado con PIRATA, con .CAT y ahora con .GAL, sobre todo redactando documentos y estudiando leyes. Es decir, tengo una visión de conjunto de bastantes zonas de la Confederación. También tengo una relación personal con varias de esas zonas: soy madrileño, he pasado toda mi vida en Cataluña, ahora resido en Galicia,...<p></p>Mi enfoque para los problemas es buscar siempre una solución pactada y dialogada, escuchando a todas las partes. Soy un pacifista convencido.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/22.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/22"
                        },
                        {
                            "title": "@fabianplaza",
                            "url": "https://twitter.com/fabianplaza"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/TaoCat"
                        },
                        {
                            "title": "Web",
                            "url": "http://www.fabianplaza.com/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Virginia Rubio López",
                    "details": "He sido representante de los trabajadores en la Universidad de Alcalá en la cual trabajo. Quisiera poner patas arriba este estado en el que vivimos. Me considero anarquista.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/13.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/13"
                        },
                        {
                            "title": "@vitalidad",
                            "url": "https://twitter.com/vitalidad"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/vitalidad"
                        },
                        {
                            "title": "Web",
                            "url": "http://www.vitalidad2.blogspot.com/"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Rodrigo Ivan Rivera Troncoso",
                    "details": "Mi nombre es Rodrigo Rivera, de profesión abogado y Técnico en Radiología en el Hospital Clínico de Barcelona, ejerzo como abogado de mi propio despacho desde el año 2009, y como Técnico desde el año 1992.<p></p>Mis motivos para iniciar esta andadura son simplemente hastío, cansancio y repugnancia. Esto es lo que me sugiere la política pero ya no en si la política si no sus representantes, que no los míos, por ello mi manera de pensar me obliga por principios a tomar la decisión de cambiar las cosas. Los cambios han de provenir desde dentro de las instituciones, sino no será posible, ya que las razones para una revolución social ya se dan a día de hoy, sin embargo la chispa aún no ha encendido la sociedad. Siempre he sido de la idea de que no esperes que los demás hagan nada por ti, intenta tú cambiar las cosas.<p></p>Mi involucración con la sociedad proviene a raíz del contacto con el tejido social más dañado, mi relación con la sanidad unida a mi relación jurídica complementa y afianza la idea de efectuar un cambio social. A mi parecer esta es mi vinculación con el movimiento ya que no he tenido ocasión aun de participar de forma activa en dicho movimiento.<p></p>Estas son mis razones y motivos para presentarme como candidato, muchas gracias por esta oportunidad.",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/41"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Juan Alberto Carreira Gomez",
                    "details": "Nací en el año 1970, por lo que tengo 43 años, en Vigo. Siempre he sido una persona con iniciativas sociales, he sido colaborador de Proyecto Hombre (reinserción de toxicómanos) y soy presidente fundador de un club de fútbol sala (SD Nosas Rúas).<p></p>Mucha gente me considera extraño, ya que entre mis prioridades no existe el dinero y trato de llevar una vida acorde con mis principios. Para mí siempre será más satisfactorio hacer algo por la sociedad que acumular dinero. La creación del club de fútbol sala en el año 1999 fue para aportar mi grano de arena a la formación de la gente joven y una de las premisas es tratar de acercar el deporte a la juventud de forma gratuita.<p></p>Con el movimiento pirata tuve contacto a través de Isa de Vigo, a la que conocí casualmente en una manifestación en la ciudad en la que yo portaba una bandera pirata. Os he seguido y trato de estar informado de todo lo que hacéis, aunque ha sido un año difícil para aportar más directamente, debido al nacimiento de mis mellizos y un problema grave de salud de mi madre.<p></p>Me gustaría formar parte de vuestro partido ya que sobre todo es un partido que acepta a cualquier ideología.",
                    "details_title": "Presentación y motivos",
                    "media_url": "",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/50"
                        },
                        {
                            "title": "Facebook",
                            "url": "https://www.facebook.com/juanalberto.carreiragomez.9"
                        }
                    ]
                },
                {
                    "a": "ballot/answer",
                    "value": "Arturo Martínez Nieves",
                    "details": "NTengo 41 años y llevo involucrado con el movimiento pirata desde el 2009 cuando formé parte de la junta de PIRATA.<p></p>Acudí en 2 ocasiones a la asamblea anual del PPI en calidad de delegado de PP-ES. Asimismo serví 2 años en el Court of Arbitration del PPI.<p></p>Me caracterizo por mi talante afable y conciliador. He vivido 15 años en Inglaterra y 5 en Alemania, por ello en parte me siento un ciudadano europeo.",
                    "details_title": "Presentación y motivos",
                    "media_url": "https://agora.confederacionpirata.org/static/img/cands/33.jpg",
                    "urls": [
                        {
                            "title": "Preguntas",
                            "url": "http://piratas2014.eu/candidates/33"
                        },
                        {
                            "title": "@artooraw",
                            "url": "http://www.twitter.com/artooraw"
                        }
                    ]
                }
    ],
    tos=dict(
        title="He leído y acepto las condiciones",
        text="De acuerdo con lo dispuesto en la Ley Orgánica 15/1999, de 13 de diciembre, de protección de datos de carácter personal, informamos que los datos personales recogidos aquí serán incorporados a un fichero titularidad de la Asociación por la Participación Social y Cultural con CIF G8693671 creada para esta la gestión administrativa de esta iniciativa. El fichero está inscrito en el Registro General de la Agencia Española de Protección de Datos. Mediante el envío del formulario existente en esta página web, el/la remitente presta su consentimiento al tratamiento automatizado de los datos incluidos en el mismo. Nos comprometemos asimismo al uso responsable y confidencial de los datos, garantizando que los datos de las/los usuarios se tratarán de acuerdo con las exigencias legales. En ningún caso los datos facilitados serán objeto de venta ni cesión a terceros. Podrá ejercitar los derechos de acceso, rectificación, cancelación y oposición establecidos en dicha Ley a través de correo electrónica, adjuntando fotocopia de su DNI/Pasaporte, en la siguiente dirección: participasocialcultural@gmail.com"
    ),
    faq_questions=[
        dict(
            question="¿cual es la pregunta?",
            answer="algo lorem ipsum"
        ),
        dict(
            question="¿cual es la preguntaaa?",
            answer="algo lorem ipsum algo lorem ipsum"
        ),
    ],
    authorities=[
        dict(
            name="AgoraVoting",
            url="https://agoravoting.com",
            description="<p>Es la plataforma de votación de software libre con la que se realizan estas primarias. Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem.</p>"
        ),
        dict(
            name="Fundación Civio",
            url="http://civio.es",
            description="<p>Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem.</p><p>Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem.</p>"
        ),
        dict(
            name="Hackandalus",
            url="https://hackandalus.net",
            description="<p>Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem.</p><p>Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem.</p>"
        ),
    ],
    contact=dict(
        email="agora@agoravoting.com",
        twitter_username="agoravoting"
    )
)

########### flask

DEBUG = False

TESTING = False

SESSION_COOKIE_SECURE = True

USE_X_SENDFILE = False

SERVER_NAME = "localhost"

SECRET_KEY = "<change this>"

BABEL_DEFAULT_LOCALE = 'en'

########### settings

SQLALCHEMY_DATABASE_URI = ''

########### celery

BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Madrid'
CELERY_ENABLE_UTC = True

########### sms provider

SMS_PROVIDER = 'altiria'
SMS_DOMAIN_ID = 'comercial'
SMS_LOGIN = ''
SMS_PASSWORD = ''
SMS_URL = 'http://www.altiria.net/api/http'
SMS_SENDER_ID = ''

########### mail

# These are the default
#MAIL_SERVER  = "localhost"
#MAIL_PORT = 25
#MAIL_DEBUG =~ app.debug
#MAIL_USE_TLS = False
#MAIL_USE_SSL = False
#MAIL_USERNAME = None
#MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = "agora@example.com"

if os.path.isfile(os.path.join(ROOT_PATH, "custom_settings.py")):
    from custom_settings import *
else:
    logging.warn("custom_settings.py not being loaded")
