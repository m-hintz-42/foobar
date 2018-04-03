from fractions import Fraction


def answer(pegs):
    """

    :param pegs: List of integers representing position of a gear along an axis.
    Expected to be sorted ascending, distinct and positive.

    :return: list of the reduced radius [numerator, denominator] of gear G(0) which satisfies the constraint - RPM of
    the last gear G(x) = 2 * G(0). Stated differently: Radius, R(0) = 2 * R(x).
    If no condition can be satisfied [-1, -1] is returned.
    """
    num_pegs = len(pegs)
    # Check for invalid objects
    if num_pegs < 2 or not pegs:
        return [-1, -1]
    if (pegs[0] < 1) or (pegs[1] < 1):
        return [-1, -1]

    even = True if (num_pegs % 2 == 0) else False
    max_radius = pegs[1] - pegs[0]

    for test_radius in xrange(0, max_radius):
        status, even_mod = check_gears(test_radius, pegs)
        if status:
            # Reduce if needed
            if even:
                test_radius = Fraction(((test_radius * 3) + even_mod), 3).limit_denominator()
                return [test_radius.numerator, test_radius.denominator]
            else:
                return [test_radius, 1]
        else:
            continue
    return [-1, -1]


def check_gears(test_radius, pegs):
    gears = [test_radius]
    for index in xrange(1, len(pegs)):
        last_peg = pegs[index - 1]
        next_radius = pegs[index] - (last_peg + gears[-1])

        # Exit if gear is too long
        if next_radius < 1:
            return False, 0
        gears.append(next_radius)

    # Check exact
    if test_radius == (gears[-1] * 2):
        return True, 0
    # Check one
    if (test_radius + 1) == (gears[-1] * 2):
        return True, 1
    # Check two
    if (test_radius + 2) == (gears[-1] * 2):
        return True, 2
    else:
        return False, 0


# pegs = [-1, 1]
pegs = [4, 30, 50]
print(answer(pegs))
