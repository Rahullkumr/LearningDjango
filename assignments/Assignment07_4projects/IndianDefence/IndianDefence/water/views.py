from django.shortcuts import render

# Create your views here.


def submarines(request):
    submarines_data = [
        {
            "name": "INS Arihant",
            "origin": "India",
            "type": "Nuclear-Powered Ballistic Missile Submarine (SSBN)",
            "displacement": "6,000 tons",
            "length": "112 meters",
            "depth": "Up to 300 meters",
            "speed": "18 knots",
            "armament": ["K-15 Sagarika Missile", "K-4 Missile"],
        },
        {
            "name": "INS Arighat",
            "origin": "India",
            "type": "Nuclear-Powered Ballistic Missile Submarine (SSBN)",
            "displacement": "6,000 tons",
            "length": "112 meters",
            "depth": "Up to 300 meters",
            "speed": "18 knots",
            "armament": ["K-4 Missile", "K-15 Sagarika Missile"],
        },
        {
            "name": "INS Chakra",
            "origin": "Russia/India",
            "type": "Nuclear-Powered Attack Submarine (SSN)",
            "displacement": "12,000 tons",
            "length": "130 meters",
            "depth": "Up to 600 meters",
            "speed": "30 knots",
            "armament": ["Torpedoes", "Cruise Missiles"],
        },
        {
            "name": "INS Kilo (Sindhughosh Class)",
            "origin": "Russia",
            "type": "Diesel-Electric Attack Submarine",
            "displacement": "3,000 tons",
            "length": "72 meters",
            "depth": "Up to 300 meters",
            "speed": "18 knots",
            "armament": ["Torpedoes", "Cruise Missiles"],
        },
        {
            "name": "INS Kalvari (Scorpène Class)",
            "origin": "France",
            "type": "Diesel-Electric Attack Submarine",
            "displacement": "1,565 tons",
            "length": "67.5 meters",
            "depth": "Up to 300 meters",
            "speed": "20 knots",
            "armament": ["Torpedoes", "Exocet Missiles"],
        },
        {
            "name": "INS Vela (Scorpène Class)",
            "origin": "France",
            "type": "Diesel-Electric Attack Submarine",
            "displacement": "1,565 tons",
            "length": "67.5 meters",
            "depth": "Up to 300 meters",
            "speed": "20 knots",
            "armament": ["Torpedoes", "Exocet Missiles"],
        },
        {
            "name": "INS Vagli (Scorpène Class)",
            "origin": "France",
            "type": "Diesel-Electric Attack Submarine",
            "displacement": "1,565 tons",
            "length": "67.5 meters",
            "depth": "Up to 300 meters",
            "speed": "20 knots",
            "armament": ["Torpedoes", "Exocet Missiles"],
        },
        {
            "name": "INS Khanderi (Scorpène Class)",
            "origin": "France",
            "type": "Diesel-Electric Attack Submarine",
            "displacement": "1,565 tons",
            "length": "67.5 meters",
            "depth": "Up to 300 meters",
            "speed": "20 knots",
            "armament": ["Torpedoes", "Exocet Missiles"],
        },
    ]
    context = {'submarines': submarines_data}
    return render(request, 'water_html/submarines.html', context)


def aircraft_carriers(request):
    ac_data = [
        {
            "name": "INS Vikramaditya",
            "origin": "Russia/India",
            "type": "Multi-role Aircraft Carrier",
            "displacement": "45,000 tons",
            "length": "284 meters",
            "speed": "30 knots",
            "aircraft_capacity": "30-40 aircraft",
            "role": ["Power Projection", "Air Superiority", "Sea Control"]
        },
        {
            "name": "INS Vikrant",
            "origin": "India",
            "type": "Indigenous Aircraft Carrier",
            "displacement": "40,000 tons",
            "length": "262 meters",
            "speed": "28 knots",
            "aircraft_capacity": "30 aircraft",
            "role": ["Power Projection", "Air Superiority", "Sea Control"]
        },
        {
            "name": "INS Viraat",
            "origin": "UK/India",
            "type": "Centaur-Class Aircraft Carrier",
            "displacement": "28,700 tons",
            "length": "226 meters",
            "speed": "28 knots",
            "aircraft_capacity": "26 aircraft",
            "role": ["Power Projection", "Air Superiority", "Sea Control"],
        }
    ]
    context = {'aircraft_carriers': ac_data}
    return render(request, 'water_html/ac.html', context)


