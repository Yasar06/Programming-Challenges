def energy(richter):
    energy = 10**((1.5*richter)+4.8)
    return energy

def tons_of_TNT(energy):
    tons_of_TNT = energy / 4.184*10**9
    return tons_of_TNT

def richter_chart():
    print("Richter\t\t\tJoules\t\t\tTNT")
    print(f"{'1':<20}{energy(1):<25}{tons_of_TNT(energy(1)):<25}")
    print(f"{'9.1':<20}{energy(9.1):<25}{tons_of_TNT(energy(9.1)):<25}")
    print(f"{'9.2':<20}{energy(9.2):<25}{tons_of_TNT(energy(9.2)):<25}")
    print(f"{'9.5':<20}{energy(9.5):<25}{tons_of_TNT(energy(9.5)):<25}")

def richter_scale():    
    richter = float(input("\nenter a richter scale value: "))
    print("Richter value:",richter)
    joules = energy(richter)
    print("Equivalence in joules:",joules)
    print("Equivalence in tons of TNT:",tons_of_TNT(joules))

richter_chart()
richter_scale()
