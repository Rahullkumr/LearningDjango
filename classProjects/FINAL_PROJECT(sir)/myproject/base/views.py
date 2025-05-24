from django.shortcuts import redirect, render
from .models import Products,CartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        cartproductscount=CartModel.objects.filter(host=request.user).count()
    else:
        cartproductscount=False

    
    trend=False
    offer=False

    if 'q' in request.GET:
        q=request.GET['q']
        all_products=Products.objects.filter(Q(pname__icontains=q)|Q(pdesc__icontains=q))  
    elif 'cat' in request.GET:
        cat=request.GET['cat'] 
        all_products=Products.objects.filter(pcategory=cat)  
    elif 'trending' in request.GET:
        all_products=Products.objects.filter(trending=1)
        trend=True  
    elif 'offer' in request.GET:
        all_products=Products.objects.filter(offer=1)
        offer=True  
    else:
        all_products=Products.objects.all()

    category=[]
    for i in Products.objects.all():
        if i.pcategory not in category:
            category+=[i.pcategory]

    return render(request,'home.html',{'all_products':all_products,'category':category,'trend':trend,'offer':offer,'cartproductscount':cartproductscount})

@login_required(login_url='login_')
def cart(request):
    cartproductscount=CartModel.objects.filter(host=request.user).count()
    cartproducts=CartModel.objects.filter(host=request.user)
    TA=0
    for i in cartproducts:
        print(i.totalprice)
        TA+=i.totalprice
    print(TA)
    return render(request,'cart.html',{'cartproducts':cartproducts,'TA':TA,'profile_nav':True,'cartproductscount':cartproductscount})

@login_required(login_url='login_')
def addtocart(request,pk):
    product=Products.objects.get(id=pk)

    try:
        cp=CartModel.objects.get(pname=product.pname,host=request.user)
        cp.quatity+=1
        cp.totalprice+=product.price
        cp.save()
        return redirect(cart)
    except:
        CartModel.objects.create(
            pname=product.pname,
            price=product.price,
            pcategory=product.pcategory,
            quatity=1,
            totalprice=product.price,
            host=request.user
        )
        return redirect(cart)

@login_required(login_url='login_')
def remove(request,pk):
    cartproduct=CartModel.objects.get(id=pk)
    cartproduct.delete()
    return redirect('cart')

