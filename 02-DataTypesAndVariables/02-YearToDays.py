century = int(input())

var_years = century * 100
var_days = var_years * 365.2422
var_hours = int(var_days) * 24
var_minutes = var_hours * 60

print(f"{century} centuries = {var_years} years = {int(var_days)} days = {var_hours} hours = {var_minutes} minutes")


