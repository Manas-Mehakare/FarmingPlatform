from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms
from django.http import HttpResponseForbidden
from .forms import ProductForm
from django.contrib import messages

def home(request):
    return render(request, 'mainApp/home.html')

def about(request):
    return render(request, 'mainApp/about.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, "mainApp/product_list.html", {"products": products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        qty = int(request.POST.get("quantity"))
        
        # Check if requested quantity is available
        if qty > product.quantity:
            return render(request, "mainApp/product_detail.html", {
                "product": product,
                "error": f"Only {product.quantity} units available!"
            })
        
        buyer = Profile.objects.get(user=request.user)
        
        # Create order
        order = Order(
            product=product,
            buyer=buyer,
            quantity=qty,
        )
        order.save()  # ✅ triggers model's custom save() to calculate total_price correctly

        
        # Reduce product quantity
        product.quantity -= qty
        product.save()
        
        return render(request, "mainApp/order_success.html", {"order": order})

    return render(request, "mainApp/product_detail.html", {"product": product})




# Signup form
class SignUpForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('corporate', 'Corporate'),
    ]

    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            role = form.cleaned_data['role']
            Profile.objects.create(user=user, role=role)
            login(request, user)  # auto login after signup
            return redirect('product_list')
    else:
        form = SignUpForm()
    return render(request, 'mainApp/signup.html', {'form': form})

@login_required
def add_product(request):
    profile = Profile.objects.get(user=request.user)
    
    # Only farmers can add products
    if profile.role != "farmer":
        return HttpResponseForbidden("❌ Only farmers can add products.")
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = profile  # set seller as logged-in farmer
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, "mainApp/add_product.html", {"form": form})



@login_required
def farmer_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role != 'farmer':
        return HttpResponseForbidden("❌ Only farmers can access this page.")
    
    products = Product.objects.filter(seller=profile)
    return render(request, 'mainApp/farmer_dashboard.html', {'products': products})


@login_required
def edit_product(request, pk):
    profile = Profile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=pk, seller=profile)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('farmer_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'mainApp/edit_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, pk):
    profile = Profile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=pk, seller=profile)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('farmer_dashboard')

    return render(request, 'mainApp/delete_product.html', {'product': product})

@login_required
def farmer_orders(request):
    profile = Profile.objects.get(user=request.user)
    if profile.role != "farmer":
        return HttpResponseForbidden("❌ Only farmers can access this page.")

    # Orders for products that this farmer is selling
    orders = Order.objects.filter(product__seller=profile).select_related('product', 'buyer')
    return render(request, "mainApp/farmer_orders.html", {"orders": orders})

@login_required
def update_order_status(request, order_id):
    profile = Profile.objects.get(user=request.user)
    if profile.role != "farmer":
        return HttpResponseForbidden("❌ Only farmers can access this page.")

    order = get_object_or_404(Order, id=order_id, product__seller=profile)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in [Order.PENDING, 'shipping', Order.DELIVERED, Order.CANCELLED]:
            # Optional: map 'shipping' to 'confirmed' or create a new status
            if new_status == 'shipping':
                order.status = Order.SHIPPING  # or a separate SHIPPING status
            else:
                order.status = new_status
            order.save()
            messages.success(request, f"Order #{order.id} status updated!")
        return redirect('farmer_orders')

    return render(request, "mainApp/update_order_status.html", {"order": order})


@login_required
def corporate_orders(request):
    profile = Profile.objects.get(user=request.user)

    if profile.role != "corporate":
        return HttpResponseForbidden("❌ Only corporates can view this page.")

    orders = Order.objects.filter(buyer=profile).select_related("product")
    return render(request, "mainApp/corporate_orders.html", {"orders": orders})