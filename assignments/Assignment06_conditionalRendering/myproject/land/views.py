from django.shortcuts import render

# Create your views here.


def land_home(request):
    context = {'land_nav': True}
    return render(request, 'land_home.html', context)


def tiger(request):
    tiger_data = [
        {
            'name': 'Bengal Tiger',
            'desc': 'The Bengal tiger is the most numerous tiger subspecies, found primarily in India, Bangladesh, and parts of Nepal and Bhutan. Known for their striking orange coat with black stripes, Bengal tigers are apex predators in their habitat, hunting large prey like deer, wild boar, and sometimes even water buffalo.',
            'img_url': 'https://www.theanimalfacts.com/wp-content/uploads/2020/11/Bengal-Tiger-2.jpg',
        },
        {
            'name': 'Siberian Tiger',
            'desc': 'The Siberian tiger, also known as the Amur tiger, is native to the forests of eastern Russia and parts of China. It is the largest of all tiger subspecies, with a thick, pale coat that helps it survive the cold, snowy climates. Siberian tigers primarily hunt large mammals like red deer and wild boar.',
            'img_url': 'https://petapixel.com/assets/uploads/2022/03/siberian-tiger-sighting-by-photographer-sascha-fonseca-1-800x572.jpg',
        },
        {
            'name': 'Sumatran Tiger',
            'desc': 'The Sumatran tiger is a critically endangered subspecies of tiger found only on the island of Sumatra in Indonesia. This smaller tiger is known for its beautiful, deep orange fur and dark black stripes. Sumatran tigers are primarily forest dwellers, preying on animals like deer, wild boar, and smaller mammals.',
            'img_url': 'https://files.worldwildlife.org/wwfcmsprod/images/30_Hills_Sumatran_tiger_resting_47149/story_full_width/63868cijym_3TigerPhoto.jpg',
        },
    ]

    context = {'land_nav': True, 'tigers': tiger_data}
    return render(request, 'tiger.html', context)


def bus(request):
    bus_data = [
        {
            'name': 'Electric Bus (High-Tech City)',
            'desc': 'Electric buses are eco-friendly public transport vehicles commonly used in modern, high-tech cities. They run on electric power, reducing greenhouse gas emissions and offering a quieter, cleaner ride. These buses are often part of a city’s push toward sustainability and smart city initiatives. They come equipped with modern amenities like Wi-Fi, USB charging ports, and air conditioning.',
            'img_url': 'https://th-i.thgim.com/public/business/f1pr2i/article68978145.ece/alternates/FREE_1200/SWITCH%20E1%20-%20Front3Qtr%201.jpg',
        },
        {
            'name': 'Double-Decker Bus',
            'desc': 'Double-decker buses are iconic in many older cities, especially in places like London. These buses have two levels, providing extra seating capacity, making them ideal for crowded urban environments. They are commonly used for both public transportation and sightseeing tours. The top deck provides panoramic views of the city, and the buses often have a vintage aesthetic in older cities.',
            'img_url': 'https://swarajya.gumlet.io/swarajya/2022-12/b586146c-b833-4051-a7a9-57d9941c2868/70079751_10156136369127134_3126094553438748672_n.jpg',
        },
        {
            'name': 'Indian Passenger Bus',
            'desc': 'Indian passenger buses are a vital mode of public transportation in India, serving both urban and rural areas. These buses come in various sizes, from smaller city buses to large intercity coaches, and are used for commuting, long-distance travel, and intercity routes. They are often equipped with features like air conditioning (in premium buses), overhead storage racks, and spacious seating for passengers. State-owned transport corporations and private operators manage most of the services. ',
            'img_url': 'https://c8.alamy.com/comp/DEN24J/overload-bus-in-rajasthan-india-DEN24J.jpg',
        },
    ]

    context = {'land_nav': True, 'buses': bus_data}
    return render(request, 'bus.html', context)


def train(request):
    train_data = [
        {
            'name': 'Bullet Train',
            'desc': 'Bullet trains, also known as Shinkansen in Japan, are high-speed trains that travel at speeds exceeding 186 mph (300 km/h). These trains are known for their aerodynamic design and punctuality. They connect major cities across countries like Japan, France, and China, providing an efficient alternative to air travel for short and medium distances.',
            'img_url': 'https://currentaffairs.adda247.com/wp-content/uploads/multisite/sites/5/2024/10/16131732/indias-first-bullet-train-244326817-16x9-1.jpg',
        },
        {
            'name': 'Freight Train',
            'desc': 'Freight trains are long trains designed to carry cargo rather than passengers. These trains are commonly used to transport goods such as coal, grain, shipping containers, and raw materials across long distances. Freight trains play a critical role in global trade and logistics, with large rail networks connecting industries to ports and cities.',
            'img_url': 'https://etvbharatimages.akamaized.net/etvbharat/prod-images/768-512-15489723-thumbnail-3x2-imgtrainnew.jpg',
        },
        {
            'name': 'Subway Train',
            'desc': 'Subway trains are rapid transit systems used in metropolitan areas to transport passengers quickly within cities. These trains typically run underground (though sometimes elevated) and are an essential part of public transportation in densely populated areas. Subway systems can be found in cities like New York, London, Tokyo, and Paris.',
            'img_url': 'https://www.madrid-traveller.com/wp-content/uploads/2020/04/madrid-subway.jpg',
        },
    ]

    context = {'land_nav': True, 'trains': train_data}
    return render(request, 'train.html', context)
