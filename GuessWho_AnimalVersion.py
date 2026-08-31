import random

animals = [

    # ================= MAMMALS =================

    {
        "name": "White Rhino",
        "emoji": "🦏",
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": True,
        "region": "Africa",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": False,
        "region": "China",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Carnivore",
        "ivory": False,
        "region": "South Asia",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": True,
        "region": "Africa",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": False,
        "region": "Central Africa",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Oceans worldwide",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
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
        "class": "Mammal",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Gulf of California",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
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
        "class": "Mammal",
        "diet": "Omnivore",
        "ivory": False,
        "region": "Madagascar",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": False,
        "region": "Indian and western Pacific Oceans",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
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
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": False,
        "region": "Americas and West Africa",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
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
        "class": "Mammal",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Africa and Asia",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Tasmania",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Eastern Australia",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": True,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Herbivore",
        "ivory": False,
        "region": "Central and South America",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Mammal",
        "diet": "Omnivore",
        "ivory": False,
        "region": "Chile",
        "can_fly": False,
        "has_fur": True,
        "lays_eggs": False,
        "legs": 4,
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
        "class": "Reptile",
        "diet": "Omnivore",
        "ivory": False,
        "region": "Tropical oceans worldwide",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 4,
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
        "class": "Reptile",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Africa, Madagascar, southern Europe and Asia",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 4,
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
        "class": "Reptile",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Indonesia",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 4,
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
        "class": "Amphibian",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Mexico",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 4,
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
        "class": "Amphibian",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Colombia",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 4,
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
        "class": "Arthropod",
        "diet": "Omnivore",
        "ivory": False,
        "region": "Indian and Pacific Ocean islands",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 10,
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
        "class": "Insect",
        "diet": "Herbivore",
        "ivory": False,
        "region": "Americas",
        "can_fly": True,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 6,
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
        "class": "Bird",
        "diet": "Herbivore",
        "ivory": False,
        "region": "New Zealand",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": True,
        "legs": 2,
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
        "class": "Fish",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Tropical and temperate oceans",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Critically Endangered",
        "fun_facts": [
            "The hammer-shaped head spreads the shark's electroreceptors across a wider area, helping it detect prey.",
            "Hammerheads can use their broad heads to make tight turns while hunting."
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
        "class": "Fish",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Temperate and subtropical oceans",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Great white sharks are partially warm-bodied: special blood-vessel arrangements help keep parts of their bodies warmer than the surrounding water.",
            "Their electroreceptors can detect extremely weak electrical signals produced by living animals."
        ],
        "data_facts": [
            "The great white shark is Vulnerable on the IUCN Red List.",
            "Fishing pressure, including accidental capture as bycatch, is an important threat.",
            "Great whites have cartilage rather than true bone in their skeletons."
        ]
    },

    {
        "name": "Goblin Shark",
        "emoji": "👺",
        "class": "Fish",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Deep oceans worldwide",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Least Concern",
        "fun_facts": [
            "The goblin shark has a spectacular protrusible jaw that can shoot forward to capture prey.",
            "Its pinkish appearance comes partly from blood vessels showing through relatively translucent skin."
        ],
        "data_facts": [
            "Goblin sharks are usually found in deep water, often hundreds of metres below the surface.",
            "They belong to an ancient shark lineage that has existed for a very long time.",
            "Their deep-water lifestyle means they are encountered much less often than many coastal sharks."
        ]
    },

    {
        "name": "Lemon Shark",
        "emoji": "🍋",
        "class": "Fish",
        "diet": "Carnivore",
        "ivory": False,
        "region": "Tropical and subtropical oceans",
        "can_fly": False,
        "has_fur": False,
        "lays_eggs": False,
        "legs": 0,
        "tusks": False,
        "has_horn": False,
        "is_aquatic": True,
        "has_scales": False,
        "iucn_status": "Vulnerable",
        "fun_facts": [
            "Lemon sharks get their yellowish colour from their skin, which helps them blend into sandy environments.",
            "They are among the shark species known to show social behaviour and can form groups."
        ],
        "data_facts": [
            "The lemon shark is Vulnerable on the IUCN Red List.",
            "Coastal development and fishing can threaten important nursery habitats such as mangroves.",
            "Young lemon sharks often use shallow coastal areas as nurseries before moving into deeper water."
        ]
    }
]

computerAnimal = random.choice(animals)
playerAnimal = random.choice(animals)
print (f"Your animal is {playerAnimal["name"]}. Are you happy with this animal?")
choice = input().lower()

while choice != "yes":
    while choice != "yes" and choice != "no":
     print(f"Please enter either yes or no")
     choice = input().lower()
    playerAnimal = random.choice(animals)
    print(f"Your animal is {playerAnimal["name"]}. Are you happy with this now?")
    choice = input().lower()

print("Great! The computer has been assigned its animal, too. Let's start! The computer will ask you a question, please reply with 'yes', 'no', 'it depends', or 'I don't know' if you really don't know (idk is also acceptable). You can then ask a question of your own.")


function 


