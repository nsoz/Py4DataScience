def ft_filter(func, iterable):
    """This function is a simplified version of the filter call."""
    if func:
        return [x for x in iterable if func(x)]
    else:
        return [x for x in iterable if x]
