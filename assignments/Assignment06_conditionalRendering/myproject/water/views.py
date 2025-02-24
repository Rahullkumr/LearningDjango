from django.shortcuts import render

# Create your views here.


def water_home(request):
    context = {'water_nav': True}
    return render(request, 'water_home.html', context)


def fish(request):
    fish_data = [
        {
            'name': 'Dolphin',
            'desc': 'A dolphin is an aquatic mammal in the clade Odontoceti (toothed whale). Dolphins belong to the families Delphinidae (the oceanic dolphins), Platanistidae (the Indian river dolphins), Iniidae (the New World river dolphins), Pontoporiidae (the brackish dolphins), and possibly extinct Lipotidae (baiji or Chinese river dolphin). There are 40 extant species named as dolphins.',
            'img_url': 'https://images.twinkl.co.uk/tw1n/image/private/t_630/u/ux/dolphin-2691864-1920_ver_1.jpg',
        },
        {
            'name': 'Whale',
            'desc': 'Whales are a widely distributed and diverse group of fully aquatic placental marine mammals. As an informal and colloquial grouping, they correspond to large members of the infraorder Cetacea, i.e. all cetaceans apart from dolphins and porpoises. Dolphins and porpoises may be considered whales from a formal, cladistic perspective.',
            'img_url': 'https://www.americanoceans.org/wp-content/uploads/2022/04/humpback-whale-megaptera-novaeangliae.jpg',
        },
        {
            'name': 'Gold fish',
            'desc': 'The goldfish is a freshwater fish in the family Cyprinidae of order Cypriniformes. It is commonly kept as a pet in indoor aquariums, and is one of the most popular aquarium fish. Goldfish released into the wild have become an invasive pest in parts of North America and Australia.',
            'img_url': 'https://static.vecteezy.com/system/resources/previews/033/360/572/non_2x/goldfish-the-sun-water-fish-fish-tank-hd-wallpaper-ai-generated-free-photo.jpg',
        },
    ]
    context = {'water_nav': True, 'fishes': fish_data}
    return render(request, 'fish.html', context)


def ship(request):
    ship_data = [
        {
            'name': 'Cargo Ship',
            'desc': 'A cargo ship is a large vessel designed to carry goods and commodities across oceans and seas. These ships are equipped with cargo holds or containers to store materials such as food, electronics, machinery, and raw materials. Cargo ships are crucial for global trade and come in various types, such as container ships, bulk carriers, and tankers.',
            'img_url': 'https://grist.org/wp-content/uploads/2021/03/Maersk-container-ship-e1614978284476.jpg',
        },
        {
            'name': 'Cruise Ship',
            'desc': 'A cruise ship is a passenger ship used for vacationing and leisure travel. These ships offer a variety of onboard amenities, such as restaurants, pools, entertainment venues, and sometimes even casinos. Cruise ships travel to popular tourist destinations, providing all-inclusive vacations with a focus on relaxation and recreation.',
            'img_url': 'https://www.cruisemapper.com/images/ships/2112-a46bd9fcc2b.jpg',
        },
        {
            'name': 'Naval Ship',
            'desc': 'A naval ship is a military vessel used by the navy to carry out defense and combat operations. These ships are equipped with advanced weaponry, radar systems, and are built for tactical operations in various environments. Naval ships come in different classes such as destroyers, frigates, aircraft carriers, and submarines, depending on their role in the fleet.',
            'img_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/INS_Imphal.jpg/1200px-INS_Imphal.jpg'
        },
    ]
    context = {'water_nav': True, 'ships': ship_data}
    return render(request, 'ship.html', context)


def yacht(request):
    yacht_data = [
        {
            'name': 'Luxury Superyacht',
            'desc': 'A luxury superyacht is a high-end, custom-built vessel designed for ultimate comfort and luxury. These yachts are often equipped with luxurious features such as helipads, swimming pools, spas, and cinema rooms. They can be used for both private and charter purposes, offering the epitome of maritime luxury.',
            'img_url': 'https://robbreport.com/wp-content/uploads/2019/07/adastra-1-courtesy-jochen-manz_orion-shuttleworth.jpg',
        },
        {
            'name': 'Sailing Yacht',
            'desc': 'A sailing yacht is a type of yacht powered primarily by sails. It is typically used for both recreation and competitive racing. Sailing yachts can range from smaller, more affordable vessels to large, sophisticated ships designed for long voyages. These yachts offer a more traditional form of cruising with a focus on wind-powered travel.',
            'img_url': 'https://photos.superyachtapi.com/download/276424/large'
        },
        {
            'name': 'Motor Yacht',
            'desc': 'A motor yacht is a type of yacht that relies on engines for propulsion. These yachts are often larger and faster than sailing yachts, offering a more luxurious experience with spacious decks, powerful engines, and various onboard amenities like jet skis and fully equipped kitchens. Motor yachts are ideal for those who prefer smooth, fast cruising.',
            'img_url': 'https://southernboating.com/wp-content/uploads/2017/10/Prestige_520-Jean-Marie_LIOT1_RT.jpg'
        },
    ]

    context = {'water_nav': True, 'yachts': yacht_data}
    return render(request, 'yacht.html', context)
