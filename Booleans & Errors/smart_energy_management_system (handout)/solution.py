def energy():
    house_occupied=str(input())=="True"
    high_energy_appliance_on=str(input())=="True"
    peak_hours=str(input())=="True"
    current_energy_usage=int(input())
    return not(house_occupied) or high_energy_appliance_on and (current_energy_usage>50)
print(energy())