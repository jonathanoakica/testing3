def clean_text(text):

    """Formats the user input.

    Text is made lowercase and spaces are removed .

    Parameters

    ----------

    text : str

        user string representing a quadratic equation



    Returns

    -------

    equation: str

        A string without spaces or uppercases.



    Example

    --------

    clean_text("4X**2 + 2x - 6")

    """
    for i in text:
        equation = text.replace(" ", "")
        equation = equation.lower()
    return equation


def find_a(equation):

    """Finds the A value in a quadratic equation.



    Takes the equation as input and checks if the A value is

    negative, positive, implicit or explicit.



    Parameters

    ----------

    equation : str

        user string representing a quadratic equation



    Returns

    -------

    a: int

        An integer value representing the A value.



    Example

    --------

    find_a("4x**2+2x-6")

    """

    if equation[0] == "-":

        if equation[1] == "x":

            a = -abs(1)

        else:

            a = -abs(int(equation[1]))

    else:

        if equation[0] == "x":

            a = 1

        else:

            a = int(equation[0])

    return a


def find_b(equation):

    """Finds the B value in a quadratic equation.



    Takes the equation as input, uses find to locate the B value,

    and checks if the B value is negative or positive.



    Parameters

    ----------

    equation : str

        User string representing a quadratic equation



    Returns

    -------

    b: int

        An integer value representing the B value.



    Example

    --------

    find_b("4x**2+2x-6")

    """

    b = equation[equation.find("**") + 3 :]

    if b[0] == "-":

        b = -abs(int(b[1]))

    else:

        b = int(b[1])

    return b


def find_c(equation):

    """Finds the C value in a quadratic equation.



    Takes the equation as input, uses find to locate the C value,

    and checks if the C value is negative or positive.



    Parameters

    ----------

    equation : str

        User string representing a quadratic equation



    Returns

    -------

    c: int

        An integer value representing the C value.



    Example

    --------

    find_c("4x**2+2x-6")

    """

    c = equation[equation.find("**") + 6 :]

    if c[0] == "-":

        c = -abs(int(c[1]))

    else:

        c = int(c[1])

    return c


def find_delta(a, b, c):

    """Calculates the delta in a quadratic equation.



    Uses the B value to the power of 2 and subtracts the results

    of the multiplication between 4, a and c.



    Parameters

    ----------

    a : int

        A value extracted from the equation input



    b : int

        B value extracted from the equation input



    c : int

        C value extracted from the equation input



    Returns

    -------

    delta: int

        An integer value.



    Example

    --------

    find_delta(4, 2, -6)

    """

    delta = (b**2) - (4 * a * c)

    return delta


def find_roots(a, b, delta):

    """Calculates the X values called roots.



    Uses the negative value of B in two instances:

    - Subtracting B from the root of delta divided by twice the value of A

    - Adding B to the root of delta divided by twice the value of A



    Parameters

    ----------

    a : int

        A value extracted from the equation input



    b : int

        B value extracted from the equation input



    delta : int

        delta value obtained from the solve_delta function



    Returns

    -------

    x_1: int

        First root value for a given equation.



    x_2: int

        Second root value for a given equation.



    Example

    --------

    find_roots(4, 2, 100)

    """

    x_1 = (-b + delta ** (1 / 2)) / (2 * a)

    x_2 = (-b - delta ** (1 / 2)) / (2 * a)

    return x_1, x_2


def calcbhaskara():

    """Solves a quadratic equation.



    Uses the find a, b, c, delta, roots and clean_text functions

    to calculate the results of a quadratic equation.



    Parameters

    ----------

    None



    Returns

    -------

    a : int

        A value extracted from the equation input



    b : int

        B value extracted from the equation input



    c: int

        C value extracted from the equation input



    delta : int

        delta value obtained from the solve_delta function



    x_1: int

        First root value for a given equation.



    x_2: int

        Second root value for a given equation.



    Example

    --------

    calcbhaskara()

    """

    text = input("paste a quadratic equation, e.g: 4x**2+2x-6...  ")

    equation = clean_text(text)

    a = find_a(equation)

    b = find_b(equation)

    c = find_c(equation)

    delta = find_delta(a, b, c)

    x_1, x_2 = find_roots(a, b, delta)

    return a, b, c, delta, x_1, x_2
