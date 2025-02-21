# Day 30: 21 Feb 2025

> if-else in navbar

- views.py of electronics app

    ```py
    def electro_home(request):
        context = {'electronics_nav': True}
        return render(request, 'electro_home.html', context)
    ```


- navbar.html (global navbar)

    ```django html
    {% if electronics_nav %}

            <nav style='background-color: rgb(96, 53, 53);'>
                <div class="logo">Electronics</div>
                <div class="links">
                    <a href="{% url 'home' %}">Home</a>
                    <a href="">Mobiles</a>
                    <a href="">Laptops</a>
                    <a href="">Watches</a>
                </div>
            </nav>

    {% else %}

            <nav>
                <div class="logo">Ecom</div>
                <div class="links">
                    <a href="{% url 'home' %}">Home</a>
                    <a href="{% url 'about' %}">About</a>
                    <a href="">Fruits</a>
                    <a href="">Sports</a>
                    <a href="{% url 'electro_home' %}">Electronics</a>
                </div>
            </nav>

    {% endif %}
    ```