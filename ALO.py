import numpy as np
from initialization import initialization
from RouletteWheelSelection import roulette_wheel_selection
from Random_walk_around_antlion import random_walk_around_antlion

def ALO(N, Max_iter, lb, ub, dim, fobj):
    lb = np.array(lb)  # Convert lb to numpy array
    ub = np.array(ub)  # Convert ub to numpy array
    
    # Initialize the positions of antlions and ants
    antlion_position = initialization(N, dim, ub, lb)
    ant_position = initialization(N, dim, ub, lb)

    # Initialize variables to save the position of elite, sorted antlions, 
    # convergence curve, antlions fitness, and ants fitness
    Sorted_antlions = np.zeros((N, dim))
    Elite_antlion_position = np.zeros(dim)
    Elite_antlion_fitness = np.inf
    Convergence_curve = np.zeros(Max_iter)
    antlions_fitness = np.zeros(N)
    ants_fitness = np.zeros(N)

    # Calculate the fitness of initial antlions and sort them
    for i in range(antlion_position.shape[0]):
        antlions_fitness[i] = fobj(antlion_position[i, :])

    sorted_antlion_fitness = np.sort(antlions_fitness)
    sorted_indexes = np.argsort(antlions_fitness)

    for newindex in range(N):
        Sorted_antlions[newindex, :] = antlion_position[sorted_indexes[newindex], :]

    Elite_antlion_position = Sorted_antlions[0, :]
    Elite_antlion_fitness = sorted_antlion_fitness[0]

    # Main loop start from the second iteration since the first iteration 
    # was dedicated to calculating the fitness of antlions
    Current_iter = 1
    while Current_iter <= Max_iter:
        # This for loop simulates random walks
        for i in range(ant_position.shape[0]):
            # Select ant lions based on their fitness (the better anlion the higher chance of catching ant)
            Rolette_index = roulette_wheel_selection(1 / sorted_antlion_fitness)
            if Rolette_index == -1:
                Rolette_index = 0

            # RA is the random walk around the selected antlion by roulette wheel
            RA = random_walk_around_antlion(dim, Max_iter, lb, ub, Sorted_antlions[Rolette_index, :], Current_iter)

            # RA is the random walk around the elite (best antlion so far)
            RE = random_walk_around_antlion(dim, Max_iter, lb, ub, Elite_antlion_position, Current_iter)

            ant_position[i, :] = (RA[Current_iter - 1, :] + RE[Current_iter - 1, :]) / 2  # Equation (2.13) in the paper

        for i in range(ant_position.shape[0]):
            # Boundary checking (bring back the antlions of ants inside search
            # space if they go beyond the boundaries
            Flag4ub = ant_position[i, :] > ub
            Flag4lb = ant_position[i, :] < lb
            ant_position[i, :] = (ant_position[i, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
            ants_fitness[i] = fobj(ant_position[i, :])

        # Update antlion positions and fitnesses based on the ants (if an ant 
        # becomes fitter than an antlion we assume it was caught by the antlion  
        # and the antlion update goes to its position to build the trap)
        double_population = np.vstack((Sorted_antlions, ant_position))
        double_fitness = np.hstack((sorted_antlion_fitness, ants_fitness))

        double_fitness_sorted = np.sort(double_fitness)
        I = np.argsort(double_fitness)
        double_sorted_population = double_population[I, :]

        antlions_fitness = double_fitness_sorted[:N]
        Sorted_antlions = double_sorted_population[:N, :]

        # Update the position of elite if any antlions become fitter than it
        if antlions_fitness[0] < Elite_antlion_fitness:
            Elite_antlion_position = Sorted_antlions[0, :]
            Elite_antlion_fitness = antlions_fitness[0]

        # Keep the elite in the population
        Sorted_antlions[0, :] = Elite_antlion_position
        antlions_fitness[0] = Elite_antlion_fitness

        # Update the convergence curve
        Convergence_curve[Current_iter - 1] = Elite_antlion_fitness

        # Display the iteration and best optimum obtained so far
        if Current_iter % 50 == 0:
            print('At iteration', Current_iter, 'the elite fitness is', Elite_antlion_fitness)

        Current_iter += 1

    return Elite_antlion_fitness, Elite_antlion_position, Convergence_curve



# def ALO(N, Max_iter, lb, ub, dim, fobj):
    lb = np.array(lb)  # Convert lb to numpy array
    ub = np.array(ub)  # Convert ub to numpy array
    
    # Initialize the positions of antlions and ants
    antlion_position = initialization(N, dim, ub, lb)
    ant_position = initialization(N, dim, ub, lb)

    # Initialize variables to save the position of elite, sorted antlions, 
    # convergence curve, antlions fitness, and ants fitness
    Sorted_antlions = np.zeros((N, dim))
    Elite_antlion_position = np.zeros(dim)
    Elite_antlion_fitness = np.inf
    Convergence_curve = np.zeros(Max_iter)
    antlions_fitness = np.zeros(N)
    ants_fitness = np.zeros(N)

    # Calculate the fitness of initial antlions and sort them
    for i in range(antlion_position.shape[0]):
        antlions_fitness[i] = fobj(antlion_position[i, :])

    sorted_antlion_fitness = np.sort(antlions_fitness)
    sorted_indexes = np.argsort(antlions_fitness)

    for newindex in range(N):
        Sorted_antlions[newindex, :] = antlion_position[sorted_indexes[newindex], :]

    Elite_antlion_position = Sorted_antlions[0, :]
    Elite_antlion_fitness = sorted_antlion_fitness[0]

    # Main loop start from the second iteration since the first iteration 
    # was dedicated to calculating the fitness of antlions
    Current_iter = 1
    while Current_iter <= Max_iter:
        # This for loop simulates random walks
        for i in range(ant_position.shape[0]):
            # Select ant lions based on their fitness (the better anlion the higher chance of catching ant)
            Rolette_index = roulette_wheel_selection(1 / sorted_antlion_fitness)
            if Rolette_index == -1:
                Rolette_index = 0

            # RA is the random walk around the selected antlion by roulette wheel
            RA = random_walk_around_antlion(dim, Max_iter, lb, ub, Sorted_antlions[Rolette_index, :], Current_iter)

            # RA is the random walk around the elite (best antlion so far)
            RE = random_walk_around_antlion(dim, Max_iter, lb, ub, Elite_antlion_position, Current_iter)

            ant_position[i, :] = (RA[Current_iter, :] + RE[Current_iter, :]) / 2  # Equation (2.13) in the paper

        for i in range(ant_position.shape[0]):
            # Boundary checking (bring back the antlions of ants inside search
            # space if they go beyond the boundaries
            Flag4ub = ant_position[i, :] > ub
            Flag4lb = ant_position[i, :] < lb
            ant_position[i, :] = (ant_position[i, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
            ants_fitness[i] = fobj(ant_position[i, :])

        # Update antlion positions and fitnesses based on the ants (if an ant 
        # becomes fitter than an antlion we assume it was caught by the antlion  
        # and the antlion update goes to its position to build the trap)
        double_population = np.vstack((Sorted_antlions, ant_position))
        double_fitness = np.hstack((sorted_antlion_fitness, ants_fitness))

        double_fitness_sorted = np.sort(double_fitness)
        I = np.argsort(double_fitness)
        double_sorted_population = double_population[I, :]

        antlions_fitness = double_fitness_sorted[:N]
        Sorted_antlions = double_sorted_population[:N, :]

        # Update the position of elite if any antlions become fitter than it
        if antlions_fitness[0] < Elite_antlion_fitness:
            Elite_antlion_position = Sorted_antlions[0, :]
            Elite_antlion_fitness = antlions_fitness[0]

        # Keep the elite in the population
        Sorted_antlions[0, :] = Elite_antlion_position
        antlions_fitness[0] = Elite_antlion_fitness

        # Update the convergence curve
        Convergence_curve[Current_iter - 1] = Elite_antlion_fitness

        # Display the iteration and best optimum obtained so far
        if Current_iter % 50 == 0:
            print('At iteration', Current_iter, 'the elite fitness is', Elite_antlion_fitness)

        Current_iter += 1

    return Elite_antlion_fitness, Elite_antlion_position, Convergence_curve




# def ALO(N, Max_iter, lb, ub, dim, fobj):
    # Initialize the positions of antlions and ants
    print()
    antlion_position = initialization(N, dim, ub, lb)
    ant_position = initialization(N, dim, ub, lb)

    # Initialize variables to save the position of elite, sorted antlions, 
    # convergence curve, antlions fitness, and ants fitness
    Sorted_antlions = np.zeros((N, dim))
    Elite_antlion_position = np.zeros(dim)
    Elite_antlion_fitness = np.inf
    Convergence_curve = np.zeros(Max_iter)
    antlions_fitness = np.zeros(N)
    ants_fitness = np.zeros(N)

    # Calculate the fitness of initial antlions and sort them
    for i in range(antlion_position.shape[0]):
        antlions_fitness[1, i] = fobj(antlion_position[i, :])

    sorted_antlion_fitness = np.sort(antlions_fitness)
    sorted_indexes = np.argsort(antlions_fitness)

    for newindex in range(N):
        Sorted_antlions[newindex, :] = antlion_position[sorted_indexes[newindex], :]

    Elite_antlion_position = Sorted_antlions[1, :]
    Elite_antlion_fitness = sorted_antlion_fitness[1]

    # Main loop start from the second iteration since the first iteration 
    # was dedicated to calculating the fitness of antlions
    Current_iter = 2
    while Current_iter < Max_iter + 1:
        # This for loop simulates random walks
        for i in range(ant_position.shape[0]):
            # Select ant lions based on their fitness (the better anlion the higher chance of catching ant)
            Rolette_index = roulette_wheel_selection(1 / sorted_antlion_fitness)
            if Rolette_index == -1:
                Rolette_index = 1

            # RA is the random walk around the selected antlion by roulette wheel
            RA = random_walk_around_antlion(dim, Max_iter, lb, ub, Sorted_antlions[Rolette_index, :], Current_iter)

            # RA is the random walk around the elite (best antlion so far)
            RE = random_walk_around_antlion(dim, Max_iter, lb, ub, Elite_antlion_position, Current_iter)

            ant_position[i, :] = (RA[Current_iter, :] + RE[Current_iter, :]) / 2  # Equation (2.13) in the paper

        for i in range(ant_position.shape[0]):
            # Boundary checking (bring back the antlions of ants inside search
            # space if they go beyond the boundaries
            Flag4ub = ant_position[i, :] > ub
            Flag4lb = ant_position[i, :] < lb
            ant_position[i, :] = (ant_position[i, :] * (~(Flag4ub + Flag4lb))) + ub * Flag4ub + lb * Flag4lb
            ants_fitness[1, i] = fobj(ant_position[i, :])

        # Update antlion positions and fitnesses based on the ants (if an ant 
        # becomes fitter than an antlion we assume it was caught by the antlion  
        # and the antlion update goes to its position to build the trap)
        double_population = np.vstack((Sorted_antlions, ant_position))
        double_fitness = np.hstack((sorted_antlion_fitness, ants_fitness))

        double_fitness_sorted = np.sort(double_fitness)
        I = np.argsort(double_fitness)
        double_sorted_population = double_population[I, :]

        antlions_fitness = double_fitness_sorted[1:N]
        Sorted_antlions = double_sorted_population[1:N, :]

        # Update the position of elite if any antlions become fitter than it
        if antlions_fitness[1] < Elite_antlion_fitness:
            Elite_antlion_position = Sorted_antlions[1, :]
            Elite_antlion_fitness = antlions_fitness[1]

        # Keep the elite in the population
        Sorted_antlions[1, :] = Elite_antlion_position
        antlions_fitness[1] = Elite_antlion_fitness

        # Update the convergence curve
        Convergence_curve[Current_iter - 1] = Elite_antlion_fitness

        # Display the iteration and best optimum obtained so far
        if Current_iter % 50 == 0:
            print('At iteration', Current_iter, 'the elite fitness is', Elite_antlion_fitness)

        Current_iter += 1

    return Elite_antlion_fitness, Elite_antlion_position, Convergence_curve
