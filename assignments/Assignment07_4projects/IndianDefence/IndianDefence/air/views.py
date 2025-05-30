from django.shortcuts import render

# Create your views here.


def fighter_jets(request):
    fj_data = [
        {
            "name": "Sukhoi Su-30MKI",
            "origin": "Russia/India",
            "role": "Multirole Fighter",
            "speed": "Mach 2",
            "range": "3,000 km",
            "weapons": ["BrahMos-A", "Astra", "R-77", "KH-59"],
        },
        {
            "name": "Dassault Rafale",
            "origin": "France",
            "role": "Multirole Fighter",
            "speed": "Mach 1.8",
            "range": "3,700 km",
            "weapons": ["Meteor", "Scalp", "MICA", "Hammer"],
        },
        {
            "name": "HAL Tejas",
            "origin": "India",
            "role": "Light Combat Aircraft (LCA)",
            "speed": "Mach 1.6",
            "range": "1,850 km",
            "weapons": ["Astra", "Python-5", "Derby", "BrahMos-NG (planned)"],
        },
        {
            "name": "MiG-29UPG",
            "origin": "Russia",
            "role": "Air Superiority Fighter",
            "speed": "Mach 2.25",
            "range": "1,500 km",
            "weapons": ["R-77", "R-27", "Kh-31", "R-73"],
        },
        {
            "name": "Mirage-2000",
            "origin": "France",
            "role": "Multirole Fighter",
            "speed": "Mach 2.2",
            "range": "1,550 km",
            "weapons": ["MICA", "ASRAAM", "Hammer", "SCALP"],
        },
        {
            "name": "MiG-21 Bison",
            "origin": "Russia",
            "role": "Interceptor / Fighter",
            "speed": "Mach 2.05",
            "range": "1,210 km",
            "weapons": ["R-73", "R-77", "S-24 Rockets"],
        },
    ]
    context = {'fighter_jets': fj_data}
    return render(request, 'air_html/fighter_jets.html', context)


def air_missiles(request):
    am_data = [
        {
            "name": "Akash",
            "origin": "India",
            "type": "Medium-Range Surface-to-Air Missile (SAM)",
            "range": "30 km",
            "speed": "Mach 2.5",
            "warhead": "High-Explosive",
        },
        {
            "name": "Barak-8",
            "origin": "India/Israel",
            "type": "Medium-Range Surface-to-Air Missile (SAM)",
            "range": "90 km",
            "speed": "Mach 2",
            "warhead": "High-Explosive Fragmentation",
        },
        {
            "name": "SPYDER",
            "origin": "Israel",
            "type": "Short-to-Medium Range Surface-to-Air Missile (SAM)",
            "range": "15-35 km",
            "speed": "Mach 4",
            "warhead": "High-Explosive",
        },
        {
            "name": "Prithvi Air Defense (PAD)",
            "origin": "India",
            "type": "Anti-Ballistic Missile (ABM)",
            "range": "80 km",
            "speed": "Mach 5",
            "warhead": "Kinetic Kill",
        },
        {
            "name": "BrahMos",
            "origin": "India/Russia",
            "type": "Supersonic Cruise Missile",
            "range": "450-800 km",
            "speed": "Mach 3",
            "warhead": "High-Explosive Penetration",
        },
        {
            "name": "Astra",
            "origin": "India",
            "type": "Beyond Visual Range (BVR) Air-to-Air Missile",
            "range": "110 km",
            "speed": "Mach 4.5",
            "warhead": "High-Explosive",
        },
        {
            "name": "Rudram-1",
            "origin": "India",
            "type": "Anti-Radiation Missile (ARM)",
            "range": "150 km",
            "speed": "Mach 2",
            "warhead": "High-Explosive",
        },
        {
            "name": "Nag Missile (Helina Variant)",
            "origin": "India",
            "type": "Helicopter-Launched Anti-Tank Guided Missile (ATGM)",
            "range": "7 km",
            "speed": "Mach 1.3",
            "warhead": "Tandem High-Explosive Anti-Tank",
        }
    ]
    context = {'air_missiles': am_data}
    return render(request, 'air_html/air_missiles.html', context)


