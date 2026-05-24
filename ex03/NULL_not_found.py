def NULL_not_found(object: any) -> int:
    """Finds and prints NULL values (None, NaN, 0, '', False)."""
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    elif type(object) is float and object != object:
        print(f"Cheese: nan {type(object)}")
        return 0
    elif type(object) is int and object == 0:
        print(f"Zero: 0 {type(object)}")
        return 0
    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")
        return 0
    elif type(object) is bool and not object:
        print(f"Fake: False {type(object)}")
        return 0
    else:
        print("Type not Found")
    return 1
