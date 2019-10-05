from basic_operations import factorial

# permutations are calculated by factorial, so we just do an assertion
# on the parameter and then just call our factorial method
def permutations(sample_size):
    assert (isinstance(sample_size, int)), 'Method requires integer paramter'
    return factorial(sample_size)

# formula for combinations:
# n! / ((n - p)! * p!)
# where n is sample_size and p is selection_size
def combinations(sample_size, selection_size):
    assert (isinstance(sample_size, int)), 'Method requires integer paramter for sample size'
    assert (isinstance(selection_size, int)), 'Method requires integer paramter for selection size'
    return factorial(sample_size) / (factorial(sample_size - selection_size) * factorial(selection_size))

# formula for variations without repetition:
# n! / (n - p)!
# where n is sample_size and p is selection_size
def variations_without_repetition(sample_size, selection_size):
    assert (isinstance(sample_size, int)), 'Method requires integer paramter for sample size'
    assert (isinstance(selection_size, int)), 'Method requires integer paramter for selection size'
    return factorial(sample_size) / factorial(sample_size - selection_size)

# formula for variations with repetition:
# n ** p (note this is a power function, not a multiplication)
# where n is sample_size and p is selection_size
def variations_with_repetition(sample_size, selection_size):
    assert (isinstance(sample_size, int)), 'Method requires integer paramter for sample size'
    assert (isinstance(selection_size, int)), 'Method requires integer paramter for selection size'
    return sample_size ** selection_size