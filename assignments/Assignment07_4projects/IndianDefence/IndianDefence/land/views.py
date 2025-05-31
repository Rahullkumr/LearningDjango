from django.shortcuts import render

# Create your views here.


def tanks(request):
    tanks_data = [
        {
            "name": "Arjun Mk-1A",
            "origin": "India",
            "type": "Main Battle Tank (MBT)",
            "weight": "68.5 tons",
            "main_armament": "120mm rifled gun",
            "engine_power": "1,400 hp",
            "speed": "58 km/h",
            "range": "500 km"
        },
        {
            "name": "T-90 Bhishma",
            "origin": "Russia/India",
            "type": "Main Battle Tank (MBT)",
            "weight": "46.5 tons",
            "main_armament": "125mm smoothbore gun",
            "engine_power": "1,000 hp",
            "speed": "60 km/h",
            "range": "550 km"
        },
        {
            "name": "T-72 Ajeya",
            "origin": "Russia/India",
            "type": "Main Battle Tank (MBT)",
            "weight": "41 tons",
            "main_armament": "125mm smoothbore gun",
            "engine_power": "780 hp",
            "speed": "60 km/h",
            "range": "500 km"
        },
        {
            "name": "Arjun Mk-2",
            "origin": "India",
            "type": "Main Battle Tank (MBT)",
            "weight": "68 tons",
            "main_armament": "120mm rifled gun",
            "engine_power": "1,500 hp",
            "speed": "58 km/h",
            "range": "500 km"
        },
        {
            "name": "T-55",
            "origin": "Russia",
            "type": "Medium Tank",
            "weight": "36 tons",
            "main_armament": "100mm rifled gun",
            "engine_power": "580 hp",
            "speed": "50 km/h",
            "range": "500 km"
        },
        {
            "name": "BMP-2 Sarath",
            "origin": "Russia/India",
            "type": "Infantry Fighting Vehicle (IFV)",
            "weight": "14.3 tons",
            "main_armament": "30mm autocannon",
            "engine_power": "300 hp",
            "speed": "65 km/h",
            "range": "600 km"
        },
        {
            "name": "Nag Missile Carrier (NAMICA)",
            "origin": "India",
            "type": "Tank Destroyer",
            "weight": "14.5 tons",
            "main_armament": "Nag Anti-Tank Guided Missile (ATGM)",
            "engine_power": "300 hp",
            "speed": "65 km/h",
            "range": "600 km"
        }
    ]

    context = {'tanks': tanks_data}
    return render(request, 'land_html/tanks.html', context)


