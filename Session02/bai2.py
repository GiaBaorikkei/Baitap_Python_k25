print("BLOOD DONOR SCRENING SYSTEM")

donor_age = int(input("Enter the age of the donor: "))
donor_weight = float(input("Enter the weight of the donor (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu
if donor_age >= 18 and donor_weight >= 50:
    print("Congratulations, you meet the criteria for blood donation.")
else:
    print("Sorry, you do not meet the criteria for blood donation.")