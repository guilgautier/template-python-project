def addition(x, y):
    """Compute the addition ``x + y``.

    .. math::
        :label: eq:my-addition

        x + y.

    Args:
        x (number): First number
        y (number): Second number

    Returns:
        number: :math:`x + y`

    .. testcode::

        from packagename.operations import addition

        result = addition(1, 3)
        print(result)

    .. testoutput::

        4
    """
    return x + y
