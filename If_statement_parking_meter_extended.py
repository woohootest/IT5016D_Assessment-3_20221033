
print("Kia Ora, this is a parking meter")

print("Maximum park time is 4 hours")

parking_hours = input("Parking time: ")


rate = 4
cost = 0

pay = float(parking_hours) * float(rate)

if parking_hours > 3:
    cost = rate * 3
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    parking_hours -= 3
    # add to the current cost
    cost += rate * parking_hours
    print("The cost of the parking is $", cost)
else:
    cost = rate * parking_hours

pay = float(parking_hours) * float(rate)