def land_missiles(request):
    lm_data = [
        {
            "name": "Prithvi I",
            "origin": "India",
            "type": "Short-Range Ballistic Missile (SRBM)",
            "range": "150 km",
            "payload": "1,000 kg",
            "propellant": "Liquid-fueled",
            "role": ["Tactical Missile", "Artillery Support"]
        },
        {
            "name": "Prithvi II",
            "origin": "India",
            "type": "Short-Range Ballistic Missile (SRBM)",
            "range": "250 km",
            "payload": "500-1,000 kg",
            "propellant": "Liquid-fueled",
            "role": ["Tactical Missile", "Artillery Support"]
        },
        {
            "name": "Agni I",
            "origin": "India",
            "type": "Medium-Range Ballistic Missile (MRBM)",
            "range": "700 km",
            "payload": "1,000 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        },
        {
            "name": "Agni II",
            "origin": "India",
            "type": "Medium-Range Ballistic Missile (MRBM)",
            "range": "2,000 km",
            "payload": "1,000 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        },
        {
            "name": "Agni III",
            "origin": "India",
            "type": "Intermediate-Range Ballistic Missile (IRBM)",
            "range": "3,000 km",
            "payload": "1,500 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        },
        {
            "name": "Agni IV",
            "origin": "India",
            "type": "Intermediate-Range Ballistic Missile (IRBM)",
            "range": "4,000 km",
            "payload": "1,000 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        },
        {
            "name": "Agni V",
            "origin": "India",
            "type": "Intercontinental Ballistic Missile (ICBM)",
            "range": "5,000+ km",
            "payload": "1,500 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        },
        {
            "name": "Dhanush",
            "origin": "India",
            "type": "Ship-to-Surface Ballistic Missile",
            "range": "350 km",
            "payload": "500-1,000 kg",
            "propellant": "Liquid-fueled",
            "role": ["Tactical Missile", "Naval Strike"]
        },
        {
            "name": "Nirbhay",
            "origin": "India",
            "type": "Subsonic Cruise Missile",
            "range": "1,000 km",
            "payload": "300 kg",
            "propellant": "Turbojet",
            "role": ["Ground Attack", "Precision Strike"]
        },
        {
            "name": "BrahMos",
            "origin": "India/Russia",
            "type": "Supersonic Cruise Missile",
            "range": "290 km",
            "payload": "200-300 kg",
            "propellant": "Solid-fueled",
            "role": ["Anti-Ship", "Anti-Surface", "Precision Strike"]
        },
        {
            "name": "Shaurya",
            "origin": "India",
            "type": "Subsurface-to-Surface Missile",
            "range": "750-1,000 km",
            "payload": "1,000 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        },
        {
            "name": "Sagarika",
            "origin": "India",
            "type": "Submarine-Launched Ballistic Missile (SLBM)",
            "range": "500 km",
            "payload": "1,000 kg",
            "propellant": "Solid-fueled",
            "role": ["Strategic Missile", "Nuclear Delivery"]
        }
    ]
    context = {'land_missiles': lm_data}
    return render(request, 'land_html/land_missiles.html', context)


def air_defence_sys(request):
    ads_data = [
        {
            "name": "Akash",
            "origin": "India",
            "type": "Surface-to-Air Missile (SAM) System",
            "range": "25-30 km",
            "altitude_range": "Up to 18,000 m",
            "role": ["Air Defense", "Anti-Aircraft", "Anti-Missile"],
            "missile_type": "Solid-fueled, Active Radar Homing"
        },
        {
            "name": "Barak 8",
            "origin": "India/Israel",
            "type": "Surface-to-Air Missile (SAM) System",
            "range": "70 km",
            "altitude_range": "Up to 16,000 m",
            "role": ["Air Defense", "Anti-Aircraft", "Anti-Missile"],
            "missile_type": "Solid-fueled, Active Radar Homing"
        },
        {
            "name": "Pechora",
            "origin": "Russia",
            "type": "Medium-Range Surface-to-Air Missile System",
            "range": "35-40 km",
            "altitude_range": "Up to 18,000 m",
            "role": ["Air Defense", "Anti-Aircraft"],
            "missile_type": "Command-guided, Solid-fueled"
        },
        {
            "name": "S-400 Triumf",
            "origin": "Russia",
            "type": "Long-Range Surface-to-Air Missile System",
            "range": "400 km",
            "altitude_range": "Up to 30,000 m",
            "role": ["Air Defense", "Anti-Missile", "Anti-Aircraft"],
            "missile_type": "Active Radar Homing, Solid-fueled"
        },
        {
            "name": "Crotale NG",
            "origin": "France",
            "type": "Short-Range Surface-to-Air Missile System",
            "range": "20-30 km",
            "altitude_range": "Up to 6,000 m",
            "role": ["Air Defense", "Anti-Aircraft"],
            "missile_type": "Infrared and Radar-guided"
        },
        {
            "name": "Igla-S",
            "origin": "Russia",
            "type": "Man-Portable Air Defense System (MANPADS)",
            "range": "5-6 km",
            "altitude_range": "Up to 3,500 m",
            "role": ["Air Defense", "Anti-Aircraft"],
            "missile_type": "Infrared Homing"
        },
        {
            "name": "SPYDER",
            "origin": "Israel",
            "type": "Surface-to-Air Missile (SAM) System",
            "range": "15-50 km",
            "altitude_range": "Up to 9,000 m",
            "role": ["Air Defense", "Anti-Aircraft"],
            "missile_type": "Infrared and Radar-guided"
        },
        {
            "name": "Advanced Air Defence (AAD)",
            "origin": "India",
            "type": "Surface-to-Air Missile (SAM) System",
            "range": "80 km",
            "altitude_range": "Up to 30,000 m",
            "role": ["Ballistic Missile Defense", "Air Defense"],
            "missile_type": "Active Radar Homing"
        },
        {
            "name": "Prithvi Air Defense (PAD)",
            "origin": "India",
            "type": "Ballistic Missile Defense System",
            "range": "80 km",
            "altitude_range": "Up to 50,000 m",
            "role": ["Ballistic Missile Defense", "Air Defense"],
            "missile_type": "Solid-fueled, Active Radar Homing"
        }
    ]
    context = {'air_defence_sys': ads_data}
    return render(request, 'land_html/ads.html', context)


def radars(request):
    radars_data = [
        {
            "name": "Arudhra",
            "origin": "India",
            "type": "3D Medium-Range Surveillance Radar",
            "range": "200 km",
            "frequency": "L-band",
            "role": ["Air Surveillance", "Missile Detection"]
        },

        {
            "name": "Revathi Radar",
            "origin": "India",
            "type": "3D Surveillance Radar",
            "range": "150 km",
            "frequency": "L-band",
            "role": ["Air Traffic Control", "Surveillance"]
        },
        {
            "name": "Shyam Radar",
            "origin": "India",
            "type": "Multi-Mode Radar",
            "range": "200 km",
            "frequency": "S-band",
            "role": ["Weather Monitoring", "Air Defense"]
        },
        {
            "name": "Rajendra Radar",
            "origin": "India",
            "type": "Multi-Function Phased Array Radar",
            "range": "150 km",
            "frequency": "S-band",
            "role": ["Air Defense", "Target Tracking", "Guidance for Surface-to-Air Missiles"]
        },
        {
            "name": "Swordfish Radar",
            "origin": "Israel",
            "type": "3D Air Surveillance Radar",
            "range": "200 km",
            "frequency": "S-band",
            "role": ["Air Surveillance", "Target Tracking"]
        },
        {
            "name": "Rohini Radar",
            "origin": "India",
            "type": "3D Surveillance Radar",
            "range": "250 km",
            "frequency": "L-band",
            "role": ["Air Defense", "Tracking Low-Altitude Targets"]
        },
        {
            "name": "Indra Radar",
            "origin": "India",
            "type": "3D Surveillance Radar",
            "range": "300 km",
            "frequency": "S-band",
            "role": ["Air Surveillance", "Missile Detection"]
        },
        {
            "name": "Green Pine Radar",
            "origin": "Israel",
            "type": "3D Long-Range Surveillance Radar",
            "range": "500 km",
            "frequency": "S-band",
            "role": ["Air Defense", "Ballistic Missile Detection"]
        },
        {
            "name": "Nuclear, Biological, and Chemical (NBC) Radar",
            "origin": "India",
            "type": "Detection Radar",
            "range": "Up to 20 km",
            "frequency": "Microwave",
            "role": ["Chemical and Biological Detection"]
        },
        {
            "name": "Thales Ground Master 400",
            "origin": "France",
            "type": "3D Long-Range Radar",
            "range": "400 km",
            "frequency": "S-band",
            "role": ["Air Surveillance", "Missile Detection", "Ground Target Surveillance"]
        },
        {
            "name": "EL/M-2084",
            "origin": "Israel",
            "type": "Multi-Function Radar",
            "range": "250 km",
            "frequency": "X-band",
            "role": ["Air Surveillance", "Target Tracking", "Ballistic Missile Defense"]
        }
    ]
    context = {'radars': radars_data}
    return render(request, 'land_html/radars.html', context)
