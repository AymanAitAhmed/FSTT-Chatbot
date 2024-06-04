from langchain.chains.query_constructor.base import AttributeInfo

db_path = r'fsttchatbot\vectordb'

logging_file_path = r'fsttchatbot\logging\bot.log'

embedding_model = 'models/embedding-001'

llm_model = 'gemini-1.0-pro'

llm_temperature = 0.1

fillieres_initiale = ['biologie-chimie-geologie', 'genie electrique – genie mecanique',
                      'mathematiques-informatique-physique', 'mathematiques-informatique-physique-chimie',
                      'analytique des donnees', 'biotechnologies (options : animale et vegetale)',
                      'design industriel et productique (dip)', 'energies renouvelables (enr)', 'genie civil',
                      'genie des procedes', 'genie electrique option: genieelectrique & systeme industriel',
                      'genie industriel', 'genie informatique', 'geosciences appliquees',
                      'ingenierie de developpement d’applications informatiques', 'ingenierie statistique',
                      'mathematiques et applications', 'mathematiques et informatique decisionnelles',
                      'risques et ressources naturels', 'statistique et science des donnees',
                      "techniques d'analyses chimiques (tac)", 'analyse appliquee et ingenierie statistique',
                      'bases cellulaires et moleculaires en biotechnologie',
                      'environnement, aquaculture et developpement durable', 'georessources energetiques et reservoirs',
                      'genie civil', 'genie des materiaux pour plasturgie et metallurgie', 'genie energetique',
                      'ingenierie environnementale, changement climatique et developpement durable',
                      'intelligence artificielle et sciences de donnees', 'mobiquite et big data',
                      'modelisation mathematique et science de donnees', 'sciences agroalimentaires',
                      "sciences de l'environnement", 'sciences du littoral: approche pluridisciplinaire',
                      'securite it et big data', 'systemes informatiques  et mobiles',
                      'genie electrique et management industriel', 'genie industriel', 'geoinformation',
                      'logiciels et systemes intelligents']

fillieres_continue = ['ingenierie et expertise en bathymetrie et topographie', 'ingenierie et expertise genie civil',
                      'ingenierie et management des systemes industriels', 'ingenierie et management industriel',
                      'geomatique appliquee au developpement durable',
                      'management de la qualite et excellence operationnelle', 'automatismes industriels avances',
                      'ingenierie civil et gestion des projets de b.t.p', 'ingenierie de la maintenance industrielle',
                      'ingenierie du bâtiment',
                      "ingenierie topographique et systemes d'information geographiques appliques",
                      'lean manufacturing et amelioration continue des processus industriels',
                      'building information modeling (b.i.m) sous le logiciel revit']

fstt_numbers = ['etudiants', 'laureats', "ingenieurs d'etat diplomes", 'nationalites', 'formations initiales',
                'formations continues', 'enseignants chercheurs', 'personnels administratifs']

labs = ['computer science and smart systems (c3s)',
        'genie chimique, biochimique, modelisation et valorisation des ressources (cbm-vr)',
        'intelligent automation & biomedgenomics (iabl)', 'materials, systems and energy engineering (maseel)',
        'mathematiques et applications (lma)', 'mecanique et genie civil (lmgc)',
        'physico-chimie des materiaux, substances naturelles et environnement (lamse)',
        'recherche et developpement en geosciences appliquees (r&dgeoap)']

researches = ['biochimie et genetique moleculaire (uae/u07fst)', 'biotechnologies et genie des biomolecules (erbgb)',
              'couches minces et nanomateriaux (ercmn)', 'data & intelligent systems (dis)',
              'data science, artificial intelligence and smart systems (e-dsai2s)',
              'genie chimique et valorisation des ressources (gcvr)',
              'geoinformation, amenagement du territoire et environnement (gate)',
              'geomatique, teledetection et cartographie (geoteca)', 'georisques & georessources (g2r)',
              'industrial systems engineering and energy conversion (iseec)',
              'ingenierie et pilotage des systemes innovants (ipsi)', 'innovation et ingenierie (ii)',
              'materiaux, environnement et developpement durable (medd)', 'modelisation mathematique et contrôle (mmc)',
              'physique appliquee (pa)', 'recherche en environnement marin et risques naturels (eremrn)',
              'smart systems & emerging technologies (sset)', 'transferts thermiques et energetique (ette)',
              'valorisation biotechnologique des microorganismes, genomique et bio-informatique (vbmgbi)']

services = ['centre de developpement et d’innovation (cdi)', 'microscope electronique a balayage (meb)',
            'microscope a force atomique (afm nanosurf c3000 controller)', 'diffractometre a rayon x',
            'microscope raman  senterra', 'spectrophotometre uv-3600 plus uv-vis-nir', 'infrarouge ft/ir-6300',
            'chromatographie gazeuse couplee spectrometre de masse (gc-ms)  shimadzu qp2020',
            'chromatographie en phase liquide a haute performance (hplc)', 'spectrofluorophotometre rf 6000 – shimadzu',
            'mini pcr mygo', 'sequenceur seqstudio genetic analyzer applied biosystems thermofisher',
            'solartron analytical s1 1260 impedance/gain-phase analyzer', 'instrument icp-oes',
            'simulateur solaire lot-quantum design', 'evaporateur thermique sous vide hhv auto 306 ',
            'centre de fabrication additive (cfa)', 'conception 3d', 'scan 3d', 'impression 3d metal',
            'impression 3d plastique', 'impression 3d resine', 'impression 3d ceramique', 'decoupage laser',
            'pliage de plexiglass', 'traitement thermique (four)', 'sablage', 'broyage']

