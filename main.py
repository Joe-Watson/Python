cost=input("Enter your total amount to payable ")
how_may_people=input("How many people in you group ")
total_cost = int(cost)
total_people = int(how_may_people)
parcentage=input("Parcentage that you can pay of each of your amount it 12%,10%,and 5%")
payble = total_cost / total_people
each_cost = (payble * int(parcentage)) / 100
total_payable_cost =round(each_cost + payble,2)
print(f"Each one should pay {total_payable_cost}")