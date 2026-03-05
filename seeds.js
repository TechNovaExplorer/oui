const SEED_DEFS = [
    {
        "id": "s1",
        "name": "Pousse Simple",
        "color": "hsl(35.431792689989706, 75.98702588336151%, 49.15154488211656%)",
        "cost": 10,
        "sell": 5,
        "lifespan": 14343.587022357797,
        "drops": [
            10,
            15
        ],
        "behavior": "none",
        "exclusive": false
    },
    {
        "id": "s2",
        "name": "Herbe Dansante",
        "color": "hsl(232.94380192267187, 78.55025093282333%, 54.30565697828433%)",
        "cost": 25,
        "sell": 12,
        "lifespan": 13063.086161093026,
        "drops": [
            10,
            15
        ],
        "behavior": "dance",
        "exclusive": false
    },
    {
        "id": "s3",
        "name": "Pousse Couarde",
        "color": "hsl(194.41982796275107, 90.0771522226969%, 78.68584078771417%)",
        "cost": 63,
        "sell": 28,
        "lifespan": 13304.140242890093,
        "drops": [
            9,
            15
        ],
        "behavior": "hide",
        "exclusive": false
    },
    {
        "id": "s4",
        "name": "Liane Voyageuse",
        "color": "hsl(2.1865145988385937, 74.69511976682455%, 57.42938649047288%)",
        "cost": 156,
        "sell": 67,
        "lifespan": 10752.328301474103,
        "drops": [
            9,
            15
        ],
        "behavior": "move",
        "exclusive": false
    },
    {
        "id": "s5",
        "name": "Ronce Parasite",
        "color": "hsl(271.49687860541405, 71.43328553571887%, 58.621495850848966%)",
        "cost": 391,
        "sell": 159,
        "lifespan": 11371.736095701715,
        "drops": [
            8,
            14
        ],
        "behavior": "parasite",
        "exclusive": false
    },
    {
        "id": "s6",
        "name": "Bourgeon Attractif",
        "color": "hsl(213.71942489804783, 80.03974682058625%, 69.25251233169305%)",
        "cost": 977,
        "sell": 378,
        "lifespan": 8665.95890405386,
        "drops": [
            8,
            14
        ],
        "behavior": "magnet",
        "exclusive": false
    },
    {
        "id": "s7",
        "name": "Fleur Ombre",
        "color": "hsl(348.7600203387129, 79.18760133397865%, 52.6457829501166%)",
        "cost": 2441,
        "sell": 897,
        "lifespan": 16578.103641998918,
        "drops": [
            7,
            14
        ],
        "behavior": "shadow",
        "exclusive": false
    },
    {
        "id": "s8",
        "name": "Cristalline Piquante",
        "color": "hsl(117.64901633961222, 94.57914571583737%, 40.21450287281346%)",
        "cost": 6104,
        "sell": 2131,
        "lifespan": 11115.784741778029,
        "drops": [
            7,
            13
        ],
        "behavior": "explode",
        "exclusive": false
    },
    {
        "id": "s9",
        "name": "Orgueil Doré",
        "color": "hsl(314.53173837186523, 72.86794550300795%, 76.56259622101672%)",
        "cost": 15259,
        "sell": 5062,
        "lifespan": 14475.506533444284,
        "drops": [
            6,
            13
        ],
        "behavior": "giant_low_drop",
        "exclusive": false
    },
    {
        "id": "s10",
        "name": "Singularité",
        "color": "hsl(107.49139439316792, 82.15979649707945%, 66.59469845760039%)",
        "cost": 38147,
        "sell": 12021,
        "lifespan": 8299.168872588307,
        "drops": [
            6,
            13
        ],
        "behavior": "blackhole",
        "exclusive": false
    },
    {
        "id": "s11",
        "name": "Fleur de Feu",
        "color": "hsl(351.95772487952445, 94.6329536320815%, 48.452149004180214%)",
        "cost": 95367,
        "sell": 28550,
        "lifespan": 5847.046820251529,
        "drops": [
            5,
            13
        ],
        "behavior": "none",
        "exclusive": false
    },
    {
        "id": "s12",
        "name": "Cristal de Givre",
        "color": "hsl(68.20943505253753, 84.98052807236537%, 60.00359921378354%)",
        "cost": 238419,
        "sell": 67806,
        "lifespan": 6542.425566642979,
        "drops": [
            5,
            12
        ],
        "behavior": "dance",
        "exclusive": false
    },
    {
        "id": "s13",
        "name": "Racine Hurlante",
        "color": "hsl(262.57509306825483, 73.59064010371227%, 75.48601759652732%)",
        "cost": 596046,
        "sell": 161040,
        "lifespan": 18137.89805534794,
        "drops": [
            4,
            12
        ],
        "behavior": "hide",
        "exclusive": false
    },
    {
        "id": "s14",
        "name": "Tige de Fer",
        "color": "hsl(185.80071808968927, 81.04959688747687%, 72.85613551872993%)",
        "cost": 1490116,
        "sell": 382470,
        "lifespan": 5536.512470416854,
        "drops": [
            4,
            12
        ],
        "behavior": "move",
        "exclusive": false
    },
    {
        "id": "s15",
        "name": "Liane Électrique",
        "color": "hsl(18.061173362696934, 92.75508086882023%, 41.73241983959738%)",
        "cost": 3725290,
        "sell": 908365,
        "lifespan": 6922.464216742691,
        "drops": [
            3,
            11
        ],
        "behavior": "parasite",
        "exclusive": false
    },
    {
        "id": "s16",
        "name": "Lotus Sanguin",
        "color": "hsl(108.3325939873029, 93.52227799821833%, 50.275501095695994%)",
        "cost": 9313226,
        "sell": 2157368,
        "lifespan": 11247.025531986059,
        "drops": [
            3,
            11
        ],
        "behavior": "magnet",
        "exclusive": false
    },
    {
        "id": "s17",
        "name": "Orchidée Fantôme",
        "color": "hsl(289.26027842511996, 73.25037116091542%, 50.30446335644666%)",
        "cost": 23283064,
        "sell": 5123749,
        "lifespan": 12682.048408307503,
        "drops": [
            2,
            11
        ],
        "behavior": "shadow",
        "exclusive": false
    },
    {
        "id": "s18",
        "name": "Cactus Émeraude",
        "color": "hsl(298.8492001914809, 81.897360786608%, 66.05094953878535%)",
        "cost": 58207661,
        "sell": 12168903,
        "lifespan": 18556.35489607796,
        "drops": [
            2,
            11
        ],
        "behavior": "explode",
        "exclusive": false
    },
    {
        "id": "s19",
        "name": "Rose des Vents",
        "color": "hsl(291.38538370509855, 92.31532664065834%, 65.09034547588983%)",
        "cost": 145519152,
        "sell": 28901145,
        "lifespan": 10720.408852291832,
        "drops": [
            1,
            10
        ],
        "behavior": "giant_low_drop",
        "exclusive": false
    },
    {
        "id": "s20",
        "name": "Tulipe d'Obsidienne",
        "color": "hsl(125.03765778306733, 77.21637613424423%, 60.44558956551448%)",
        "cost": 363797881,
        "sell": 68640220,
        "lifespan": 19152.924968652787,
        "drops": [
            1,
            10
        ],
        "behavior": "blackhole",
        "exclusive": false
    },
    {
        "id": "s21",
        "name": "Graine Tempête",
        "color": "hsl(251.814268869525, 72.46324900010381%, 66.5715315212538%)",
        "cost": 909494702,
        "sell": 163020524,
        "lifespan": 13423.291785578414,
        "drops": [
            1,
            10
        ],
        "behavior": "none",
        "exclusive": false
    },
    {
        "id": "s22",
        "name": "Bourgeon Sombre",
        "color": "hsl(231.62276054376875, 71.4237313995409%, 58.85222345974302%)",
        "cost": 2273736754,
        "sell": 387173743,
        "lifespan": 6008.715147936542,
        "drops": [
            1,
            9
        ],
        "behavior": "dance",
        "exclusive": false
    },
    {
        "id": "s23",
        "name": "Lys Solaire",
        "color": "hsl(348.48665506139054, 86.7670944232915%, 56.449842779191364%)",
        "cost": 5684341886,
        "sell": 919537641,
        "lifespan": 10020.182793928707,
        "drops": [
            1,
            9
        ],
        "behavior": "hide",
        "exclusive": false
    },
    {
        "id": "s24",
        "name": "Pétale Lunaire",
        "color": "hsl(204.3473201163983, 97.98439919287038%, 74.86542047461162%)",
        "cost": 14210854715,
        "sell": 2183901896,
        "lifespan": 14669.707861563129,
        "drops": [
            1,
            9
        ],
        "behavior": "move",
        "exclusive": false
    },
    {
        "id": "s25",
        "name": "Fleur Toxique",
        "color": "hsl(221.17246215200092, 70.88332026897233%, 51.97379034820343%)",
        "cost": 35527136788,
        "sell": 5186767004,
        "lifespan": 14414.231634088726,
        "drops": [
            1,
            9
        ],
        "behavior": "parasite",
        "exclusive": false
    },
    {
        "id": "s26",
        "name": "Ronce d'Acier",
        "color": "hsl(29.383190878274554, 85.51025338583409%, 70.37512456717744%)",
        "cost": 88817841970,
        "sell": 12318571635,
        "lifespan": 19042.60634618439,
        "drops": [
            1,
            8
        ],
        "behavior": "magnet",
        "exclusive": false
    },
    {
        "id": "s27",
        "name": "Lierre Épineux",
        "color": "hsl(94.43034123993512, 86.91275562438426%, 60.74155494180603%)",
        "cost": 222044604925,
        "sell": 29256607633,
        "lifespan": 5716.20362462369,
        "drops": [
            1,
            8
        ],
        "behavior": "shadow",
        "exclusive": false
    },
    {
        "id": "s28",
        "name": "Jacinthe d'Eau",
        "color": "hsl(327.74977889458137, 82.73731185494056%, 63.04023785206971%)",
        "cost": 555111512313,
        "sell": 69484443128,
        "lifespan": 15404.486011257572,
        "drops": [
            1,
            8
        ],
        "behavior": "explode",
        "exclusive": false
    },
    {
        "id": "s29",
        "name": "Coquelicot Géant",
        "color": "hsl(298.7542661146358, 98.59927381297663%, 61.34151296540142%)",
        "cost": 1387778780781,
        "sell": 165025552428,
        "lifespan": 14111.803596201591,
        "drops": [
            1,
            7
        ],
        "behavior": "giant_low_drop",
        "exclusive": false
    },
    {
        "id": "s30",
        "name": "Iris Céleste",
        "color": "hsl(289.92395771936197, 81.38474418632958%, 65.56230568474754%)",
        "cost": 3469446951954,
        "sell": 391935687017,
        "lifespan": 12194.61212258847,
        "drops": [
            1,
            7
        ],
        "behavior": "blackhole",
        "exclusive": false
    },
    {
        "id": "s31",
        "name": "Fougère Ancienne",
        "color": "hsl(32.624450949916266, 83.32606235942822%, 71.37291279253577%)",
        "cost": 8673617379884,
        "sell": 930847256666,
        "lifespan": 15980.784907710007,
        "drops": [
            1,
            7
        ],
        "behavior": "none",
        "exclusive": false
    },
    {
        "id": "s32",
        "name": "Baobab Nain",
        "color": "hsl(227.4307174000134, 75.97252186620182%, 56.42231453845274%)",
        "cost": 21684043449710,
        "sell": 2210762234582,
        "lifespan": 18828.8880320948,
        "drops": [
            1,
            7
        ],
        "behavior": "dance",
        "exclusive": false
    },
    {
        "id": "s33",
        "name": "Graine de Météore",
        "color": "hsl(23.425832711849218, 87.52024765631735%, 46.446493499149604%)",
        "cost": 54210108624275,
        "sell": 5250560307132,
        "lifespan": 13137.625833968581,
        "drops": [
            1,
            6
        ],
        "behavior": "hide",
        "exclusive": false
    },
    {
        "id": "s34",
        "name": "Pousse de Lave",
        "color": "hsl(148.01818910853962, 97.38401307795615%, 70.86148868195757%)",
        "cost": 135525271560688,
        "sell": 12470080729440,
        "lifespan": 16174.806188318867,
        "drops": [
            1,
            6
        ],
        "behavior": "move",
        "exclusive": false
    },
    {
        "id": "s35",
        "name": "Herbe de Cristal",
        "color": "hsl(273.0711818105421, 71.93064484115189%, 45.46637506536495%)",
        "cost": 338813178901720,
        "sell": 29616441732419,
        "lifespan": 7101.283790648229,
        "drops": [
            1,
            6
        ],
        "behavior": "parasite",
        "exclusive": false
    },
    {
        "id": "s36",
        "name": "Artefact Botanique",
        "color": "hsl(86.67110980571013, 92.00154416857717%, 74.64603117919313%)",
        "cost": 847032947254300,
        "sell": 70339049114495,
        "lifespan": 18892.31302151556,
        "drops": [
            1,
            5
        ],
        "behavior": "magnet",
        "exclusive": true
    },
    {
        "id": "s37",
        "name": "Graine Stellaire",
        "color": "hsl(170.50035756902562, 80.64975312129535%, 71.00129078539203%)",
        "cost": 2117582368135751,
        "sell": 167055241646926,
        "lifespan": 9511.834654502582,
        "drops": [
            1,
            5
        ],
        "behavior": "shadow",
        "exclusive": true
    },
    {
        "id": "s38",
        "name": "Racine du Néant",
        "color": "hsl(285.7193434695829, 98.8133744701884%, 57.741061737229906%)",
        "cost": 5293955920339377,
        "sell": 396756198911450,
        "lifespan": 16099.127930764775,
        "drops": [
            1,
            5
        ],
        "behavior": "explode",
        "exclusive": true
    },
    {
        "id": "s39",
        "name": "Fleur Temporelle",
        "color": "hsl(18.01293256608309, 93.4034018323744%, 78.36929438479291%)",
        "cost": 13234889800848442,
        "sell": 942295972414694,
        "lifespan": 13215.446607647871,
        "drops": [
            1,
            5
        ],
        "behavior": "giant_low_drop",
        "exclusive": true
    },
    {
        "id": "s40",
        "name": "Lotus Noir",
        "color": "hsl(354.86322741777735, 86.21847025166635%, 72.37691747106643%)",
        "cost": 33087224502121110,
        "sell": 2237952934484897,
        "lifespan": 7061.925649551542,
        "drops": [
            1,
            4
        ],
        "behavior": "blackhole",
        "exclusive": true
    },
    {
        "id": "s41",
        "name": "Orchidée Primordiale",
        "color": "hsl(225.63657611848964, 71.59411749126535%, 71.46866985710167%)",
        "cost": 82718061255302770,
        "sell": 5315138219401630,
        "lifespan": 18327.571429798918,
        "drops": [
            1,
            4
        ],
        "behavior": "none",
        "exclusive": true
    },
    {
        "id": "s42",
        "name": "Rose de Cristal",
        "color": "hsl(332.75278082010345, 94.17249950140364%, 53.32347139012874%)",
        "cost": 206795153138256930,
        "sell": 12623453271078870,
        "lifespan": 6586.477459013974,
        "drops": [
            1,
            4
        ],
        "behavior": "dance",
        "exclusive": true
    },
    {
        "id": "s43",
        "name": "Bourgeon Divin",
        "color": "hsl(182.43350653622716, 79.93218710288042%, 57.2960697821497%)",
        "cost": 516987882845642240,
        "sell": 29980701518812310,
        "lifespan": 5783.384231719455,
        "drops": [
            1,
            3
        ],
        "behavior": "hide",
        "exclusive": true
    },
    {
        "id": "s44",
        "name": "Liane Dimensionnelle",
        "color": "hsl(15.10776377942931, 74.3807630590741%, 77.10490589314729%)",
        "cost": 1292469707114105900,
        "sell": 71204166107179256,
        "lifespan": 18371.588300264426,
        "drops": [
            1,
            3
        ],
        "behavior": "move",
        "exclusive": true
    },
    {
        "id": "s45",
        "name": "Tige Cosmos",
        "color": "hsl(219.74941844766354, 70.04609633357083%, 75.92077005219926%)",
        "cost": 3231174267785264600,
        "sell": 169109894504550720,
        "lifespan": 19761.564348102576,
        "drops": [
            1,
            3
        ],
        "behavior": "parasite",
        "exclusive": true
    },
    {
        "id": "s46",
        "name": "Fleur d'Ombre Pure",
        "color": "hsl(225.05479183253294, 93.04999097259147%, 62.16452556450633%)",
        "cost": 8077935669463161000,
        "sell": 401635999448307900,
        "lifespan": 15718.899365872208,
        "drops": [
            1,
            3
        ],
        "behavior": "magnet",
        "exclusive": true
    },
    {
        "id": "s47",
        "name": "Graine d'Éternité",
        "color": "hsl(278.56105279651314, 84.71570033698988%, 42.23056654928749%)",
        "cost": 20194839173657903000,
        "sell": 953885498689731200,
        "lifespan": 10121.529954959471,
        "drops": [
            1,
            2
        ],
        "behavior": "shadow",
        "exclusive": true
    },
    {
        "id": "s48",
        "name": "Pétale Chaos",
        "color": "hsl(231.13234477178852, 73.61809586064066%, 68.93371112056269%)",
        "cost": 50487097934144760000,
        "sell": 2265478059388112000,
        "lifespan": 11597.173526353006,
        "drops": [
            1,
            2
        ],
        "behavior": "explode",
        "exclusive": true
    },
    {
        "id": "s49",
        "name": "Lys de l'Aube",
        "color": "hsl(55.3463766226481, 94.65936730434035%, 62.73096271416982%)",
        "cost": 126217744835361900000,
        "sell": 5380510391046766000,
        "lifespan": 12374.22450539341,
        "drops": [
            1,
            2
        ],
        "behavior": "giant_low_drop",
        "exclusive": true
    },
    {
        "id": "s50",
        "name": "Singularité Absolue",
        "color": "hsl(288.2521588204936, 84.74305439177364%, 54.778089218322776%)",
        "cost": 315544362088404750000,
        "sell": 12778712178736067000,
        "lifespan": 7424.581122356092,
        "drops": [
            1,
            2
        ],
        "behavior": "blackhole",
        "exclusive": true
    }
];