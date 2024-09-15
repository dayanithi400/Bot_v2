from django.shortcuts import render
from django.http import HttpResponse
from .models import signup
from .models import MiningActivity, CarbonSink, EmissionCalculation
from .forms import MiningActivityForm, CarbonSinkForm

def home(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        
        obj = signup()
        obj.Firstname=firstname
        obj.Lastname=lastname
        obj.Email=email
        obj.Password=password
        obj.save()
    return render(request,'index.html')
def main(request):
    return render(request,('main.html'))

def validate(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        users = signup.objects.filter(Email=username, Password=password)
        
        if users.exists():
            return render(request, 'main.html')
        else:
            return HttpResponse('Invalid username or password')
    
    return render(request, 'signin.html')

# Example emission factors
EMISSION_FACTOR = 2.7  # Emission per ton of excavation
FUEL_EMISSION_FACTOR = 2.3  # Emission per liter of fuel

# Carbon absorption factor
CARBON_ABSORPTION_PER_TREE = 21  # Example: One tree absorbs 21 kg of CO2/year

def calculate_emissions(mining_activity):
    excavation_emission = mining_activity.excavation * EMISSION_FACTOR
    fuel_emission = mining_activity.fuel_usage * FUEL_EMISSION_FACTOR
    return excavation_emission + fuel_emission

def calculate_absorption(carbon_sink):
    return carbon_sink.tree_count * CARBON_ABSORPTION_PER_TREE

def gap_analysis(request):
    if request.method == 'POST':
        mining_form = MiningActivityForm(request.POST)
        sink_form = CarbonSinkForm(request.POST)
        
        if mining_form.is_valid() and sink_form.is_valid():
            mining_activity = mining_form.save(commit=False)
            #mining_activity.user = request.user  # Assuming user is logged in
            mining_activity.save()
            
            carbon_sink = sink_form.save(commit=False)
            #carbon_sink.user = request.user
            carbon_sink.save()
            
            # Perform calculations
            total_emissions = calculate_emissions(mining_activity)
            total_absorption = calculate_absorption(carbon_sink)
            gap = total_emissions - total_absorption
            
            # Save the results
            emission_calculation = EmissionCalculation(
                #   user=request.user,
                total_emissions=total_emissions,
                total_absorption=total_absorption,
                gap=gap
            )
            emission_calculation.save()
            
            # Render result
            return render(request, 'results.html', {
                'total_emissions': total_emissions,
                'total_absorption': total_absorption,
                'gap': gap,
            })
    else:
        mining_form = MiningActivityForm()
        sink_form = CarbonSinkForm()
    
    return render(request, 'data_entry.html', {
        'mining_form': mining_form,
        'sink_form': sink_form,
    })
