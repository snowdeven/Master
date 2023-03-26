import multiprocessing

def simulate_treatment_wrapper(args):
    return simulate_treatment(*args)

def simulate_treatment(param1, param2):
    donor = Individual(param1, param2)
    patient = Individual(param1, param2)

    heals = 0
    nb_therapeutic_targets = 0
    if donor.can_heal(patient):
        heals = 1
        nb_therapeutic_targets = len(donor.targets(patient))

    return heals, nb_therapeutic_targets

def main():
    p = Pool(processes=4)
    tasks = [(param1, param2) for i in range(1000000)]
    simulations = p.map_async(simulate_treatment_wrapper, tasks)
    p.close()
    p.join()
    for sim in simulations.get():
        heals = sim[0]
        nb_therapeutic_minors = sim[1]
        # do some stuff with the results