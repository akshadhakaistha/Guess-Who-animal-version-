import random

animals = [

    # ================= MAMMALS =================

    {
        "name": "White Rhino",
        "emoji": "🦏",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": False,
        "region": ["Africa"],
        "habitat": ["savannah", "grassland", "shrubland", "woodland"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": True,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Near Threatened",
        "fun_facts": [
            "White rhinos are actually grey, not white. Their name probably comes from a misunderstanding of the Afrikaans or Dutch word for 'wide', referring to their broad, square lips.",
            "They communicate using several sounds, including grunts, squeaks and deep calls that can travel over long distances."
        ],
        "data_facts": [
            "The white rhino is the least threatened of the five living rhino species, but it is still affected by poaching and habitat pressures.",
            "The northern white rhino is functionally extinct: only two known individuals remain, both female.",
            "Successful conservation programmes have helped southern white rhino numbers recover dramatically from historic lows."
        ]
    },

    {
        "name": "Giant Panda",
        "emoji": "🐼",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": False,
        "region": ["Asia"],
        "habitat": ["temperate forest", "mountain forest", "bamboo forest"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Pandas have a 'pseudo-thumb' — an enlarged wrist bone that works like an extra digit and helps them grip bamboo.",
            "Although bamboo makes up most of their diet, pandas are members of the order Carnivora and still have the digestive system of a carnivorous ancestor."
        ],
        "data_facts": [
            "The giant panda was downlisted from Endangered to Vulnerable by the IUCN in 2016 after conservation efforts helped its wild population recover.",
            "Pandas remain threatened by habitat fragmentation, which can isolate groups and make it harder for them to find bamboo and mates.",
            "Most wild giant pandas live in mountain forests in central China."
        ]
    },

    {
        "name": "Bengal Tiger",
        "emoji": "🐅",
        "cLass": "mammal",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Asia"],
        "habitat": ["forest", "grassland", "savannah", "mangrove", "wetland"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Every tiger has a unique stripe pattern, rather like a fingerprint. The stripes occur on the skin as well as the fur.",
            "Tigers are unusually comfortable in water for big cats and are capable swimmers."
        ],
        "data_facts": [
            "Wild tigers now number around 5,500 globally, according to the Global Tiger Forum's 2023 estimate.",
            "India contains the world's largest wild tiger population.",
            "Tiger range has shrunk by about 95% over the last 150 years, mainly because of habitat loss and human pressure."
        ]
    },

    {
        "name": "African Elephant",
        "emoji": "🐘",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": True,
        "region": ["Africa"],
        "habitat": ["savannah", "grassland", "woodland", "forest", "wetland"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "4",
        "tusks": True,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered / Critically Endangered",
        "fun_facts": [
            "African elephants use low-frequency rumbles that can travel through the ground, allowing elephants to communicate over surprisingly long distances.",
            "An elephant's trunk contains tens of thousands of muscle units and is used for breathing, smelling, touching, drinking and manipulating objects."
        ],
        "data_facts": [
            "African elephants are now recognised as two species: the African savanna elephant and the African forest elephant.",
            "The savanna elephant is Endangered, while the forest elephant is Critically Endangered on the IUCN Red List.",
            "Poaching for ivory and habitat loss remain major threats, although some protected populations are stable or increasing."
        ]
    },

    {
        "name": "Mountain Gorilla",
        "emoji": "🦍",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": False,
        "region": ["Africa"],
        "habitat": ["mountain forest", "bamboo forest", "montane grassland"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Gorillas can be identified by the unique pattern of wrinkles on their noses, known as noseprints.",
            "Mountain gorillas live in social groups led by a dominant silverback, and groups can contain multiple adults and young."
        ],
        "data_facts": [
            "A 2018 census estimated more than 1,000 mountain gorillas in the wild, making them one of the rarest great apes.",
            "Their population has increased because of intensive conservation, veterinary care and anti-poaching work.",
            "Despite this recovery, the species remains Endangered and its range is extremely restricted."
        ]
    },

    {
        "name": "Blue Whale",
        "emoji": "🐋",
        "cLass": "mammal",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe", "North America", "Central America", "South America", "Oceania"],
        "habitat": ["open ocean", "coastal ocean"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "The blue whale is the largest animal known to have ever lived, reaching enormous sizes while feeding mainly on tiny krill.",
            "Its calls can travel huge distances through the ocean and are among the loudest sounds produced by animals."
        ],
        "data_facts": [
            "Commercial whaling caused enormous declines in blue whale populations during the twentieth century.",
            "The IUCN currently lists the blue whale as Endangered.",
            "Different populations have recovered to different degrees, so conservation status and population estimates vary between regions."
        ]
    },

    {
        "name": "Vaquita",
        "emoji": "🐬",
        "cLass": "mammal",
        "diet": "carnivore",
        "ivory": False,
        "region": ["North America"],
        "habitat": ["shallow coastal ocean", "marine waters"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Critically Endangered",
        "fun_facts": [
            "The vaquita is the world's smallest cetacean, reaching only about 1.5 metres in length.",
            "Its dark eye and lip markings have earned it the nickname 'panda of the sea'."
        ],
        "data_facts": [
            "Fewer than 10 vaquitas are estimated to remain.",
            "They live only in a small area of the northern Gulf of California in Mexico.",
            "The greatest threat is accidental entanglement in gillnets, particularly nets used illegally to catch totoaba."
        ]
    },

    {
        "name": "Aye-Aye",
        "emoji": "🐒",
        "cLass": "mammal",
        "diet": "omnivore",
        "ivory": False,
        "region": ["Africa"],
        "habitat": ["tropical rainforest", "dry forest", "mangrove forest"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "The aye-aye taps on branches with its fingers and listens for changes in sound to locate insects hiding inside wood.",
            "Its extremely long middle finger is used to extract food from tiny holes and crevices."
        ],
        "data_facts": [
            "The aye-aye is found only in Madagascar.",
            "It is the world's largest nocturnal primate.",
            "Deforestation and persecution caused by local superstitions are important threats to the species."
        ]
    },

    {
        "name": "Dugong",
        "emoji": "🧜",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": False,
        "region": ["Asia", "Oceania"],
        "habitat": ["seagrass meadow", "shallow coastal ocean", "estuary"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Dugongs are more closely related to elephants than to whales or dolphins.",
            "They feed mainly on seagrass and use their muscular lips to pull plants from the seabed."
        ],
        "data_facts": [
            "Dugongs are Vulnerable on the IUCN Red List.",
            "Their slow reproduction makes populations particularly difficult to recover after declines.",
            "Gillnets, habitat loss, boat traffic, pollution and hunting all threaten dugong populations."
        ]
    },

    {
        "name": "Manatee",
        "emoji": "🦭",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": False,
        "region": ["North America", "Central America", "South America", "Africa"],
        "habitat": ["river", "wetland", "estuary", "shallow coastal ocean"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Manatees constantly replace their molars as worn teeth move forward and eventually fall out.",
            "Their large lungs and heavy bones help them control their position in the water."
        ],
        "data_facts": [
            "Manatees are fully aquatic mammals even though early sailors sometimes mistook them for mythical sea creatures.",
            "Boat strikes are a major cause of death in several manatee populations.",
            "Habitat loss, pollution and harmful algal blooms also threaten them."
        ]
    },

    {
        "name": "Pangolin",
        "emoji": "🛡️",
        "cLass": "mammal",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia"],
        "habitat": ["tropical forest", "savannah", "grassland", "woodland", "shrubland"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": True,
        "iucn_status": "Critically Endangered / Endangered",
        "fun_facts": [
            "Pangolin scales are made from keratin — the same protein found in human fingernails and hair.",
            "Pangolins have no teeth. They catch ants and termites with an extraordinarily long, sticky tongue."
        ],
        "data_facts": [
            "All eight pangolin species are threatened with extinction to varying degrees.",
            "Pangolins are among the world's most heavily trafficked mammals.",
            "International commercial trade in pangolins was banned under CITES in 2016."
        ]
    },

    {
        "name": "Tasmanian Devil",
        "emoji": "😈",
        "cLass": "mammal",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Oceania"],
        "habitat": ["temperate forest", "woodland", "grassland", "coastal scrub"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Tasmanian devils have exceptionally powerful jaws for their size and can crush and eat bones.",
            "They are the largest surviving carnivorous marsupials."
        ],
        "data_facts": [
            "Devil Facial Tumour Disease has caused severe population declines since it was first recorded in the 1990s.",
            "The disease can spread between devils through biting.",
            "Conservation programmes are working on disease-resistant animals and establishing healthy populations."
        ]
    },

    {
        "name": "Platypus",
        "emoji": "🦦",
        "cLass": "mammal",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Oceania"],
        "habitat": ["river", "stream", "freshwater wetland", "lakeshore"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": True,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Near Threatened",
        "fun_facts": [
            "The platypus is one of only five living monotreme species — mammals that lay eggs.",
            "A platypus can detect tiny electrical signals produced by prey using receptors in its bill."
        ],
        "data_facts": [
            "Male platypuses have a venomous spur on their hind legs.",
            "Platypuses are semi-aquatic and spend much of their time hunting in rivers and streams.",
            "Water pollution, drought, habitat degradation and changes to river systems can threaten local populations."
        ]
    },

    {
        "name": "Sloth",
        "emoji": "🦥",
        "cLass": "mammal",
        "diet": "herbivore",
        "ivory": False,
        "region": ["Central America", "South America"],
        "habitat": ["tropical rainforest", "tropical dry forest", "woodland", "mangrove forest"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Species-dependent",
        "fun_facts": [
            "Sloth fur can support a tiny ecosystem of algae, fungi and specialised insects.",
            "Some sloths have extra neck vertebrae that allow them to rotate their heads much farther than most mammals."
        ],
        "data_facts": [
            "There are six living species of sloth, and their conservation statuses differ.",
            "The pygmy three-toed sloth is Critically Endangered and has a very restricted range.",
            "Habitat loss is an important threat to several sloth species."
        ]
    },

    {
        "name": "Darwin's Fox",
        "emoji": "🦊",
        "cLass": "mammal",
        "diet": "omnivore",
        "ivory": False,
        "region": ["South America"],
        "habitat": ["temperate rainforest", "woodland", "shrubland"],
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Darwin's fox is not a true fox in the genus Vulpes; it belongs to the South American canid genus Lycalopex.",
            "It is one of the world's rarest canids and has populations on Chiloé Island and mainland Chile."
        ],
        "data_facts": [
            "The species has a very small and fragmented population.",
            "Habitat loss and disease transmitted by domestic dogs are important threats.",
            "Conservation work includes protecting forest habitat and reducing contact with domestic dogs."
        ]
    },


    # ================= REPTILES =================

    {
        "name": "Hawksbill Sea Turtle",
        "emoji": "🐢",
        "cLass": "reptile",
        "diet": "omnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe", "North America", "Central America", "South America", "Oceania"],
        "habitat": ["coral reef", "shallow coastal ocean", "seagrass meadow", "mangrove"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": True,
        "iucn_status": "Critically Endangered",
        "fun_facts": [
            "The hawksbill gets its name from its narrow, hooked beak, which helps it reach food in cracks in coral reefs.",
            "It is one of the few known reptiles capable of biofluorescence."
        ],
        "data_facts": [
            "Hawksbill turtles are Critically Endangered.",
            "Historically, their shells were heavily exploited for tortoiseshell products.",
            "Protecting nesting beaches, coral reefs and reducing illegal trade are important parts of their conservation."
        ]
    },

    {
        "name": "Chameleon",
        "emoji": "🦎",
        "cLass": "reptile",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe"],
        "habitat": ["tropical forest", "dry forest", "woodland", "savannah", "shrubland", "grassland"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": True,
        "iucn_status": "Species-dependent",
        "fun_facts": [
            "A chameleon's eyes can move independently, allowing it to watch in different directions at the same time.",
            "Colour changes can communicate social information and help regulate temperature; camouflage is only one possible function."
        ],
        "data_facts": [
            "There are more than 200 recognised chameleon species, so their conservation statuses vary enormously.",
            "Madagascar contains a particularly large diversity of chameleons.",
            "Habitat loss is an important threat to many chameleon species."
        ]
    },

    {
        "name": "Komodo Dragon",
        "emoji": "🐉",
        "cLass": "reptile",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Asia"],
        "habitat": ["savannah", "woodland", "tropical forest", "coastal forest", "grassland"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": True,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Komodo dragons are the largest living lizards.",
            "Females can sometimes reproduce without a male through parthenogenesis, producing offspring from unfertilised eggs."
        ],
        "data_facts": [
            "Komodo dragons are found naturally on several Indonesian islands.",
            "They were listed as Endangered by the IUCN in 2021.",
            "Habitat change, reduced prey availability and climate change are major conservation concerns."
        ]
    },


    # ================= AMPHIBIANS =================

    {
        "name": "Axolotl",
        "emoji": "🧬",
        "cLass": "amphibian",
        "diet": "carnivore",
        "ivory": False,
        "region": ["North America"],
        "habitat": ["freshwater lake", "wetland", "freshwater canal"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Critically Endangered",
        "fun_facts": [
            "Axolotls normally keep their juvenile features, including external gills, even after reaching sexual maturity.",
            "They can regenerate limbs and parts of several organs, which is why they are heavily studied by scientists."
        ],
        "data_facts": [
            "Wild axolotls are native to the remaining wetland habitat around Lake Xochimilco in Mexico City.",
            "Their wild population has declined dramatically because of pollution, habitat loss and introduced predatory fish.",
            "Millions of axolotls exist in laboratories, but these captive animals do not represent a healthy wild population."
        ]
    },

    {
        "name": "Golden Poison Frog",
        "emoji": "🐸",
        "cLass": "amphibian",
        "diet": "carnivore",
        "ivory": False,
        "region": ["South America"],
        "habitat": ["tropical rainforest", "rainforest stream", "humid forest"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "4",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Golden poison frogs are famous for their powerful skin toxins, although captive-bred frogs often lack the same toxicity.",
            "Their bright colour is an example of aposematism: a warning signal telling predators that they are dangerous to eat."
        ],
        "data_facts": [
            "The species is native to a small region of Colombia.",
            "Habitat loss from agriculture, logging and mining threatens its rainforest habitat.",
            "Its toxin, batrachotoxin, affects sodium channels in nerve and muscle cells."
        ]
    },


    # ================= ARTHROPODS =================

    {
        "name": "Coconut Crab",
        "emoji": "🦀",
        "cLass": "arthropod",
        "diet": "omnivore",
        "ivory": False,
        "region": ["Asia", "Oceania"],
        "habitat": ["tropical forest", "coastal forest", "beach", "island woodland"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "10",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "The coconut crab is the largest land-living arthropod.",
            "Despite being related to crabs, adults are highly terrestrial and can drown if submerged for too long."
        ],
        "data_facts": [
            "Coconut crabs live on islands across parts of the Indian and Pacific Oceans.",
            "They are threatened by harvesting for food and by habitat loss.",
            "Their powerful claws allow them to open tough food, including coconuts."
        ]
    },

    {
        "name": "Monarch Butterfly",
        "emoji": "🦋",
        "cLass": "insect",
        "diet": "herbivore",
        "ivory": False,
        "region": ["North America", "Central America", "South America"],
        "habitat": ["grassland", "meadow", "woodland", "forest", "shrubland", "wetland"],
        "can_fly": True,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "6",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": True,
        "iucn_status": "Endangered",
        "fun_facts": [
            "Monarch wings are covered in tiny scales, just like those of other butterflies.",
            "Some monarch populations migrate thousands of kilometres, yet several generations are involved in completing the full annual cycle."
        ],
        "data_facts": [
            "The migratory monarch butterfly was assessed as Endangered by the IUCN in 2022.",
            "Loss of milkweed and other habitat, pesticides and climate change all affect monarch populations.",
            "The caterpillars feed mainly on milkweed, which also gives them chemical protection from many predators."
        ]
    },


    # ================= BIRDS =================

    {
        "name": "Kakapo",
        "emoji": "🦜",
        "cLass": "bird",
        "diet": "herbivore",
        "ivory": False,
        "region": ["Oceania"],
        "habitat": ["temperate forest", "shrubland", "grassland", "coastal forest"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": "2",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": False,
        "has_scales": False,
        "iucn_status": "Critically Endangered",
        "fun_facts": [
            "The kakapo is the world's heaviest parrot and is completely flightless.",
            "It is nocturnal and has a remarkably strong sense of smell compared with many other birds."
        ],
        "data_facts": [
            "Kakapo disappeared from mainland New Zealand after predators such as rats, cats and stoats were introduced.",
            "The remaining birds live on predator-free or intensively managed islands.",
            "Every surviving kakapo is individually monitored as part of an intensive conservation programme."
        ]
    },


    # ================= FISH =================

    {
        "name": "Great Hammerhead Shark",
        "emoji": "🔨",
        "cLass": "fish",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe", "North America", "Central America", "South America", "Oceania"],
        "habitat": ["coastal ocean", "coral reef", "continental shelf", "open ocean"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": True,
        "iucn_status": "Critically Endangered",
        "fun_facts": [
            "The hammer-shaped head spreads the shark's electroreceptors across a wider area, helping it detect prey.",
            "Hammerheads can use their broad heads to make tight turns while hunting.",
            "Shark skin is covered in tiny tooth-like scales called dermal denticles."
        ],
        "data_facts": [
            "The great hammerhead is Critically Endangered.",
            "It is particularly vulnerable to fishing pressure because it grows slowly and reproduces relatively late.",
            "Demand for shark fins has contributed to severe declines in many hammerhead populations."
        ]
    },

    {
        "name": "Great White Shark",
        "emoji": "🦈",
        "cLass": "fish",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe", "North America", "Central America", "South America", "Oceania"],
        "habitat": ["coastal ocean", "open ocean", "continental shelf"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": True,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Great white sharks are partially warm-bodied: special blood-vessel arrangements help keep parts of their bodies warmer than the surrounding water.",
            "Their electroreceptors can detect extremely weak electrical signals produced by living animals.",
            "Shark skin is covered in tiny tooth-like scales called dermal denticles."
        ],
        "data_facts": [
            "The great white shark is Vulnerable on the IUCN Red List.",
            "fishing pressure, including accidental capture as bycatch, is an important threat.",
            "Great whites have cartilage rather than true bone in their skeletons."
        ]
    },

    {
        "name": "Goblin Shark",
        "emoji": "👺",
        "cLass": "fish",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe", "North America", "Central America", "South America", "Oceania"],
        "habitat": ["deep ocean", "continental slope", "deep-sea floor"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": True,
        "iucn_status": "Least Concern",
        "fun_facts": [
            "The goblin shark has a spectacular protrusible jaw that can shoot forward to capture prey.",
            "Its pinkish appearance comes partly from blood vessels showing through relatively translucent skin.",
            "Shark skin is covered in tiny tooth-like scales called dermal denticles."
        ],
        "data_facts": [
            "Goblin sharks are usually found in deep water, often hundreds of metres below the surface.",
            "They belong to an ancient shark lineage that has existed for a very long time.",
            "Their deep-water lifestyle means they are encountered much less often than many coastal sharks."
        ]
    },

    {
        "name": "lemon shark",
        "emoji": "🍋",
        "cLass": "fish",
        "diet": "carnivore",
        "ivory": False,
        "region": ["Africa", "Asia", "Europe", "North America", "Central America", "South America", "Oceania"],
        "habitat": ["coastal ocean", "coral reef", "mangrove", "seagrass meadow", "estuary"],
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": "0",
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": True,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Lemon sharks get their yellowish colour from their skin, which helps them blend into sandy environments.",
            "They are among the shark species known to show social behaviour and can form groups.",
            "Shark skin is covered in tiny tooth-like scales called dermal denticles."
        ],
        "data_facts": [
            "The lemon shark is Vulnerable on the IUCN Red List.",
            "Coastal development and fishing can threaten important nursery habitats such as mangroves.",
            "Young lemon sharks often use shallow coastal areas as nurseries before moving into deeper water."
        ]
    }
]

Questions = {
   
    "cLass" : {
        "mammal": [
            "Is it a mammal?"
            ],
        "reptile": [
            "Is it a reptile?"
            ],
        "amphibian": [
            "Is it an amphibian?"
            ],
        "arthropod": [
            "Is it an arthropod?"
            ],
        "insect": [
            "Is it an insect?"
            ],
        "bird": [
            "Is it a bird?"
            ],
        "fish": [
            "Is it a fish?"
            ]
    },
    

    
    "diet" : {
           
        "herbivore": [
            "Does your animal eat only plants?",
            "Is your animal a herbivore?"
            ],
        "carnivore": [
            "Is it a meat eater?",
            "Is your animal a carnivore?"
            ],
        "omnivore": [
            "Does it eat both plants and animals?",
            "Is your animal an omnivore?"
            ]
    },

    "has_fur" : {
        "Tracker" : [
            "Does your animal have fur?",
            "Does it have fur?",
            "Is it furry?"
        ]
    },

    "lays_eggs" : {
        "Tracker": [
            "Does it lay eggs?",
            "Is it egg-laying?"
        ]
    },

    "ivory" : {
        "Tracker": [
            "Does it have ivory?",
            "Is it associated with ivory?",
            "Is it hunted for ivory?"
        ]
    },

    "region" : {
        "Africa": [
                "Does it live in Africa?"
            ],
        "Asia": [
                "Does it live in Asia?"
            ],
        "Europe": [
                "Does it live in Europe?"
            ],
        "North America": [
                "Does it live in North America?"
            ],
        "Central America": [
                "Does it live in Central America?"
            ],
        "South America": [
                "Does it live in South America?"
            ],
        "Oceania": [
                "Does it live in Oceania?"
            ]
    },

    "habitat" : {
        "savannah": [
                "Does your animal live in savannah?"
            ],
        "grassland": [
                "Does your animal live in grasslands?",
                "Is your animal found in grassy open habitats?"
            ],
        "shrubland": [
                "Does your animal live in shrubland?",
                "Is your animal found in areas dominated by shrubs?"
            ],
        "wetland": [
                "Does your animal live in wetlands?",
                "Is your animal associated with wetland habitats?"
            ],
        "temperate forest": [
                "Does your animal live in temperate forests?",
                "Is your animal found in forests with a temperate climate?"
            ],
        "mountain forest": [
                "Does your animal live in mountain forests?",
                "Is your animal found in forests at high elevations?"
            ],
        "bamboo forest": [
                "Does your animal live in bamboo forests?"
            ],
        "tropical forest": [
                "Does your animal live in tropical forests?",
                "Is your animal found in warm tropical forests?"
            ],
        "tropical rainforest": [
                "Does your animal live in tropical rainforests?",
                "Is your animal found in rainforest?"
            ],
        "tropical dry forest": [
                "Does your animal live in tropical dry forests?"
            ],
        "dry forest": [
                "Does your animal live in dry forests?"
            ],
        "woodland": [
                "Does your animal live in woodland?",
                "Is your animal found where trees are more widely spaced than in a dense forest?"
            ],
        "forest": [
                "Does your animal live in forests?"
            ],
        "mangrove": [
                "Does your animal live in mangrove habitats?",
                "Is your animal associated with mangrove forests?"
            ],
        "mangrove forest": [
                "Does your animal live in mangrove forests?"
            ],
        "open ocean": [
                "Does your animal live in the open ocean?",
                "Can your animal be found far offshore?"
            ],
        "coastal ocean": [
                "Does your animal live in coastal ocean waters?",
                "Is your animal found close to the coast?"
            ],
        "shallow coastal ocean": [
                "Does your animal live in shallow coastal ocean?"
            ],
        "marine waters": [
                "Does your animal live in marine waters?"
            ],
        "seagrass meadow": [
                "Does your animal live in seagrass meadows?",
                "Is your animal associated with underwater seagrass beds?"
            ],
        "coral reef": [
                "Does your animal live around coral reefs?",
                "Is your animal associated with coral reef ecosystems?"
            ],
        "river": [
                "Does your animal live in rivers?",
                "Is your animal found in flowing freshwater?"
            ],
        "stream": [
                "Does your animal live in streams?"
            ],
        "freshwater stream": [
                "Does your animal live in freshwater streams?",
                "Is your animal found in small flowing freshwater habitats?"
            ],
        "rainforest stream": [
                "Does your animal live near rainforest streams?"
            ],
        "freshwater wetland": [
                "Does your animal live in freshwater wetlands?",
                "Is your animal associated with freshwater wetlands?"
            ],
        "freshwater lake": [
                "Does your animal live in freshwater lakes?"
            ],
        "freshwater canal": [
                "Does your animal live in freshwater canals?"
            ],
        "lakeshore": [
                "Does your animal live around lakeshores?"
            ],
        "estuary": [
                "Does your animal live in estuaries?"
            ],
        "deep ocean": [
                "Does your animal live in the deep ocean?",
                "Is your animal found hundreds of metres below the surface?"
            ],
        "continental shelf": [
                "Does your animal live around continental shelves?"
            ],
        "continental slope": [
                "Does your animal live around continental slopes?"
            ],
        "deep-sea floor": [
                "Does your animal live on the deep-sea floor?"
            ],
        "island": [
                "Does your animal live on islands?",
                "Is your animal naturally restricted to island habitats?"
            ],
        "island woodland": [
                "Does your animal live in island woodland?"
            ],
        "coastal forest": [
                "Does your animal live in coastal forests?",
                "Is your animal found in forests near the sea?"
            ],
        "coastal scrub": [
                "Does your animal live in coastal scrub?"
            ],
        "beach": [
                "Does your animal live around beaches?"
            ],
        "meadow": [
                "Does your animal live in meadows?",
                "Is your animal found in open areas with grasses and flowering plants?"
            ],
        "humid forest": [
                "Does your animal live in humid forests?"
            ],
        "montane grassland": [
                "Does your animal live in montane grasslands?"
            ]
    },

   "can_fly" : {
        "Tracker": [
            "Can it fly?",
            "Is your animal airborne?"
        ]
    },

    "legs" : {
        "0": [
                "Is your animal legless?",
                "Does your animal have no legs?"
            ],
        "2": [
                "Does your animal have 2 legs?",
                "Is your animal two-legged?"
            ],
        "4": [
                "Does your animal have 4 legs?",
                "Is your animal four-legged?"
            ],
        "6": [
                "Does your animal have 6 legs?",
                "Is your animal six-legged?"
            ],
        "10": [
                "Does your animal have 10 legs?",
                "Is your animal ten-legged?"
            ]
    },
    
    "tusks" : {
        "Tracker": [
            "Does it have tusks?",
            "Is it associated with tusks?"
        ]
    },

    "has_horn" : {
        "Tracker": [
            "Does your animal have a horn on its nose?",
            "Does your animal have a horn?"
        ]
    },

    "is_aquatic" : {
        "Tracker": [
            "Does your animal live in water?",
            "Is your animal aquatic?"
        ]
    },

    "has_scales" : {
        "Tracker": [
            "Does your animal have scales?",
            "Is your animal scaly?"
        ]
    }
}


computerAnimal = random.choice(animals)
print(computerAnimal["name"])

playerAnimal = random.choice(animals)

print(f"Your animal is {playerAnimal['name']}. Are you happy with this animal?")

choice = input().lower()

while choice != "yes":

    while choice != "yes" and choice != "no":
        print("Please enter either yes or no")
        choice = input().lower()

    if choice == "no":
        playerAnimal = random.choice(animals)

        print(
            f"Your animal is {playerAnimal['name']}. "
            "Are you happy with this now?"
        )

        choice = input().lower()

print(
    "Great! The computer has been assigned its animal, too. "
)

print("You both have one of these animals:")
print()

count = 0

for animal in animals:
    print(f"{animal['emoji']} {animal['name']:<20}",end="     ")
    count = count + 1
    if count == 4:
     print(
     )
     count = 0

print()
print()
print("Let's start! The computer will ask you a question, "
    "please reply with 'yes', 'no', 'it depends', or "
    "'I don't know' if you really don't know "
    "(idk is also acceptable). You can then ask a question of your own.")

Bank = {
     "cLass" : {
       "Tracker":"unknown",
       "mammal": "unknown",
       "reptile": "unknown",
       "amphibian": "unknown",
       "arthropod": "unknown",
       "insect": "unknown",
       "bird": "unknown",
       "fish": "unknown"},
       
     "diet" : {
       "Tracker":"unknown",
       "herbivore": "unknown",
       "carnivore": "unknown",
       "omnivore": "unknown"},

     "ivory" : {"Tracker":"unknown"},

     "region" : {
       "Tracker":"unknown",
       "Africa": "unknown",
       "Asia": "unknown",
       "Europe": "unknown",
       "North America": "unknown",
       "Central America": "unknown",
       "South America": "unknown",
       "Oceania": "unknown"},

     "habitat" : {
       "Tracker":"unknown",
       "grassland": "unknown",
       "savannah": "unknown",
       "shrubland": "unknown",
       "wetland": "unknown",
       "temperate forest": "unknown",
       "mountain forest": "unknown",
       "tropical forest": "unknown",
       "tropical rainforest": "unknown",
       "woodland": "unknown",
       "mangrove": "unknown",
       "open ocean": "unknown",
       "coastal ocean": "unknown",
       "seagrass meadow": "unknown",
       "coral reef": "unknown",
       "river": "unknown",
       "freshwater wetland": "unknown",
       "lake": "unknown",
       "freshwater stream": "unknown",
       "deep ocean": "unknown",
       "island": "unknown",
       "coastal forest": "unknown",
       "meadow": "unknown"},

     "can_fly" : {"Tracker":"unknown"},

     "has_fur" : {"Tracker":"unknown"},

     "lays_eggs" : {"Tracker":"unknown"},

     "legs" : {
       "Tracker":"unknown",
       "0": "unknown",
       "2": "unknown",
       "4": "unknown",
       "6": "unknown",
       "10": "unknown"},

     "tusks" : {"Tracker":"unknown"},

     "has_horn" : {"Tracker":"unknown"},

     "is_aquatic" : {"Tracker":"unknown"},

     "has_scales" : {"Tracker":"unknown"},

 }

def askQ(Bank):
     options = []
     for attribute, values in Bank.items():
        if attribute in ["cLass", "diet", "legs", "habitat", "region"]:
            if values["Tracker"] == "unknown":
                for value, status in values.items():
                    if value != "Tracker" and status == "unknown":
                        options.append((attribute, value))
        else:
            if values["Tracker"] == "unknown":
                options.append((attribute, "Tracker"))
     attribute, value = random.choice(options)
     question = random.choice(Questions[attribute][value])
     return question, attribute, value

def processAnswer(question):

    print(question)
    answer = input().lower()

    while answer not in ["idk", "i don't know", "depends", "yes", "no"]:
        print("Please enter one of the following: 'yes', 'no', 'depends' or 'idk'/'I don't know'")
        answer = input().lower()

    if answer in ["yes","depends"]:
        return True

    elif answer == "no":
        return False

    else:
        return "unknown"

def updateBank(Bank,attribute, value, ans):
    Bank[attribute][value] = ans
    if Bank[attribute] in ["cLass","diet","legs"]:
        if ans == True:
          Bank[attribute]["Tracker"] = "Known"
    return Bank

def PlayerQ():

    print("Your turn - ask a question! Please enusure it is about of the following:")
    print("1. What class is it?")
    print("2. What does it eat?")
    print("3. Does it have ivory?")
    print("4. What region does it live in?")
    print("5. What habitat does it live in?")
    print("6. How many legs does it have?")
    print("7. Can it fly?")
    print("8. Does it have fur?")
    print("9. Does it lay eggs?")
    print("10. Does it have tusks?")
    print("11. Does it have a horn?")
    print("12. Is it aquatic?")
    print("13. Does it have scales?")
    print("14. Guessing an animal.")
    print()
    print("Which would you like to ask about? Please enter a number.")
    choice = int(input())
    while type(choice) == str() and choice > 14 or choice < 1:
        print("Please enter a number 1 to 14")
        choice = int(input())
    if choice == 1:
        attribute = "cLass"
    elif choice == 2:
        attribute = "diet"
    elif choice == 3:
        attribute = "ivory"
    elif choice == 4:
        attribute = "region"
    elif choice == 5:
        attribute = "habitat"
    elif choice == 6:
        attribute = "legs"
    elif choice == 7:
        attribute = "can_fly"
    elif choice == 8:
        attribute = "has_fur"
    elif choice == 9:
        attribute = "lays_eggs"
    elif choice == 10:
        attribute = "tusks"
    elif choice == 11:
        attribute = "has_horn"
    elif choice == 12:
        attribute = "is_aquatic"
    elif choice == 13:
        attribute = "has_scales"
    elif choice == 14:
        attribute = "name"

    print("Please ask your question now. This should be a yes/no question, not open-ended, and the computer will only answer in yes or no.")
    question = input().lower()
    words = question.split()
    print(words)
    processed = False
    negative = False
    for word in words:
       while word in ["what","why","how"]:
         print("Please ensure your question is not open-ended.")
         question = input().lower()
         words = question.split()
         print(words)
       if word in ["not","unable","no","none","doesnt","isn't"] and attribute != "legs":
           negative = True
    for word in words:
        if attribute in ["cLass","diet","legs","name"]:
          if word == computerAnimal[attribute].lower():
             print("Yes")
             processed = True
          if attribute == "diet":
                if word in ["meat"] and word in ["plants"]:
                     if computerAnimal[attribute].lower() == "omnivore":
                       processed = True
                elif word in ["meat"]:
                     if computerAnimal[attribute].lower() == "carnivore":
                       processed = True
                elif word in ["plant"]:
                    if computerAnimal[attribute].lower() == "herbivore":
                       processed = True
        elif word == computerAnimal[attribute]:
            processed = True
        if attribute == "can_fly":
          if word in ["fly","flight","airborne"]:
              if computerAnimal[attribute] == True:
                processed = True
        if attribute == "has_fur":
          if word in ["fur","hair","furry","hairy","soft","fluffy"]:
            if computerAnimal[attribute] == True:
                processed = True
        if attribute == "lays_eggs":
           if word in ["egg","eggs","egg-laying"]:
              if computerAnimal[attribute] == True:
                processed = True
        if attribute == "has_horn":
          if word in ["horn","horned"]:
            if computerAnimal[attribute] == True:
                processed = True
        if attribute == "has_scales":
          if word in ["scale","scales","scaled","scaly"]:
            if computerAnimal[attribute] == True:
                processed = True
        if attribute == "is_aquatic":
          if word in ["water","ocean","sea","lake","aquatic","underwater"]:
            if computerAnimal[attribute] == True:
                processed = True
        if attribute == "legs":
            if computerAnimal[attribute] == "0":
                if word in ["none","no","zero","legless","not"]:
                    processed = True
            if computerAnimal[attribute] == "2":
                 if word in ["two","two-legged"]:
                    processed = True
            if computerAnimal[attribute] == "4":
                 if word in ["four","four-legged",]:
                    processed = True   
            if computerAnimal[attribute] == "6":
                 if word in ["six","six-legged"]:
                    processed = True   
            if computerAnimal[attribute] == "10":
                 if word in ["ten","ten-legged",]:
                    processed = True   
    if attribute == "name":
        if computerAnimal[attribute] == "White Rhino":
         if "white" and "rhino" in words:
            processed = True
    if computerAnimal[attribute] == "Mountain Gorilla":
        if "mountain" and "gorilla" in words:
            processed = True
    if computerAnimal[attribute] == "Coconut Crab":
        if "coconut" and "crab" in words:
            processed = True
    if computerAnimal[attribute] == "Great White Shark":
        if "great" and "white" in words:
            processed = True
    if computerAnimal[attribute] == "Giant Panda":
        if "giant" and "panda" in words:
            processed = True
    if computerAnimal[attribute] == "Blue Whale":
        if "blue" and "whale" in words:
            processed = True
    if computerAnimal[attribute] == "Komodo Dragon":
        if "komodo" and "dragon" in words:
            processed = True
    if computerAnimal[attribute] == "Monarch Butterfly":
        if "monarch" and "butterfly" in words:
            processed = True
    if computerAnimal[attribute] == "Goblin Shark":
        if "goblin" and "shark" in words:
            processed = True
    if computerAnimal[attribute] == "Bengal Tiger":
        if "bengal" and "tiger" in words:
            processed = True
    if computerAnimal[attribute] == "Darwin's Fox":
        if "darwin's" and "fox" in words:
            processed = True
        elif "darwin's" and "fox" in words:
            processed = True
    if computerAnimal[attribute] == "lemon shark":
        if "lemon" and "shark" in words:
            processed = True
    if computerAnimal[attribute] == "African Elephant":
        if "african" and "elephant" in words:
            processed = True
    if computerAnimal[attribute] == "Tasmian Devil":
        if "tasmanian" and "devil" in words:
            processed = True
    if computerAnimal[attribute] == "Aye-Aye":
        if "aye" and "aye" in words:
            processed = True
    if computerAnimal[attribute] == "Hawksbill Sea Turtle":
        if "sea" and "turtle" in words:
            processed = True
        elif "hawksbill" and "turtle" in words:
            processed = True
    if computerAnimal[attribute] == "Golden Poison Frog":
        if "poison" and "frog" in words:
            processed = True
    if computerAnimal[attribute] == "Great Hammerhead Shark":
        if "hammerhead" in words:
            processed = True

    if processed == False and negative == False:
           print("no")
    elif processed == True and negative == False:
           print("Yes")
           if attribute == "name":
               lose(computerAnimal)
    elif processed == False and negative == True:
           print("Yes")
           if attribute == "name":
                lose(computerAnimal)
    else:
        print("no")

def lose(computerAnimal):
       print("Well done!! You win!!!")
       print(f"My animal was {computerAnimal['name']} {computerAnimal['emoji']}") 
       print(f"Some stats about my animal:")
       print(computerAnimal["cLass"])
       print(computerAnimal["diet"])
       print(computerAnimal["ivory"])
       print(computerAnimal["region"])
       print(computerAnimal["habitat"])
       print(computerAnimal["iucn_status"])
       print("And here are some funfacts:")
       print(computerAnimal["fun_facts"])
       print("And here's some more about it:")
       print(computerAnimal["data_facts"])
       return True
    
def gameplay(Bank):
     question, attribute, value = askQ(Bank)
     ans = processAnswer(question)
     Bank = updateBank(Bank,attribute, value, ans)
     PlayerQ()

def win(computerAnimal,playerAnimal):
   print("Yay!! I win!!!")
   print(f"My animal was {computerAnimal['name']} {computerAnimal['emoji']}") 
   print(f"Some stats about my animal:")
   print(computerAnimal["cLass"])
   print(computerAnimal["diet"])
   print(computerAnimal["ivory"])
   print(computerAnimal["region"])
   print(computerAnimal["habitat"])
   print(computerAnimal["iucn_status"])
   print("And here are some funfacts:")
   print(computerAnimal["fun_facts"])
   print("And here's some more about it:")
   print(computerAnimal["data_facts"])
   return True

def guess(Bank, animals, notAnimal):
  notAnimal = notAnimal
  
  possibleAnimal = []
  info = {}
  for attribute, value in Bank.items():
        if value["Tracker"] == "Known":
           for values, data in value.items():
            if values!= "Tracker" and data == True: 
             info[attribute] = values
  for attribute,value in info.items():
        for animal in animals:
           if info[attribute] != animal[attribute]:
               notAnimal.append(animal["name"])

  for animal in animals: 
    possible = True
    for item in notAnimal:
        if animal["name"] == item:
             possible = False
    if possible == True:
        possibleAnimal.append(animal)
  
  guessValue = random.choice(possibleAnimal)
  print(f"Is your animal {guessValue['name']}?")
  ans = input().lower()
  while ans != "yes" and ans != "no":
      print("Please enter one of yes or no.")
      ans = input().lower()
  if ans == "yes":
      win(computerAnimal,playerAnimal)
  else:
      notAnimal.append(guessValue["name"]) 
  return notAnimal

found = False
loop = 0
list = [] 

while found != True: 
   gameplay(Bank)
   loop = loop + 1 
   if loop >= 2 and loop <= 5:
     nextMove = random.choice([1,2,3,4,5])
     if nextMove == 1:
       notAnimal = guess(Bank, animals,list)
       list = notAnimal
     else:
       gameplay(Bank)
   elif loop >= 6 and loop <= 10:
         nextMove = random.choice([1,2,3,4,5])
         if nextMove in [1,2]:
           guess(Bank, animals,list)
           list = notAnimal
         else:
           gameplay(Bank)
   elif loop >= 11:
          nextMove = random.choice([1,2])
          if nextMove == 1:
            guess(Bank,animals,list)
            list = notAnimal
          else:
            gameplay(Bank)
   
    
    
     

             

       




 
 




    
    