def drones(request):
    drones_data = [
        {
            "name": "Rustom-2 (TAPAS-BH)",
            "origin": "India",
            "type": "Medium-Altitude Long-Endurance (MALE) UAV",
            "range": "1,000 km",
            "endurance": "18 hours",
            "role": ["Reconnaissance", "Surveillance", "Target Acquisition"],
        },
        {
            "name": "Heron TP",
            "origin": "Israel",
            "type": "Medium-Altitude Long-Endurance (MALE) UAV",
            "range": "1,500 km",
            "endurance": "36 hours",
            "role": ["Reconnaissance", "Surveillance", "Combat (armed variant)"],
        },
        {
            "name": "Harop",
            "origin": "Israel",
            "type": "Loitering Munition (Kamikaze Drone)",
            "range": "1,000 km",
            "endurance": "9 hours",
            "role": ["Precision Strike", "SEAD"],
        },
        {
            "name": "Ghatak UCAV",
            "origin": "India",
            "type": "Stealth Unmanned Combat Aerial Vehicle (UCAV)",
            "range": "Unknown",
            "endurance": "Unknown",
            "role": ["Autonomous Combat Missions", "Stealth Airstrikes"],
        },
        {
            "name": "Raven RQ-11",
            "origin": "USA",
            "type": "Small Hand-Launched UAV",
            "range": "10 km",
            "endurance": "90 minutes",
            "role": ["Short-Range Surveillance"],
        },
        {
            "name": "Searcher Mk II",
            "origin": "Israel",
            "type": "Short-Range UAV",
            "range": "200 km",
            "endurance": "18 hours",
            "role": ["Reconnaissance", "Target Acquisition"],
        },
        {
            "name": "Nishant",
            "origin": "India",
            "type": "Short-Range UAV",
            "range": "160 km",
            "endurance": "4.5 hours",
            "role": ["Surveillance", "Target Tracking"],
        },
        {
            "name": "DRDO Lakshya",
            "origin": "India",
            "type": "Target Drone",
            "range": "150 km",
            "endurance": "30 minutes",
            "role": ["Target Practice", "Missile Testing"],
        },
        {
            "name": "DRDO Abhyas",
            "origin": "India",
            "type": "High-Speed Expendable Aerial Target (HEAT)",
            "range": "400 km",
            "endurance": "30 minutes",
            "role": ["Target Training", "Missile Testing"],
        }
    ]
    context = {'drones': drones_data}
    return render(request, 'air_html/drones.html', context)


def helicopters(request):
    helicopters_data = [
        {
            "name": "HAL Dhruv",
            "origin": "India",
            "type": "Utility Helicopter",
            "speed": "290 km/h",
            "range": "630 km",
            "role": ["Transport", "Reconnaissance", "Medical Evacuation"],
        },
        {
            "name": "HAL Prachand (LCH)",
            "origin": "India",
            "type": "Attack Helicopter",
            "speed": "268 km/h",
            "range": "550 km",
            "role": ["Close Air Support", "Anti-Tank Warfare"],
            "weapons": ["Mistral ATAM", "Helina ATGM", "Rockets"],
        },
        {
            "name": "HAL Rudra",
            "origin": "India",
            "type": "Armed Helicopter",
            "speed": "290 km/h",
            "range": "700 km",
            "role": ["Attack", "Reconnaissance"],
            "weapons": ["Helina ATGM", "Rockets", "Machine Guns"],
        },
        {
            "name": "AH-64E Apache",
            "origin": "USA",
            "type": "Attack Helicopter",
            "speed": "293 km/h",
            "range": "476 km",
            "role": ["Close Air Support", "Anti-Armor"],
            "weapons": ["Hellfire Missiles", "Hydra Rockets", "30mm Chain Gun"],
        },
        {
            "name": "Mi-35",
            "origin": "Russia",
            "type": "Attack Helicopter",
            "speed": "310 km/h",
            "range": "450 km",
            "role": ["Close Air Support", "Transport"],
            "weapons": ["Rocket Pods", "Anti-Tank Missiles"],
        },
        {
            "name": "Mi-17 V5",
            "origin": "Russia",
            "type": "Transport Helicopter",
            "speed": "250 km/h",
            "range": "580 km",
            "role": ["Troop Transport", "Rescue Operations"],
        },
        {
            "name": "Kamov Ka-31",
            "origin": "Russia",
            "type": "Airborne Early Warning Helicopter",
            "speed": "250 km/h",
            "range": "600 km",
            "role": ["Surveillance", "Early Warning"],
        },
        {
            "name": "CH-47F Chinook",
            "origin": "USA",
            "type": "Heavy-Lift Helicopter",
            "speed": "315 km/h",
            "range": "741 km",
            "role": ["Heavy Transport", "Logistics"],
        },
        {
            "name": "HAL Chetak",
            "origin": "India/France",
            "type": "Light Utility Helicopter",
            "speed": "220 km/h",
            "range": "500 km",
            "role": ["Transport", "Rescue", "Surveillance"],
        },
        {
            "name": "HAL Cheetah",
            "origin": "India/France",
            "type": "Light Utility Helicopter",
            "speed": "220 km/h",
            "range": "600 km",
            "role": ["High-Altitude Operations", "Reconnaissance"],
        },
        {
            "name": "Sikorsky MH-60R Romeo",
            "origin": "USA",
            "type": "Naval Multi-Role Helicopter",
            "speed": "270 km/h",
            "range": "830 km",
            "role": ["Anti-Submarine Warfare", "Reconnaissance"],
        }
    ]
    context = {'helicopters': helicopters_data}
    return render(request, 'air_html/helicopters.html', context)
