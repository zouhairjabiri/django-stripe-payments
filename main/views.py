from django.shortcuts import render
import stripe
# Create your views here.

stripe.api_key = "sk_test_51H31OKIUPngVvEtgLTa2GrbTMWQlm9tegccKqyPcYJ7lq1jdB6usF6f5Nv9n66N7DUOD77e6F5UdXFj0K3jcKKGz00PE7rnMxO"


def index(request):
    return render(request, 'main/index.html')


def checkout(request, pk):
    if pk == 1:
        abonnement = 'Meduim'
        prix = 150

    if pk == 2:
        abonnement = 'Premuim'
        prix = 290
    return render(request, 'main/checkout.html', {'abonnement': abonnement, 'prix': prix})


def thnks(request):
    if request.method == "POST":
        Customer = stripe.Customer.create(
            name=request.POST['var2'], email=request.POST['var3'],source=request.POST['stripeToken'] )
        stripe.Charge.create(
            amount=int(request.POST['prix']),
            customer=Customer,
            currency="usd",
            description="My First Test Charge (created for API docs)",
        )
    return render(request, 'main/thnks.html')