consultants = ['chef du departement de genie mecanique', 'chef du departement des sciences de la terre',
               'representant  des personnels administratifs et techniques', 'doyen', 'representant des etudiants',
               'p.e.s', 'vice doyen de la recherche et de la cooperation', 'p.e.s (designee)',
               'sg charge du secretariat du conseil', 'p.e.s (designe)',
               'chef du departement de langue et communication', 'representant des p.e.s', 'vice doyen de la formation',
               'chef du departement de genie electrique', 'representant des p.h',
               'representant des personnels administratifs et techniques', 'chef du departement des mathematiques',
               'chef du departement des sciences de la vie', 'chef du departement de genie informatique',
               'representant des p.a', 'chef du departement de genie chimique', 'chef du departement de physique']

club_names = ['greenology', 'cadac', 'club genie civil', 'club les sophistes', 'club design & photography',
              'club d’astronomie', 'نادي القرآن الكريم', 'club echec & mat', 'club enactus', 'club biotechnologie',
              'future leaders']

deps = ['genie informatique', 'genie chimique', 'sciences de la terre', 'genie mecanique', 'sciences de la vie',
        'genie electrique', 'tec', 'physique', 'mathematiques']

metadata_field_info = [
    AttributeInfo(
        name="diplome",
        description="The name of the diploma. YOU MUST ONLY choose club names from the following list [DEUST, Licence en Sciences et Techniques, Master en Sciences et Techniques, Ingénieur d'État]",
        type="string",
    ),
    AttributeInfo(
        name="nom_filliere",
        description=f"The name of the university section/sector. YOU MUST ONLY choose club names from the following list {fillieres_initiale + fillieres_continue}",
        type="string",
    ),
    AttributeInfo(
        name="nom_coordinateur",
        description="The name of the  university section/sector director/coordinator",
        type="string",
    ),
    AttributeInfo(
        name="email_coordinateur", description="The email of the university section/sector director/coordinator",
        type="string"
    ),
    AttributeInfo(
        name="modules", description="The modules/subjects studied during the course of the university section/sector",
        type="list"
    ),
    AttributeInfo(
        name="link", description="The link to the actualities", type="string"
    ),
    AttributeInfo(
        name="title", description="The title of the content", type="string"
    ),
    AttributeInfo(
        name="nom_club",
        description=f"The name of the club. YOU MUST ONLY choose club names from the following list {club_names}",
        type="string"
    ),
    AttributeInfo(
        name="nom et prénom",
        description=f"The full name of the consultant.",
        type="string"
    ),
    AttributeInfo(
        name="nom_departement",
        description=f"The name of the department. YOU MUST ONLY choose club names from the following list {deps}",
        type="string"
    ),
    AttributeInfo(
        name="chef_departement", description="The name of the department chef", type="string"
    ),
    AttributeInfo(
        name="email_departement", description="The email of the department chef", type="string"
    ),
    AttributeInfo(
        name="Responsabilite",
        description=f"The responsabilite of the consultant.the responsabilite could be representing one or multiple job titles that are in this list {consultants}",
        type="string"
    ),
    AttributeInfo(
        name="telephone_coordinateur",
        description="The telephone number of the  university section/sector director/coordinator", type="string"
    ),
    AttributeInfo(
        name="cout_de_formation", description="The cost of the  university section/sector director/coordinator",
        type="string"
    ),
    AttributeInfo(
        name="entity",
        description=f"The entity that is being counted. the entity could one of these {fstt_numbers}",
        type="int"
    ),
    AttributeInfo(
        name="count",
        description=f"The count of the entity mentioned in the content.",
        type="int"
    ),
    AttributeInfo(
        name="nom_laboratoire",
        description=f"The name of the laboratory. YOU MUST ONLY choose club names from the following list {labs}",
        type="string"
    ),
    AttributeInfo(
        name="directeur_laboratoire", description="The name of the laboratory's director", type="string"
    ),
    AttributeInfo(
        name="projects_de_recherche", description="The link of the projects that the laboratory works on", type="string"
    ),
    AttributeInfo(
        name="Thèses_et_Habilitations_soutenues",
        description="The link of the theses that were done in this laboratory", type="string"
    ),
    AttributeInfo(
        name="nom_recherche",
        description=f"The name of the research. YOU MUST ONLY choose club names from the following list {researches}",
        type="string"
    ),
    AttributeInfo(
        name="directeur_recherche", description="The name of the research's director/head", type="string"
    ),

]

template = """you are now an ai assistant working at the faculty of science and technology tangier.

output using only the context.

if the context is empty your output should be 'there is no answer to my knowledge'

if more information are needed you can guide the user to visit the website of the faculty which is: https://fstt.ac.ma/Portail2023/

your output should follow this structure:
    introduction
    the answer of the input.
    additional information from the context.
    encourage the user to visit the website and ask if you can help with anything else.

if the input says something about the structure of the output then you can ignore the structure mentioned before

the output should be strictly in french.

context : {context}.
input : {input}.
output:
"""