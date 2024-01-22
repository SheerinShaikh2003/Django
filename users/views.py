from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from users.models import CusOrders, CusRatingFeedback
from users.forms import CusOrdersUpd, CusRatFeedForm,UserProfileForm
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from food.models import Item
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'Welcome {}, your account has been successfully created'.format(username))
            form.save()
            return redirect('login')
        
    else:
        form = RegisterForm()
        
        context = {
            'form': form
        }
      
    return render(request, 'users/register.html', context)

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:

            messages.success(
                request,
                'Invalid Login, Please Try Again'
            )
            return redirect('login')
        elif user.is_superuser:
            login(request, user)
            messages.success(
                request,
                'Welcome Superuser {}, you have been successfully logged in.'.format(request.user.username)
            )
            return redirect('food:index')

        elif user is not None:
            login(request, user)
            messages.success(
                request,
                'Welcome {}, you have been successfully logged in.'.format(request.user.username)
            )
            return redirect('food:index')
        

        
    return render(request, 'users/login.html')


def logout_view(request):
    messages.success(
        request,
        '{}, You have successfully logged out'.format(request.user.username)
    )
    logout(request)
    return redirect ('food:index')


@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

def Orders(request, id, pdcd, user):
    
    
    context = {
        'pdcd': pdcd,
        'user': user,
    }
    
    if request.method == 'POST':
        item = Item.objects.get(prod_code=pdcd)

       
        
        Obj_CusOrds = CusOrders(
             prod_code=pdcd,
             user=user,
             quantity=request.POST.get('qty'),
        )
        
        Obj_CusOrds.save()
        
        send_mail(
            "Your Order has been successfully placed",
            f"Dear {Obj_CusOrds.user},\n\n"
            f"Your order #{Obj_CusOrds.order_id} has been successfully placed!\n"                    
            f"Here are the details:\n"
            f"- Item Name: {item.item_name}\n"
            f"- Quantity: {Obj_CusOrds.quantity}\n"
            f"- Price: ₹{item.item_price}\n\n"
            f"Thank you for your purchase!",
            "shaikhsheerin77@gmail.com",
            ["shaikhsheerin77@gmail.com"],
            fail_silently=False,
        )
        return redirect ('food:detail', item_id=id)
    
    return render(request, 'users/orders.html', context)

def update_orders(request, id, upd_order_id):
    #customer order object
    coo = CusOrders.objects.get(order_id=upd_order_id)
    form = CusOrdersUpd(request.POST or None, instance=coo)
    
    context = {
        'form':form
    }
    
    if request.method == 'POST':
        form.instance.order_id = coo.order_id
        form.instance.prod_code = coo.prod_code
        form.instance.user = request.user.username
        form.save()
        return redirect ('food:detail', item_id=id)
    
    return render(request,'users/orders_upd.html', context)

def delete_order(request, item_id, order_id):
    # Get the order object
    order = get_object_or_404(CusOrders, order_id=order_id)

    # Check if the user has the permission to delete the order
    if request.user.profile.user_type == 'Cust' and request.user.username == order.user:
        # Delete the order
        order.delete()
        return redirect('food:detail', item_id=item_id)
    else:
        # If the user does not have permission, you may want to handle this case appropriately,
        # such as showing an error message or redirecting to a different page.
        return redirect('food:detail', item_id=item_id)

def CusRatFeed(request, it_id, pc):
    
    form = CusRatFeedForm(request.POST or None)
    
    context = {
        'form':form
    }
    
    if request.method == 'POST':
        form.instance.prod_code = pc
        form.instance.username = request.user.username
        form.save()
        return redirect ('food:detail', item_id=it_id)
    
    return render(request,'users/item-form.html', context)


def update_crf(request, details_id, crf_id):

    crfo = CusRatingFeedback.objects.get(pk=crf_id)
    form = CusRatFeedForm(request.POST or None, instance=crfo)

    context = {
        'form':form
    }

    if form.is_valid():
        form.save()
        return redirect('food:detail', item_id=details_id)

    return render(request, 'users/crf_upd.html', context)


def delete_crf(request, details_id, crf_id):

    crfo = CusRatingFeedback.objects.get(pk=crf_id)

    context = {
        'crfo':crfo
    }

    if request.method == 'POST':
        crfo.delete()
        return redirect('food:detail', item_id=details_id)

    return render(request, 'users/crf_del.html', context)

def Payment(request, amt, qty):
    
    context = {
        'amt': amt,
        'qty': qty,
        'tot': amt * qty
    }
    
    return render(request, 'users/payment.html', context)


def OnApprove(request):
    
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        
        context = {
            
        }
        
        return JsonResponse(context)
    
    
def PaymentSuccess(request):
    
    return render(request, 'users/pymtsuccess.html')




def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('users:edit_profile')
        else:
            messages.error(request, 'Error updating profile. Please correct the errors.')

    else:
        form = UserProfileForm(instance=user.profile)

    return render(request, 'users/edit_profile.html', {'form': form})