def destroyers(request):
    destroyers_data = [
        {
            "name": "INS Kolkata",
            "origin": "India",
            "type": "Kolkata-Class Guided Missile Destroyer",
            "displacement": "7,500 tons",
            "length": "163 meters",
            "speed": "30 knots",
            "armament": ["BrahMos Cruise Missile", "Barak-8 SAM", "Heavy Torpedoes", "Close-in Weapon System"],
        },
        {
            "name": "INS Kochi",
            "origin": "India",
            "type": "Kolkata-Class Guided Missile Destroyer",
            "displacement": "7,500 tons",
            "length": "163 meters",
            "speed": "30 knots",
            "armament": ["BrahMos Cruise Missile", "Barak-8 SAM", "Heavy Torpedoes", "Close-in Weapon System"],
        },
        {
            "name": "INS Chennai",
            "origin": "India",
            "type": "Kolkata-Class Guided Missile Destroyer",
            "displacement": "7,500 tons",
            "length": "163 meters",
            "speed": "30 knots",
            "armament": ["BrahMos Cruise Missile", "Barak-8 SAM", "Heavy Torpedoes", "Close-in Weapon System"],
        },
        {
            "name": "INS Ranjit",
            "origin": "India",
            "type": "Rajput-Class Destroyer",
            "displacement": "6,500 tons",
            "length": "154 meters",
            "speed": "30 knots",
            "armament": ["Sunburn Anti-Ship Missile", "Shtil-1 SAM", "Torpedoes"],
        },
        {
            "name": "INS Ranvijay",
            "origin": "India",
            "type": "Rajput-Class Destroyer",
            "displacement": "6,500 tons",
            "length": "154 meters",
            "speed": "30 knots",
            "armament": ["Sunburn Anti-Ship Missile", "Shtil-1 SAM", "Torpedoes"],
        }
    ]

    context = {'destroyers': destroyers_data}
    return render(request, 'water_html/destroyers.html', context)


def frigates(request):
    frigates_data = [
        {
            "name": "INS Shivalik",
            "origin": "India",
            "type": "Shivalik-Class Stealth Frigate",
            "displacement": "6,200 tons",
            "length": "142 meters",
            "speed": "30 knots",
            "armament": ["BrahMos Cruise Missile", "Surface-to-Air Missiles", "Torpedoes", "R-77 Missiles"],
        },
        {
            "name": "INS Satpura",
            "origin": "India",
            "type": "Shivalik-Class Stealth Frigate",
            "displacement": "6,200 tons",
            "length": "142 meters",
            "speed": "30 knots",
            "armament": ["BrahMos Cruise Missile", "Surface-to-Air Missiles", "Torpedoes"],
        },
        {
            "name": "INS Sahyadri",
            "origin": "India",
            "type": "Shivalik-Class Stealth Frigate",
            "displacement": "6,200 tons",
            "length": "142 meters",
            "speed": "30 knots",
            "armament": ["BrahMos Cruise Missile", "Surface-to-Air Missiles", "Torpedoes"],
        },
        {
            "name": "INS Talwar",
            "origin": "Russia",
            "type": "Talwar-Class Frigate",
            "displacement": "4,000 tons",
            "length": "124 meters",
            "speed": "30 knots",
            "armament": ["Kh-35 Anti-Ship Missiles", "Surface-to-Air Missiles", "Torpedoes"],
        },
        {
            "name": "INS Trikand",
            "origin": "Russia",
            "type": "Talwar-Class Frigate",
            "displacement": "4,000 tons",
            "length": "124 meters",
            "speed": "30 knots",
            "armament": ["Kh-35 Anti-Ship Missiles", "Surface-to-Air Missiles", "Torpedoes"],
        }
    ]

    context = {'frigates': frigates_data}
    return render(request, 'water_html/frigates.html', context)
