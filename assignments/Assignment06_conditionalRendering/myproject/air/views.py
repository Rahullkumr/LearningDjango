from django.shortcuts import render

# Create your views here.


def air_home(request):
    context = {'air_nav': True}
    return render(request, 'air_home.html', context)


def birds(request):
    bird_data = [
        {
            'name': 'Eagle',
            'desc': 'Eagles are large birds of prey known for their powerful build, keen eyesight, and sharp talons. They are found in a wide range of habitats, including forests, mountains, and coastal regions. Eagles primarily hunt fish, small mammals, and other birds. They are often symbols of strength and freedom in many cultures.',
            'img_url': 'https://abcbirds.org/wp-content/uploads/2015/03/Golden-Eagle_Jesus-Giraldo-Gutierrez-Shutterstock-1024x663.jpg',
        },
        {
            'name': 'Parrot',
            'desc': 'Parrots are colorful, intelligent birds found in tropical and subtropical regions around the world. They are known for their ability to mimic human speech and other sounds. Parrots have strong beaks and zygodactyl feet that help them climb and hold onto branches. Many species of parrots are popular pets due to their vibrant plumage and playful nature.',
            'img_url': 'https://d2zp5xs5cp8zlg.cloudfront.net/image-85281-800.jpg',
        },
        {
            'name': 'Penguin',
            'desc': 'Penguins are flightless birds that are well adapted to life in cold climates. They have a unique body shape that allows them to swim effectively in water. Penguins are primarily found in the Southern Hemisphere, with many species inhabiting Antarctica. They are known for their tuxedo-like black-and-white plumage and their waddling walk on land.',
            'img_url': 'https://cdn.download.ams.birds.cornell.edu/api/v2/asset/612763581/900',
        },
    ]

    context = {'air_nav': True, 'birds': bird_data}
    return render(request, 'birds.html', context)


def helicopter(request):
    helicopter_data = [
        {
            'name': 'Attack Helicopter',
            'desc': 'An attack helicopter is a type of military helicopter designed for ground-attack missions. These helicopters are equipped with advanced weaponry, such as guided missiles, rockets, and machine guns, and are often used to support infantry, destroy tanks, or target enemy forces. Popular models include the Apache AH-64 and the Mil Mi-24.',
            'img_url': 'https://bsmedia.business-standard.com/_media/bs/img/article/2023-05/29/full/1685342425-94.jpg',
        },
        {
            'name': 'Transport Helicopter',
            'desc': 'A transport helicopter is designed to carry troops, equipment, or supplies to and from various locations, often in rugged or inaccessible areas. These helicopters can carry large loads and are used by both military and civilian organizations. The CH-47 Chinook is a well-known example of a heavy-lift transport helicopter.',
            'img_url': 'https://armyrecognition.com/images/stories/news/2022/april/US_Marine_Corps_declares_Initial_Operational_Capability_of_Sikorsky_CH-53K.jpg',
        },
        {
            'name': 'Rescue Helicopter',
            'desc': 'Rescue helicopters are specially equipped helicopters used in emergency situations to provide search and rescue services. These helicopters are often equipped with hoists, winches, and medical equipment to assist in saving lives. They are used for evacuating people from hazardous locations, such as mountain rescues, offshore oil rigs, or disaster zones.',
            'img_url': 'https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/20/2015/04/LR099-EOB-Highline-LM.jpg',
        },
    ]

    context = {'air_nav': True, 'helicopters': helicopter_data}
    return render(request, 'helicopter.html', context)


def aeroplane(request):
    airplane_data = [
        {
            'name': 'Commercial Airliner',
            'desc': 'Commercial airliners are large aircraft designed to carry passengers and cargo over long distances. These airplanes are used by airlines for regular scheduled flights and can accommodate hundreds of passengers. Popular examples include the Boeing 737, Airbus A320, and Boeing 777. They are designed for comfort, efficiency, and safety on international and domestic routes.',
            'img_url': 'https://www.financialexpress.com/wp-content/uploads/2023/02/Air-India-Reuters-1.jpg',
        },
        {
            'name': 'Private Jet',
            'desc': 'Private jets are small, luxury aircraft designed for personal or business use. These jets are often used by wealthy individuals, corporations, or government officials to travel quickly and privately. They offer luxurious interiors with amenities such as reclining seats, Wi-Fi, and sometimes even bedrooms. Popular models include the Gulfstream G650 and Bombardier Global 7500.',
            'img_url': 'https://www.claylacy.com/wp-content/uploads/2018/07/Gulfstream-GIV-Exterior-Sunset.jpg',
        },
        {
            'name': 'Cargo Airplane',
            'desc': 'Cargo airplanes are specialized aircraft used for transporting goods, rather than passengers. These planes are designed with large cargo holds and can carry a wide range of freight, including heavy machinery, vehicles, and perishable goods. They play a key role in global trade and logistics, with popular models like the Boeing 747 Freighter and Airbus A330 Freighter.',
            'img_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/C5_galaxy.jpg/1200px-C5_galaxy.jpg',
        },
    ]

    context = {'air_nav': True, 'airplanes': airplane_data}
    return render(request, 'aeroplane.html', context)
