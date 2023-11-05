import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .models import Account, Address
from .forms import AccountForm, AccountAddForm, AddressForm


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            user = auth.authenticate(email=email, password=password)

            if user is not None:
                # try:
                #     cart = Cart.objects.get(cart_id=_cart_id(request))
                #     is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                #     if is_cart_item_exists:
                #         cart_item = CartItem.objects.filter(cart=cart)
                #
                #         # Getting the product variations by cart id
                #         product_variation = []
                #         for item in cart_item:
                #             variation = item.variations.all()
                #             product_variation.append(list(variation))
                #
                #         # Get the cart items from the user to access his product variations
                #         cart_item = CartItem.objects.filter(user=user)
                #         ex_var_list = []
                #         id = []
                #         for item in cart_item:
                #             existing_variation = item.variations.all()
                #             ex_var_list.append(list(existing_variation))
                #             id.append(item.id)
                #
                #         # product_variation = [1, 2, 3, 4, 6]
                #         # ex_var_list = [4, 6, 3, 5]
                #
                #         for pr in product_variation:
                #             if pr in ex_var_list:
                #                 index = ex_var_list.index(pr)
                #                 item_id = id[index]
                #                 item = CartItem.objects.get(id=item_id)
                #                 item.quantity += 1
                #                 item.user = user
                #                 item.save()
                #             else:
                #                 cart_item = CartItem.objects.filter(cart=cart)
                #                 for item in cart_item:
                #                     item.user = user
                #                     item.save()
                # except:
                #     pass
                auth.login(request, user)
                messages.success(request, 'You are now logged in.')
                url = request.META.get('HTTP_REFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    # next=/cart/checkout/
                    params = dict(x.split('=') for x in query.split('&'))
                    if 'next' in params:
                        nextPage = params['next']
                        return redirect(nextPage)
                except:
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        return render(request, 'fe/accounts/login.html')


@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'be/pages/dashboard.html', context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, _('You are logged out successfully!'))
    return redirect('login')


@login_required(login_url='login')
def userListView(request):
    currentUser = request.user
    if currentUser.is_superuser or currentUser.is_admin:
        allUsers = Account.objects.all().order_by('-date_joined')
    else:
        messages.error(request, 'Your are not allowed to view this page!')
        return redirect('dashboard')
    context = {
        'allUsers': allUsers,
    }
    return render(request, 'be/pages/users/account/read.html', context)


@login_required(login_url='login')
def userAddView(request):
    if request.method == 'POST':
        userForm = AccountAddForm(request.POST)
        if userForm.is_valid():
            first_name = userForm.cleaned_data['first_name']
            last_name = userForm.cleaned_data['last_name']
            email = userForm.cleaned_data['email']
            password = userForm.cleaned_data['password']
            phone_number = userForm.cleaned_data['phone_number']
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            user.phone_number = phone_number
            user.status = 'Active'
            user.save()

            messages.success(request, 'Your account has been created.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct form errors.')
    else:
        userForm = AccountAddForm()

    context = {
        'userForm': userForm,
    }
    return render(request, 'be/pages/users/account/create.html', context)


def userEditView(request, pk):
    try:
        userAccount = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        userAccount = None

    if request.method == 'POST':
        userForm = AccountForm(request.POST, instance=userAccount)
        if userForm.is_valid():
            if userForm.has_changed():
                userForm.save()
                messages.success(request, 'User account has been updated.')
            else:
                messages.info(request, 'Nothing has changed.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct form errors.')
    else:
        userForm = AccountForm(instance=userAccount)

    context = {
        'userAccount': userAccount,
        'userForm': userForm,
    }

    return render(request, 'be/pages/users/account/update.html', context)


def userDeleteView(request, pk):
    currentUser = request.user
    userAccount = get_object_or_404(Account, id=pk)
    if currentUser.is_superuser or currentUser.is_admin:
        if currentUser.id == int(userAccount.id):
            messages.warning(request, 'You can\'t delete your own account')
        else:
            if request.method == "POST":
                userAccount.is_deleted = True
                userAccount.deleted_at = timezone.now()
                userAccount.save()
                messages.success(request, 'You have successfully deleted the account!')
                return redirect('userList')
    else:
        messages.error(request, 'You are not allowed to do this!')
    context = {
        'userAccount': userAccount,
    }
    return render(request, 'be/pages/users/account/delete.html', context)


def addressEditView(request, pk):
    # Fetch the target user based on the provided pk.
    try:
        target_user = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        messages.error(request, "User does not exist.")
        return redirect('userList')  # or wherever you want to redirect to

    # Get the address associated with this user or initialize a new one if it doesn't exist.
    userAddress, created = Address.objects.get_or_create(user=target_user)

    if request.method == 'POST':
        addrForm = AddressForm(request.POST, instance=userAddress)
        if addrForm.is_valid():
            if addrForm.has_changed():
                addr = addrForm.save(commit=False)
                addr.user = target_user  # Ensure the user is set.
                addr.save()
                messages.success(request, 'User address has been updated.')
            else:
                messages.info(request, 'Nothing has changed.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct form errors.')
    else:
        addrForm = AddressForm(instance=userAddress)

    context = {
        'userAccount': target_user,
        'userAddress': userAddress,
        'addrForm': addrForm,
    }
    return render(request, 'be/pages/users/address/update.html', context)