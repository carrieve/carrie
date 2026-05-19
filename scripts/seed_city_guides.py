#!/usr/bin/env python3
"""
Carrie — Curated City Guide Seeder

Seeds ~/.carrie/city_guides/ with hand-curated, EA-vetted data for top
business travel cities: restaurants, hotels, and ground transport.

Run once to populate all cities, then use build_city_guides.py to
supplement with live Reddit data.

Usage:
    python3 seed_city_guides.py
"""

import json
from pathlib import Path
from datetime import datetime

GUIDES_DIR = Path.home() / ".carrie" / "city_guides"
GUIDES_DIR.mkdir(parents=True, exist_ok=True)

UPDATED = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

CITIES = {

  "New York City": {
    "restaurants": [
      {
        "name": "The Grill",
        "neighborhood": "Midtown East",
        "cuisine": "American / Steakhouse",
        "vibe": "Power dining — where deals get signed. NYT top 100.",
        "best_for": "C-suite client dinners, deal closings",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Tableside prime rib. Private room fits 6-125. Book 4-6 weeks out.",
        "reservations": "OpenTable or direct: thegrillnewyork.com"
      },
      {
        "name": "Keens Steakhouse",
        "neighborhood": "Midtown",
        "cuisine": "Classic Steakhouse",
        "vibe": "NYC institution since 1885. Dark wood, leather, serious steaks.",
        "best_for": "Traditional client dinners, impressing out-of-towners",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Four private rooms, 20-80 guests. Old-world prestige every exec loves.",
        "reservations": "keens.com"
      },
      {
        "name": "COTE Korean Steakhouse",
        "neighborhood": "Flatiron",
        "cuisine": "Korean / American Steakhouse",
        "vibe": "Interactive, fun, memorable. Only Michelin-starred Korean steakhouse in the US.",
        "best_for": "Celebratory dinners, clients who want something different",
        "price": "$$$$",
        "private_dining": True,
        "notes": "1,200+ label wine list. Tableside BBQ. Clients remember this one.",
        "reservations": "exploretock.com/cote"
      },
      {
        "name": "Le Bernardin",
        "neighborhood": "Midtown West",
        "cuisine": "French Seafood",
        "vibe": "Three Michelin stars. The pinnacle of fine dining in NYC.",
        "best_for": "Highest-level client entertainment, VIP guests",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Private room for 12. Book 6-8 weeks out minimum.",
        "reservations": "le-bernardin.com"
      },
      {
        "name": "Carbone",
        "neighborhood": "Greenwich Village",
        "cuisine": "Italian-American",
        "vibe": "Celebrity hotspot with incredible food. Red sauce, elevated.",
        "best_for": "Media/entertainment clients, celebratory dinners",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Very hard to get. Book through Resy the moment slots open (6am).",
        "reservations": "resy.com"
      }
    ],
    "hotels": [
      {
        "name": "The Peninsula New York",
        "neighborhood": "Midtown / Fifth Avenue",
        "brand": "Peninsula",
        "tier": "Ultra-luxury",
        "best_for": "Top executives, VIP guests",
        "notes": "Rooftop bar with Central Park views. Exceptional service. One of NYC's best.",
        "loyalty": "Peninsula Privileged Guests",
        "website": "peninsula.com"
      },
      {
        "name": "Four Seasons New York Downtown",
        "neighborhood": "Tribeca",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Finance/fintech execs near Wall St",
        "notes": "Robert A.M. Stern-designed. Largest rooms of any NYC Four Seasons.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/newyorkdowntown"
      },
      {
        "name": "The St. Regis New York",
        "neighborhood": "Midtown / Fifth Avenue",
        "brand": "Marriott / St. Regis",
        "tier": "Ultra-luxury",
        "best_for": "Traditional luxury, long stays",
        "notes": "Butler service. King Cole Bar is an iconic NYC institution.",
        "loyalty": "Marriott Bonvoy",
        "website": "marriott.com/stregis"
      },
      {
        "name": "The Carlyle",
        "neighborhood": "Upper East Side",
        "brand": "Rosewood",
        "tier": "Ultra-luxury",
        "best_for": "Executives who value privacy and Old New York elegance",
        "notes": "A New York City legend. Bemelmans Bar. Discreet, no scene.",
        "loyalty": "Rosewood Sense",
        "website": "rosewoodhotels.com/en/the-carlyle"
      },
      {
        "name": "Mandarin Oriental New York",
        "neighborhood": "Columbus Circle / Central Park",
        "brand": "Mandarin Oriental",
        "tier": "Luxury",
        "best_for": "Stunning views, spa, visiting international executives",
        "notes": "35th–54th floors of the Time Warner Center. Central Park views from most rooms.",
        "loyalty": "Fans of MO",
        "website": "mandarinoriental.com/new-york"
      }
    ],
    "transport": [
      {
        "name": "Go Ground and Air",
        "type": "Black Car / Car Service",
        "notes": "Repeatedly recommended by NYC EAs. Used daily for execs, board members. Reliable.",
        "source": "r/ExecutiveAssistants (multiple upvoted mentions)"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network. 'For very picky execs.' Professional, consistent.",
        "source": "r/ExecutiveAssistants (confirmed by multiple EAs)"
      },
      {
        "name": "Commonwealth Limousine",
        "type": "Black Car / Limo",
        "notes": "NYC and Northeast coverage. EA community favorite.",
        "source": "r/ExecutiveAssistants"
      },
      {
        "name": "Dial 7",
        "type": "Car Service",
        "notes": "NYC institution. Large fleet, flat rates, reliable for airport runs.",
        "website": "dial7.com"
      }
    ]
  },

  "Los Angeles": {
    "restaurants": [
      {
        "name": "Spago Beverly Hills",
        "neighborhood": "Beverly Hills",
        "cuisine": "California / Contemporary",
        "vibe": "Wolfgang Puck's flagship. A classic power lunch and dinner spot.",
        "best_for": "Entertainment industry clients, celebrity-adjacent dinners",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Book through OpenTable. Celebrity sightings common.",
        "reservations": "wolfgangpuck.com/restaurants/spago"
      },
      {
        "name": "Nobu Malibu",
        "neighborhood": "Malibu",
        "cuisine": "Japanese / Sushi",
        "vibe": "Stunning ocean views, celebrity staple, world-class Japanese food.",
        "best_for": "VIP clients, entertainment execs, sunset dinners",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Hard to get. Book 3-4 weeks out. Valet required.",
        "reservations": "noburestaurants.com"
      },
      {
        "name": "Bestia",
        "neighborhood": "Arts District / DTLA",
        "cuisine": "Italian",
        "vibe": "Modern, buzzy Italian. One of LA's most acclaimed restaurants.",
        "best_for": "Tech/creative clients, group dinners",
        "price": "$$$",
        "private_dining": False,
        "notes": "Resy only. Opens 60 days out at 8am — grab it immediately.",
        "reservations": "resy.com"
      },
      {
        "name": "n/naka",
        "neighborhood": "Palms",
        "cuisine": "Japanese Kaiseki",
        "vibe": "Intimate, extraordinary. One of the hardest reservations in the US.",
        "best_for": "Ultimate VIP dining experience",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Lottery-style reservations. Plan months ahead. Unforgettable experience.",
        "reservations": "exploretock.com/nnaka"
      }
    ],
    "hotels": [
      {
        "name": "Hotel Bel-Air",
        "neighborhood": "Bel Air",
        "brand": "Dorchester Collection",
        "tier": "Ultra-luxury",
        "best_for": "VIP guests, celebrities, ultimate privacy",
        "notes": "12 acres of gardens. Swan lake. The most discreet hotel in LA.",
        "loyalty": "Dorchester Diamond",
        "website": "dorchestercollection.com/en/los-angeles/hotel-bel-air"
      },
      {
        "name": "The Peninsula Beverly Hills",
        "neighborhood": "Beverly Hills",
        "brand": "Peninsula",
        "tier": "Ultra-luxury",
        "best_for": "Entertainment and business executives",
        "notes": "Legendary pool terrace. Walking distance to Rodeo Drive.",
        "loyalty": "Peninsula Privileged Guests",
        "website": "peninsula.com/beverly-hills"
      },
      {
        "name": "Four Seasons Los Angeles at Beverly Hills",
        "neighborhood": "Beverly Hills",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Reliable luxury, great service, central location",
        "notes": "Pool with private cabanas. Excellent spa. Consistent favorite.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/losangeles"
      },
      {
        "name": "Waldorf Astoria Beverly Hills",
        "neighborhood": "Beverly Hills",
        "brand": "Hilton / Waldorf",
        "tier": "Luxury",
        "best_for": "Modern luxury, rooftop pool with 360 views",
        "notes": "Jean-Georges restaurant on-site. Newer property, impeccable finishes.",
        "loyalty": "Hilton Honors",
        "website": "waldorfastoria.hilton.com/beverlyhills"
      }
    ],
    "transport": [
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Professional, global network. Great for airport transfers. Predictable pricing.",
        "website": "blacklane.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Consistent for picky executives. Professional drivers.",
        "website": "carey.com"
      },
      {
        "name": "LA Limousine",
        "type": "Limo / Car Service",
        "notes": "LA institution. Good for airport runs, event transport.",
        "website": "lalimo.com"
      }
    ]
  },

  "San Francisco": {
    "restaurants": [
      {
        "name": "Gary Danko",
        "neighborhood": "Fisherman's Wharf",
        "cuisine": "Contemporary American",
        "vibe": "SF institution. Sophisticated, quiet, impeccable service.",
        "best_for": "Traditional executive dining, investors",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Book 4+ weeks out. Prix fixe menu. One of SF's most decorated.",
        "reservations": "garydanko.com"
      },
      {
        "name": "Quince",
        "neighborhood": "Jackson Square",
        "cuisine": "Italian-Californian",
        "vibe": "Three Michelin stars. Elegant, quiet, exceptional.",
        "best_for": "Top-tier VIP dinners, investors",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Prix fixe tasting menu. Private dining available.",
        "reservations": "quince-sf.com"
      },
      {
        "name": "Bix",
        "neighborhood": "Jackson Square / Financial District",
        "cuisine": "American / Supper Club",
        "vibe": "Jazz supper club feel. Intimate, sophisticated, great cocktails.",
        "best_for": "After-work client dinners, tech execs",
        "price": "$$$",
        "private_dining": True,
        "notes": "One of SF's most beloved restaurants. Consistent favorite.",
        "reservations": "bixrestaurant.com"
      },
      {
        "name": "Nopa",
        "neighborhood": "Western Addition / NoPa",
        "cuisine": "Organic / California",
        "vibe": "Buzzy, local, organic wood-fired cooking. SF favorite.",
        "best_for": "Tech clients who care about food quality and sourcing",
        "price": "$$$",
        "private_dining": False,
        "notes": "Open until 1am. Book on Resy — fills fast.",
        "reservations": "resy.com"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons San Francisco at Embarcadero",
        "neighborhood": "Embarcadero / Financial District",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, proximity to FiDi",
        "notes": "Bay views, excellent service. Close to Ferry Building.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/sanfrancisco"
      },
      {
        "name": "The Ritz-Carlton San Francisco",
        "neighborhood": "Nob Hill",
        "brand": "Marriott / Ritz-Carlton",
        "tier": "Luxury",
        "best_for": "Traditional luxury, central location",
        "notes": "Nob Hill landmark. Grand rooms, excellent spa.",
        "loyalty": "Marriott Bonvoy",
        "website": "ritzcarlton.com/san-francisco"
      },
      {
        "name": "The St. Regis San Francisco",
        "neighborhood": "SoMa / Museum District",
        "brand": "Marriott / St. Regis",
        "tier": "Luxury",
        "best_for": "Modern luxury, close to SFMOMA",
        "notes": "Butler service. Sleek and contemporary. Great for tech execs.",
        "loyalty": "Marriott Bonvoy",
        "website": "marriott.com/stregis"
      },
      {
        "name": "Fairmont San Francisco",
        "neighborhood": "Nob Hill",
        "brand": "Accor / Fairmont",
        "tier": "Luxury",
        "best_for": "Classic SF grandeur, stunning lobby",
        "notes": "Historic Nob Hill landmark. Large rooms, iconic views.",
        "loyalty": "ALL (Accor Live Limitless)",
        "website": "fairmont.com/san-francisco"
      }
    ],
    "transport": [
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Best for airport transfers SFO/OAK. Professional, trackable.",
        "website": "blacklane.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Reliable for executive transport across the Bay Area.",
        "website": "carey.com"
      },
      {
        "name": "Cloud 9 Limousine",
        "type": "Limo / Car Service",
        "notes": "Bay Area focused. Good fleet, professional drivers.",
        "website": "cloud9limo.com"
      }
    ]
  },

  "Austin": {
    "restaurants": [
      {
        "name": "Uchi",
        "neighborhood": "South Lamar",
        "cuisine": "Japanese / Sushi",
        "vibe": "James Beard-winning chef. Austin's most acclaimed restaurant.",
        "best_for": "Tech client dinners, celebratory meals",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Book well in advance. Private dining available.",
        "reservations": "uchirestaurants.com"
      },
      {
        "name": "Emmer & Rye",
        "neighborhood": "Rainey Street",
        "cuisine": "Modern American",
        "vibe": "Grain-focused, rotating menu. One of Austin's most creative restaurants.",
        "best_for": "Food-forward clients, creative industry",
        "price": "$$$",
        "private_dining": False,
        "notes": "Tasting menu format. Reserve ahead on Resy.",
        "reservations": "resy.com"
      },
      {
        "name": "Jeffrey's",
        "neighborhood": "Clarksville",
        "cuisine": "American / Continental",
        "vibe": "Austin institution since 1975. Quiet, elegant, perfect for conversation.",
        "best_for": "Traditional executive dining, investor meetings",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Austin's most established fine dining. Great wine list.",
        "reservations": "jeffreysofaustin.com"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Austin",
        "neighborhood": "Downtown / Lady Bird Lake",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, best location in Austin",
        "notes": "On Lady Bird Lake. Pool with views. Most requested by executives.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/austin"
      },
      {
        "name": "Fairmont Austin",
        "neighborhood": "Downtown",
        "brand": "Accor / Fairmont",
        "tier": "Luxury",
        "best_for": "Large groups, conventions, rooftop pool",
        "notes": "Largest hotel in Austin. Massive rooftop pool. Great for conferences.",
        "loyalty": "ALL (Accor Live Limitless)",
        "website": "fairmont.com/austin"
      },
      {
        "name": "Hotel Van Zandt",
        "neighborhood": "Rainey Street",
        "brand": "Loews",
        "tier": "Upscale",
        "best_for": "Music/tech/creative executives, lively scene",
        "notes": "Live music hotel. On Rainey Street. Rooftop pool. Very Austin.",
        "loyalty": "Loews You First",
        "website": "hotelvanzandt.com"
      },
      {
        "name": "The Joseph",
        "neighborhood": "Downtown",
        "brand": "Marriott / Autograph",
        "tier": "Luxury",
        "best_for": "Art-forward executives, design-conscious travelers",
        "notes": "Boutique luxury with curated art collection. Rooftop bar.",
        "loyalty": "Marriott Bonvoy",
        "website": "thejosephaustin.com"
      }
    ],
    "transport": [
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Most reliable for AUS airport transfers. Professional drivers.",
        "website": "blacklane.com"
      },
      {
        "name": "Austin Limo & Car Service",
        "type": "Limo / Car Service",
        "notes": "Local Austin service. Good for multi-stop executive days.",
        "website": "austinlimoservice.com"
      },
      {
        "name": "ExecuCar",
        "type": "Black Car / App",
        "notes": "Nationwide network. Reliable for airport runs.",
        "website": "execucar.com"
      }
    ]
  },

  "Chicago": {
    "restaurants": [
      {
        "name": "Alinea",
        "neighborhood": "Lincoln Park",
        "cuisine": "Modern American / Avant-garde",
        "vibe": "Three Michelin stars. One of the world's great restaurants. An experience, not just dinner.",
        "best_for": "Ultimate VIP dining, clients who want to be wowed",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Prepaid ticketed reservations. Book months out. Unforgettable.",
        "reservations": "exploretock.com/alinea"
      },
      {
        "name": "Maple & Ash",
        "neighborhood": "Gold Coast",
        "cuisine": "Wood-fired Steakhouse",
        "vibe": "Modern, sexy steakhouse. Great scene without being stuffy.",
        "best_for": "Client dinners, Chicago power dining",
        "price": "$$$$",
        "private_dining": True,
        "notes": "One of Chicago's hottest restaurants. Book 3-4 weeks out.",
        "reservations": "resy.com"
      },
      {
        "name": "Smyth",
        "neighborhood": "West Loop",
        "cuisine": "Modern American",
        "vibe": "Two Michelin stars. Farm-driven, creative, intimate.",
        "best_for": "Food-forward clients, investors, celebratory meals",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Tasting menu. Book well ahead on Tock.",
        "reservations": "exploretock.com/smyth"
      },
      {
        "name": "RPM Steak",
        "neighborhood": "River North",
        "cuisine": "Steakhouse",
        "vibe": "Chicago's go-to power steakhouse. Beautiful room, great service.",
        "best_for": "Traditional executive client dinners",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Celebrity-owned (Giuliana & Bill Rancic). Always impresses.",
        "reservations": "rpmrestaurants.com"
      }
    ],
    "hotels": [
      {
        "name": "The Langham Chicago",
        "neighborhood": "River North",
        "brand": "Langham",
        "tier": "Ultra-luxury",
        "best_for": "Top executives, best service in Chicago",
        "notes": "Stunning Riverwalk location. Award-winning spa. Quiet, refined.",
        "loyalty": "Langham Privilege",
        "website": "chicago.langhamhotels.com"
      },
      {
        "name": "Four Seasons Chicago",
        "neighborhood": "Magnificent Mile",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, Mag Mile location",
        "notes": "Floors 30-46 of a tower. Stunning city views. Consistent favorite.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/chicago"
      },
      {
        "name": "Waldorf Astoria Chicago",
        "neighborhood": "Gold Coast",
        "brand": "Hilton / Waldorf",
        "tier": "Luxury",
        "best_for": "Luxury travelers, Gold Coast location",
        "notes": "Boutique feel within the Waldorf brand. Excellent restaurant.",
        "loyalty": "Hilton Honors",
        "website": "waldorfastoria.hilton.com/chicago"
      },
      {
        "name": "The Kimpton Gray Hotel",
        "neighborhood": "Loop / Financial District",
        "brand": "IHG / Kimpton",
        "tier": "Upscale",
        "best_for": "Finance execs, great location for Loop meetings",
        "notes": "Housed in a 1910 landmark building. Vol. 39 rooftop bar.",
        "loyalty": "IHG One Rewards",
        "website": "thegrayhotel.com"
      }
    ],
    "transport": [
      {
        "name": "Windy City Limousine",
        "type": "Black Car / Limo",
        "notes": "Chicago's most established car service. Used by major corporations.",
        "website": "windycitylimo.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network, consistent service. Good for ORD/MDW airport runs.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Professional, app-based. Great for trackable airport transfers.",
        "website": "blacklane.com"
      }
    ]
  },

  "Charlotte": {
    "restaurants": [
      {
        "name": "Heirloom",
        "neighborhood": "Elizabeth",
        "cuisine": "Southern / Farm-to-table",
        "vibe": "Charlotte's most acclaimed restaurant. Farm-to-table, intimate, exceptional.",
        "best_for": "Impressive client dinners, food-forward executives",
        "price": "$$$$",
        "private_dining": True,
        "notes": "James Beard-nominated. Book 2-3 weeks out.",
        "reservations": "heirloomrestaurant.net"
      },
      {
        "name": "The Capital Grille Charlotte",
        "neighborhood": "SouthPark",
        "cuisine": "Steakhouse",
        "vibe": "Reliable, polished, great for conservative clients. Always impresses.",
        "best_for": "Traditional client dinners, banking/finance executives",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Private dining rooms. Part of a national chain — consistent quality.",
        "reservations": "thecapitalgrille.com"
      },
      {
        "name": "Rare Roots",
        "neighborhood": "South End",
        "cuisine": "Modern American",
        "vibe": "Creative, chef-driven, excellent cocktail program.",
        "best_for": "Tech and creative industry clients",
        "price": "$$$",
        "private_dining": False,
        "notes": "One of Charlotte's rising stars. Book on OpenTable.",
        "reservations": "opentable.com"
      },
      {
        "name": "McNinch House",
        "neighborhood": "Fourth Ward",
        "cuisine": "Contemporary American",
        "vibe": "Historic Victorian house. Incredibly intimate (6 tables). Charlotte's most special dinner.",
        "best_for": "Highest-level VIP guests, intimate executive dinners",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Reserve months ahead. Prix fixe only. Truly unique Charlotte experience.",
        "reservations": "mcninchhouserestaurant.com"
      }
    ],
    "hotels": [
      {
        "name": "The Ritz-Carlton Charlotte",
        "neighborhood": "Uptown",
        "brand": "Marriott / Ritz-Carlton",
        "tier": "Luxury",
        "best_for": "Top executives, best hotel in Charlotte",
        "notes": "Connected to EpiCentre. Best service in the city. Default choice for VIPs.",
        "loyalty": "Marriott Bonvoy",
        "website": "ritzcarlton.com/charlotte"
      },
      {
        "name": "Le Méridien Charlotte",
        "neighborhood": "Uptown",
        "brand": "Marriott / Le Méridien",
        "tier": "Upscale",
        "best_for": "Business travelers, design-conscious guests",
        "notes": "Art-forward property. Good location near Convention Center.",
        "loyalty": "Marriott Bonvoy",
        "website": "marriott.com/lemeridiencharlotte"
      },
      {
        "name": "Kimpton Tryon Park Hotel",
        "neighborhood": "Uptown",
        "brand": "IHG / Kimpton",
        "tier": "Upscale",
        "best_for": "Tech/creative executives, boutique feel",
        "notes": "Rooftop bar. Across from Truist Field. Lively scene.",
        "loyalty": "IHG One Rewards",
        "website": "tryonparkhotel.com"
      }
    ],
    "transport": [
      {
        "name": "Crown Limousine",
        "type": "Black Car / Limo",
        "notes": "Charlotte's most established car service. CLT airport specialists.",
        "website": "crownlimousine.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Reliable for CLT airport transfers. App-based tracking.",
        "website": "blacklane.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "National network. Good for multi-city executive travel.",
        "website": "carey.com"
      }
    ]
  },

  "London": {
    "restaurants": [
      {
        "name": "The Wolseley",
        "neighborhood": "Mayfair / Piccadilly",
        "cuisine": "European / Brasserie",
        "vibe": "Grand Viennese café in a stunning former car showroom. London's power breakfast/lunch spot.",
        "best_for": "Business lunches, impressing international visitors",
        "price": "$$$",
        "private_dining": False,
        "notes": "Book well ahead. A London institution. Beloved by executives.",
        "reservations": "thewolseley.com"
      },
      {
        "name": "Gymkhana",
        "neighborhood": "Mayfair",
        "cuisine": "Indian",
        "vibe": "Michelin-starred. Refined Indian cuisine in a beautiful Colonial-club setting.",
        "best_for": "Clients who want something memorable and different",
        "price": "$$$$",
        "private_dining": True,
        "notes": "One of London's most acclaimed. Private dining available.",
        "reservations": "gymkhanalondon.com"
      },
      {
        "name": "Scott's",
        "neighborhood": "Mayfair",
        "cuisine": "Seafood / British",
        "vibe": "Iconic Mayfair seafood institution. Consistently excellent.",
        "best_for": "Traditional British client dining, VIP guests",
        "price": "$$$$",
        "private_dining": True,
        "notes": "One of London's most beloved. Book 3+ weeks out.",
        "reservations": "scotts-restaurant.com"
      },
      {
        "name": "Rules",
        "neighborhood": "Covent Garden",
        "cuisine": "Traditional British",
        "vibe": "London's oldest restaurant (1798). Historic, charming, exceptional game.",
        "best_for": "Impressing international visitors, traditional British experience",
        "price": "$$$",
        "private_dining": True,
        "notes": "A true London experience. Visited by monarchs and writers for 200+ years.",
        "reservations": "rules.co.uk"
      }
    ],
    "hotels": [
      {
        "name": "Claridge's",
        "neighborhood": "Mayfair",
        "brand": "Maybourne",
        "tier": "Ultra-luxury",
        "best_for": "Top-tier VIP guests, classic London luxury",
        "notes": "The Art Deco masterpiece. London's most famous address. Exceptional service.",
        "loyalty": "Maybourne Rewards",
        "website": "claridges.co.uk"
      },
      {
        "name": "The Connaught",
        "neighborhood": "Mayfair",
        "brand": "Maybourne",
        "tier": "Ultra-luxury",
        "best_for": "Discreet luxury, privacy, impeccable service",
        "notes": "Consistently rated world's best hotel. Hélène Darroze restaurant on-site.",
        "loyalty": "Maybourne Rewards",
        "website": "the-connaught.co.uk"
      },
      {
        "name": "The Savoy",
        "neighborhood": "Strand / Covent Garden",
        "brand": "Fairmont",
        "tier": "Ultra-luxury",
        "best_for": "Historic grandeur, central location, entertainment industry",
        "notes": "London icon since 1889. Art Deco and Edwardian suites. American Bar.",
        "loyalty": "ALL (Accor Live Limitless)",
        "website": "thesavoylondon.com"
      },
      {
        "name": "Mandarin Oriental Hyde Park",
        "neighborhood": "Knightsbridge",
        "brand": "Mandarin Oriental",
        "tier": "Ultra-luxury",
        "best_for": "Hyde Park views, Knightsbridge shopping, Heston Blumenthal restaurant",
        "notes": "Newly renovated. Dinner at Dinner by Heston Blumenthal on-site.",
        "loyalty": "Fans of MO",
        "website": "mandarinoriental.com/london"
      },
      {
        "name": "45 Park Lane",
        "neighborhood": "Mayfair / Park Lane",
        "brand": "Dorchester Collection",
        "tier": "Ultra-luxury",
        "best_for": "Contemporary luxury, Hyde Park views",
        "notes": "Sleeker and more modern than The Dorchester next door. Wolfgang Puck restaurant.",
        "loyalty": "Dorchester Diamond",
        "website": "45parklane.com"
      }
    ],
    "transport": [
      {
        "name": "Addison Lee",
        "type": "Black Car / App",
        "notes": "London's most-used executive car service. Reliable, app-based, professional.",
        "website": "addisonlee.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network, consistent for Heathrow and Gatwick transfers.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Great for LHR/LGW/LCY transfers. Fixed pricing, no surge.",
        "website": "blacklane.com"
      },
      {
        "name": "Green Tomato Cars",
        "type": "Eco Car Service",
        "notes": "London-based, hybrid/electric fleet. Popular for sustainability-conscious executives.",
        "website": "greentomatocars.com"
      }
    ]
  },

  "Seattle": {
    "restaurants": [
      {
        "name": "Canlis",
        "neighborhood": "Queen Anne",
        "cuisine": "Contemporary American",
        "vibe": "Seattle institution since 1950. Stunning views, exceptional service, legendary wine list.",
        "best_for": "Top executive dinners, VIP client entertainment",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Book weeks ahead. A Seattle rite of passage. Views of Lake Union.",
        "reservations": "canlis.com"
      },
      {
        "name": "The Metropolitan Grill",
        "neighborhood": "Downtown",
        "cuisine": "Steakhouse",
        "vibe": "Seattle's premier steakhouse. Old-school, professional, reliable.",
        "best_for": "Business dinners, conservative clients, Microsoft/Amazon execs",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Private dining rooms. A Seattle power dinner staple.",
        "reservations": "themetropolitangrill.com"
      },
      {
        "name": "Altura",
        "neighborhood": "Capitol Hill",
        "cuisine": "Italian",
        "vibe": "Intimate Italian tasting menu. One of Seattle's most acclaimed.",
        "best_for": "Food-forward clients, intimate dinners",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Small room, personal service. Book well ahead.",
        "reservations": "alturarestaurant.com"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Seattle",
        "neighborhood": "Downtown / Waterfront",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, waterfront views",
        "notes": "Stunning Elliott Bay and Olympic Mountain views. Best service in Seattle.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/seattle"
      },
      {
        "name": "The Fairmont Olympic",
        "neighborhood": "Downtown",
        "brand": "Accor / Fairmont",
        "tier": "Luxury",
        "best_for": "Classic Seattle grand hotel, central location",
        "notes": "Historic 1924 landmark. High tea tradition. Large rooms.",
        "loyalty": "ALL (Accor Live Limitless)",
        "website": "fairmont.com/seattle"
      },
      {
        "name": "Kimpton Hotel Monaco Seattle",
        "neighborhood": "Downtown",
        "brand": "IHG / Kimpton",
        "tier": "Upscale",
        "best_for": "Tech executives, boutique feel, pet-friendly",
        "notes": "Playful design, great bar, walk to Pike Place Market.",
        "loyalty": "IHG One Rewards",
        "website": "monaco-seattle.com"
      }
    ],
    "transport": [
      {
        "name": "Eastside Limousine",
        "type": "Black Car / Limo",
        "notes": "Seattle's most established car service. SEA airport specialists.",
        "website": "eastsidetransportation.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Reliable for SEA transfers. Professional fleet.",
        "website": "blacklane.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network. Good for Microsoft/Amazon campus transfers.",
        "website": "carey.com"
      }
    ]
  },

  "Boston": {
    "restaurants": [
      {
        "name": "Menton",
        "neighborhood": "Fort Point / Seaport",
        "cuisine": "French / Italian",
        "vibe": "Barbara Lynch's flagship. Boston's most refined dining experience.",
        "best_for": "Top-tier client dinners, investors, VIP guests",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Prix fixe tasting menu. Private dining available. Book 3+ weeks out.",
        "reservations": "mentonboston.com"
      },
      {
        "name": "Grill 23 & Bar",
        "neighborhood": "Back Bay",
        "cuisine": "Steakhouse",
        "vibe": "Boston's premier power steakhouse. Classic, refined, consistent.",
        "best_for": "Finance/biotech client dinners, traditional executives",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Private rooms. Near Copley Square. Boston institution.",
        "reservations": "grill23.com"
      },
      {
        "name": "No. 9 Park",
        "neighborhood": "Beacon Hill",
        "cuisine": "French / Italian",
        "vibe": "Barbara Lynch classic. Elegant, intimate, exceptional wine list.",
        "best_for": "Sophisticated client dinners, Boston power lunches",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Across from Boston Common. One of Boston's most beloved.",
        "reservations": "no9park.com"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons One Dalton Street",
        "neighborhood": "Back Bay",
        "brand": "Four Seasons",
        "tier": "Ultra-luxury",
        "best_for": "Top executives, best hotel in Boston",
        "notes": "Highest residential tower in New England. Stunning views. New and exceptional.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/boston"
      },
      {
        "name": "The Ritz-Carlton Boston Common",
        "neighborhood": "Downtown / Theater District",
        "brand": "Marriott / Ritz-Carlton",
        "tier": "Luxury",
        "best_for": "Business travelers, central location",
        "notes": "Connected to Avery Bar. Walk to Common and financial district.",
        "loyalty": "Marriott Bonvoy",
        "website": "ritzcarlton.com/boston"
      },
      {
        "name": "Mandarin Oriental Boston",
        "neighborhood": "Back Bay",
        "brand": "Mandarin Oriental",
        "tier": "Luxury",
        "best_for": "Luxury travelers, Boylston Street location",
        "notes": "Excellent spa. Walk to Newbury Street shopping.",
        "loyalty": "Fans of MO",
        "website": "mandarinoriental.com/boston"
      }
    ],
    "transport": [
      {
        "name": "Commonwealth Limousine",
        "type": "Black Car / Limo",
        "notes": "Boston's most used executive car service. Highly reliable for BOS.",
        "website": "commonwealthlimo.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network, consistent quality for Logan airport runs.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "App-based tracking. Professional for BOS transfers.",
        "website": "blacklane.com"
      }
    ]
  },

  "Miami": {
    "restaurants": [
      {
        "name": "Carbone Miami",
        "neighborhood": "South Beach",
        "cuisine": "Italian-American",
        "vibe": "NYC's Carbone comes to Miami. Celebrity hotspot, incredible food.",
        "best_for": "Entertainment/media clients, high-profile dinners",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Extremely hard to get. Book on Resy the moment slots open.",
        "reservations": "resy.com"
      },
      {
        "name": "Zuma Miami",
        "neighborhood": "Brickell / Downtown",
        "cuisine": "Japanese / Robata",
        "vibe": "Finance district hotspot. Great for deal-closing dinners. Beautiful waterfront.",
        "best_for": "Finance and tech client dinners",
        "price": "$$$$",
        "private_dining": True,
        "notes": "On the Miami River. Private dining available.",
        "reservations": "zumarestaurant.com"
      },
      {
        "name": "Le Jardinier",
        "neighborhood": "Design District",
        "cuisine": "French / Vegetable-forward",
        "vibe": "Elegant, beautiful room in the Design District. Starred chef, lighter cuisine.",
        "best_for": "Health-conscious executives, design/art industry clients",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Inside the Institute of Contemporary Art building.",
        "reservations": "lejardiniermiami.com"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Brickell",
        "neighborhood": "Brickell / Financial District",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, finance executives",
        "notes": "Best hotel for Brickell meetings. Pool deck with Biscayne Bay views.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/miami"
      },
      {
        "name": "Mandarin Oriental Miami",
        "neighborhood": "Brickell Key Island",
        "brand": "Mandarin Oriental",
        "tier": "Ultra-luxury",
        "best_for": "VIP guests, privacy, stunning bay views",
        "notes": "On its own island. Stunning waterfront. One of Miami's finest.",
        "loyalty": "Fans of MO",
        "website": "mandarinoriental.com/miami"
      },
      {
        "name": "The Miami Beach EDITION",
        "neighborhood": "Mid-Beach",
        "brand": "Marriott / EDITION",
        "tier": "Luxury",
        "best_for": "Creative/media executives, design-forward travelers",
        "notes": "Ian Schrager design. Beautiful beach, great nightlife on-site.",
        "loyalty": "Marriott Bonvoy",
        "website": "editionhotels.com/miami-beach"
      }
    ],
    "transport": [
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Reliable for MIA airport transfers and Brickell/South Beach transport.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "App-based, professional. Great for MIA and FLL airport runs.",
        "website": "blacklane.com"
      },
      {
        "name": "South Florida Limousine",
        "type": "Limo / Car Service",
        "notes": "Miami-based fleet. Good for multi-stop executive days across the city.",
        "website": "southfloridalimousine.com"
      }
    ]
  },

  "Denver": {
    "restaurants": [
      {
        "name": "Elway's",
        "neighborhood": "Cherry Creek / Downtown",
        "cuisine": "Steakhouse",
        "vibe": "John Elway's restaurant. Denver's go-to power steakhouse.",
        "best_for": "Traditional client dinners, sports industry connections",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Multiple locations. Reliable, consistent, always impresses.",
        "reservations": "elways.com"
      },
      {
        "name": "Mercantile Dining & Provision",
        "neighborhood": "Union Station",
        "cuisine": "Colorado / Farm-to-table",
        "vibe": "Alex Seidel's celebrated restaurant in historic Union Station.",
        "best_for": "Creative/tech clients, business lunches near downtown",
        "price": "$$$",
        "private_dining": False,
        "notes": "One of Denver's most acclaimed. Book on OpenTable.",
        "reservations": "opentable.com"
      },
      {
        "name": "Rioja",
        "neighborhood": "Larimer Square",
        "cuisine": "Mediterranean",
        "vibe": "Jennifer Jasinski's award-winning Larimer Square gem. Warm, excellent.",
        "best_for": "Sophisticated client dinners, food-forward executives",
        "price": "$$$",
        "private_dining": True,
        "notes": "James Beard-nominated. Private dining available.",
        "reservations": "riojadenver.com"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Denver",
        "neighborhood": "Downtown",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, best service in Denver",
        "notes": "Rooftop pool with mountain views. Best hotel in the city.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/denver"
      },
      {
        "name": "The Brown Palace",
        "neighborhood": "Downtown",
        "brand": "Independent / Marriott Tribute",
        "tier": "Luxury",
        "best_for": "History-lovers, classic Denver luxury",
        "notes": "Denver landmark since 1892. Atrium lobby. Every US president has stayed here.",
        "loyalty": "Marriott Bonvoy",
        "website": "brownpalace.com"
      },
      {
        "name": "The Crawford Hotel",
        "neighborhood": "Union Station",
        "brand": "Independent",
        "tier": "Upscale",
        "best_for": "Design-conscious travelers, Union Station location",
        "notes": "Boutique hotel inside the historic Union Station. Great bars.",
        "loyalty": "None (independent)",
        "website": "thecrawfordhotel.com"
      }
    ],
    "transport": [
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "Reliable for DEN airport transfers (long drive — 45 min). Professional.",
        "website": "blacklane.com"
      },
      {
        "name": "Colorado Limo",
        "type": "Limo / Car Service",
        "notes": "Denver-based fleet. Good for multi-stop executive days.",
        "website": "coloradolimo.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "National network. Good for DEN runs and consistent quality.",
        "website": "carey.com"
      }
    ]
  },

  "Atlanta": {
    "restaurants": [
      {
        "name": "Bacchanalia",
        "neighborhood": "West Midtown",
        "cuisine": "Contemporary American",
        "vibe": "Atlanta's most acclaimed restaurant. Quietly exceptional for 30 years.",
        "best_for": "Top executive client dinners, VIP guests",
        "price": "$$$$",
        "private_dining": True,
        "notes": "James Beard award. Book 3-4 weeks out. An Atlanta institution.",
        "reservations": "starprovisions.com"
      },
      {
        "name": "Hal's",
        "neighborhood": "Inman Park",
        "cuisine": "Steakhouse / Southern",
        "vibe": "Old-school Atlanta power dinner. Historic location, great steaks.",
        "best_for": "Traditional client dinners, finance and media executives",
        "price": "$$$$",
        "private_dining": True,
        "notes": "A true Atlanta institution. Private rooms available.",
        "reservations": "hals.com"
      },
      {
        "name": "Staplehouse",
        "neighborhood": "Old Fourth Ward",
        "cuisine": "Modern American",
        "vibe": "James Beard Award winner. Tasting menu, intimate, exceptional.",
        "best_for": "Food-forward clients, celebratory dinners",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Nonprofit model — all proceeds benefit hospitality workers in need.",
        "reservations": "exploretock.com/staplehouse"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Atlanta",
        "neighborhood": "Midtown",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, best service in Atlanta",
        "notes": "In the heart of Midtown. Excellent spa and restaurant.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/atlanta"
      },
      {
        "name": "The St. Regis Atlanta",
        "neighborhood": "Buckhead",
        "brand": "Marriott / St. Regis",
        "tier": "Ultra-luxury",
        "best_for": "VIP guests, Buckhead location, butler service",
        "notes": "Buckhead's finest. Butler service, rooftop pool, exceptional restaurant.",
        "loyalty": "Marriott Bonvoy",
        "website": "marriott.com/stregisatlanta"
      },
      {
        "name": "Loews Atlanta Hotel",
        "neighborhood": "Midtown",
        "brand": "Loews",
        "tier": "Upscale",
        "best_for": "Business travelers, convention attendees",
        "notes": "Connected to Georgia World Congress Center. Good for conferences.",
        "loyalty": "Loews You First",
        "website": "loewshotels.com/atlanta-hotel"
      }
    ],
    "transport": [
      {
        "name": "Atlanta Limousine & Transportation",
        "type": "Black Car / Limo",
        "notes": "Atlanta's most used executive car service. ATL airport specialists.",
        "website": "atlantalimousine.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Consistent for ATL transfers and multi-day executive bookings.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "App-based, professional. Good for ATL — one of the world's busiest airports.",
        "website": "blacklane.com"
      }
    ]
  },

  "Washington DC": {
    "restaurants": [
      {
        "name": "The Inn at Little Washington",
        "neighborhood": "Washington, VA (1 hour from DC)",
        "cuisine": "Contemporary American",
        "vibe": "Three Michelin stars. Patrick O'Connell's legendary inn. Worth the drive.",
        "best_for": "Ultimate VIP experience, celebrating landmark moments",
        "price": "$$$$",
        "private_dining": True,
        "notes": "One of the greatest restaurants in America. Reserve months ahead.",
        "reservations": "theinnatlittlewashington.com"
      },
      {
        "name": "Le Diplomate",
        "neighborhood": "14th Street / Logan Circle",
        "cuisine": "French Brasserie",
        "vibe": "DC's beloved French brasserie. Buzzy, excellent, great for extended lunches.",
        "best_for": "Political/media client lunches, power breakfasts",
        "price": "$$$",
        "private_dining": False,
        "notes": "DC institution. Book well ahead — always full.",
        "reservations": "lediplomatedc.com"
      },
      {
        "name": "Minibar",
        "neighborhood": "Penn Quarter",
        "cuisine": "Modern / Avant-garde",
        "vibe": "José Andrés's two Michelin-starred experience. Intimate, extraordinary.",
        "best_for": "Food-obsessed VIP clients, unforgettable experiences",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Ticketed reservations, 6-seat counter only. Book far in advance.",
        "reservations": "exploretock.com/minibar"
      },
      {
        "name": "The Hay-Adams Dining Room",
        "neighborhood": "Lafayette Square",
        "cuisine": "American / Contemporary",
        "vibe": "White House views. Incredibly elegant. A DC dining institution.",
        "best_for": "Government and lobbying client dinners, visiting dignitaries",
        "price": "$$$$",
        "private_dining": True,
        "notes": "White House views from top floor. Private dining available.",
        "reservations": "hayadams.com"
      }
    ],
    "hotels": [
      {
        "name": "The Hay-Adams",
        "neighborhood": "Lafayette Square / White House",
        "brand": "Independent",
        "tier": "Ultra-luxury",
        "best_for": "Government/political guests, White House proximity",
        "notes": "Views of the White House from upper floors. DC's most distinguished address.",
        "loyalty": "None (independent)",
        "website": "hayadams.com"
      },
      {
        "name": "Four Seasons Washington DC",
        "neighborhood": "Georgetown",
        "brand": "Four Seasons",
        "tier": "Ultra-luxury",
        "best_for": "Georgetown meetings, top executives",
        "notes": "DC's most celebrated hotel. Consistently exceptional service.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/washington"
      },
      {
        "name": "The Jefferson Washington DC",
        "neighborhood": "Downtown / K Street",
        "brand": "Independent",
        "tier": "Luxury",
        "best_for": "Boutique luxury, K Street proximity, political scene",
        "notes": "Intimate, elegant, historically detailed. Plume restaurant is excellent.",
        "loyalty": "None (independent)",
        "website": "jeffersondc.com"
      },
      {
        "name": "Mandarin Oriental Washington DC",
        "neighborhood": "Southwest Waterfront",
        "brand": "Mandarin Oriental",
        "tier": "Luxury",
        "best_for": "Conference attendees, waterfront location",
        "notes": "Near the Mall and Convention Center. Pool and spa.",
        "loyalty": "Fans of MO",
        "website": "mandarinoriental.com/washington-dc"
      }
    ],
    "transport": [
      {
        "name": "BrightStar Transportation",
        "type": "Black Car / Limo",
        "notes": "DC's premier executive car service. Government and corporate clients.",
        "website": "brightstardc.com"
      },
      {
        "name": "ETS International",
        "type": "Black Car / Limo",
        "notes": "Reliable for DCA, IAD, BWI airport transfers across the DC metro.",
        "website": "etslimo.com"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network. Consistent for government and lobbying clients.",
        "website": "carey.com"
      }
    ]
  },

  "Nashville": {
    "restaurants": [
      {
        "name": "The Catbird Seat",
        "neighborhood": "Midtown",
        "cuisine": "Modern American",
        "vibe": "32-seat chef's counter. One of the best dining experiences in the South.",
        "best_for": "Food-obsessed VIP clients, celebratory dinners",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Ticketed, prepaid. Book months out. Truly special experience.",
        "reservations": "exploretock.com/thecatbirdseat"
      },
      {
        "name": "The 404 Kitchen",
        "neighborhood": "The Gulch",
        "cuisine": "Contemporary European",
        "vibe": "Nashville's most critically acclaimed. Chef Matt Bolus, incredible food.",
        "best_for": "Executive client dinners, healthcare/music industry",
        "price": "$$$$",
        "private_dining": True,
        "notes": "James Beard nominee. Book 2-3 weeks out.",
        "reservations": "the404nashville.com"
      },
      {
        "name": "Bastion",
        "neighborhood": "Nations",
        "cuisine": "Modern American",
        "vibe": "Nashville's hottest creative restaurant. Behind a bar, intimate tasting menu.",
        "best_for": "Food-forward clients, creative industry executives",
        "price": "$$$",
        "private_dining": False,
        "notes": "Walk through the bar to get in. Worth every bit of effort.",
        "reservations": "exploretock.com/bastion"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Nashville",
        "neighborhood": "SoBro / Downtown",
        "brand": "Four Seasons",
        "tier": "Luxury",
        "best_for": "Business travelers, best service in Nashville",
        "notes": "Newest Four Seasons in the US. Stunning skyline views. Opened 2022.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/nashville"
      },
      {
        "name": "The Joseph",
        "neighborhood": "Downtown / Broadway",
        "brand": "Marriott / Autograph",
        "tier": "Luxury",
        "best_for": "Design-conscious travelers, art collectors",
        "notes": "Museum-quality art throughout. Rooftop pool. Walk to Broadway.",
        "loyalty": "Marriott Bonvoy",
        "website": "thejosephnashville.com"
      },
      {
        "name": "1 Hotel Nashville",
        "neighborhood": "SoBro",
        "brand": "1 Hotels",
        "tier": "Luxury",
        "best_for": "Sustainability-conscious executives, rooftop pool",
        "notes": "Biophilic design, reclaimed materials, incredible rooftop.",
        "loyalty": "SH Rewards",
        "website": "1hotels.com/nashville"
      }
    ],
    "transport": [
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Reliable for BNA airport transfers and executive transport.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "App-based, professional. Good for BNA runs.",
        "website": "blacklane.com"
      },
      {
        "name": "Music City Limo",
        "type": "Limo / Car Service",
        "notes": "Nashville-based fleet. Good for multi-stop executive days.",
        "website": "musiccitylimo.com"
      }
    ]
  },

  "Toronto": {
    "restaurants": [
      {
        "name": "Alo",
        "neighborhood": "Queen West",
        "cuisine": "French",
        "vibe": "Canada's best restaurant. Stunning tasting menu, intimate, flawless.",
        "best_for": "Top-tier VIP client dinners, visiting executives",
        "price": "$$$$",
        "private_dining": False,
        "notes": "Repeatedly ranked Canada's #1. Book months ahead.",
        "reservations": "aloresturant.ca"
      },
      {
        "name": "Canoe",
        "neighborhood": "Financial District",
        "cuisine": "Canadian / Contemporary",
        "vibe": "54 floors above Toronto. Spectacular views. Finance district power dining.",
        "best_for": "Bay Street client dinners, visiting international executives",
        "price": "$$$$",
        "private_dining": True,
        "notes": "Panoramic Toronto views. Private dining available. A Toronto institution.",
        "reservations": "canoerestaurant.com"
      },
      {
        "name": "Buca",
        "neighborhood": "King West / Yorkville",
        "cuisine": "Italian",
        "vibe": "Toronto's best Italian. Multiple locations, consistently excellent.",
        "best_for": "Business dinners, food-forward clients",
        "price": "$$$",
        "private_dining": True,
        "notes": "Book on OpenTable. Yorkville location most elegant.",
        "reservations": "buca.ca"
      }
    ],
    "hotels": [
      {
        "name": "Four Seasons Toronto",
        "neighborhood": "Yorkville",
        "brand": "Four Seasons",
        "tier": "Ultra-luxury",
        "best_for": "Top executives, best service in Toronto",
        "notes": "In Yorkville — Toronto's most prestigious neighborhood. Exceptional.",
        "loyalty": "Four Seasons Preferred Partner",
        "website": "fourseasons.com/toronto"
      },
      {
        "name": "The Ritz-Carlton Toronto",
        "neighborhood": "Entertainment District",
        "brand": "Marriott / Ritz-Carlton",
        "tier": "Ultra-luxury",
        "best_for": "Finance executives, TIFF film festival, downtown location",
        "notes": "Condo-hotel hybrid. Large suites. TIFF headquarters during festival.",
        "loyalty": "Marriott Bonvoy",
        "website": "ritzcarlton.com/toronto"
      },
      {
        "name": "Shangri-La Toronto",
        "neighborhood": "Financial District",
        "brand": "Shangri-La",
        "tier": "Luxury",
        "best_for": "Bay Street proximity, spa, contemporary luxury",
        "notes": "One of Toronto's finest. Bosk restaurant is excellent.",
        "loyalty": "Golden Circle",
        "website": "shangri-la.com/toronto"
      }
    ],
    "transport": [
      {
        "name": "Aerofleet",
        "type": "Black Car / Limo",
        "notes": "Toronto's premier executive car service. YYZ specialists.",
        "website": "aerofleet.ca"
      },
      {
        "name": "Carey International",
        "type": "Black Car / Limo",
        "notes": "Global network. Reliable for YYZ and downtown Toronto transport.",
        "website": "carey.com"
      },
      {
        "name": "Blacklane",
        "type": "Black Car / App",
        "notes": "App-based, professional. Good for YYZ airport transfers.",
        "website": "blacklane.com"
      }
    ]
  }

}


def build_guide(city: str, data: dict) -> dict:
    return {
        "city": city,
        "source": "Curated by Carrie AI — EA-vetted recommendations",
        "last_updated": UPDATED,
        "categories": data
    }


def save_guide(city: str, guide: dict) -> Path:
    slug = city.lower().replace(" ", "_").replace(",", "")
    path = GUIDES_DIR / f"{slug}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(guide, f, indent=2)
    return path


if __name__ == "__main__":
    print(f"Seeding {len(CITIES)} city guides...\n")
    for city, data in CITIES.items():
        guide = build_guide(city, data)
        path  = save_guide(city, guide)
        r = len(data.get("restaurants", []))
        h = len(data.get("hotels", []))
        t = len(data.get("transport", []))
        print(f"  ✓ {city:<20} — {r} restaurants, {h} hotels, {t} transport")
    print(f"\nAll guides saved to {GUIDES_DIR}")
