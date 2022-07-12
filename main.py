# Problem 92:
#     Square Digit Chains
#
# Description:
#     A number chain is created by continuously adding the square of the digits in a number
#       to form a new number until it has been seen before.
#
#     For example,
#         44 → 32 → 13 → 10 → 1 → 1
#         85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
#     Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
#     What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
#     How many starting numbers below ten million will arrive at 89?

def square_digit_next(n: int) -> int:
    """
    Returns the number following `n` in its 'square-digit-chain',
      meaning the sum of the squares of the digits of `n`.

    Args:
        n (int): Natural number

    Returns:
        (int): Next number, after `n`, in its square-digit-chain.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0
    return sum(map(lambda d: int(d)**2, list(str(n))))


def main(n: int) -> int:
    """
    Returns the amount of starting numbers below `n` whose square-digit-chains arrive at 89.

    Args:
        n (int): Natural number

    Returns:
        (int): Amount of starting numbers whose square-digit-chains arrive at 89

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    destinations = {1: 1, 89: 89}  # Map of starting points to ending location (which is always either 1 or 89)
    to_89 = 0                      # Count of numbers below `n` eventually arriving at 89
    for x in range(1, n):
        if x not in destinations:
            # Haven't seen this number, so follow the chain until hitting something known
            curr = x
            seen = {curr}
            while curr not in destinations:
                seen.add(curr)
                curr = square_digit_next(curr)

            # All traversed numbers in the chain end at this number
            endpoint = destinations[curr]
            for y in seen:
                destinations[y] = endpoint

        # Now know where `x` ends, so check if it ends at 89
        to_89 += int(destinations[x] == 89)

    return to_89


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    arriving_89 = main(num)
    print('Numbers below {} arriving at 89:'.format(num))
    print('  {}'.format(arriving_89))
