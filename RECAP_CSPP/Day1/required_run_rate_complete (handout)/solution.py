# Write your solution here
def Req_run_rate(runs, overs):
    run_rate = runs / overs
    return round(run_rate,2)
print(Req_run_rate(int(input()), float(input())))

