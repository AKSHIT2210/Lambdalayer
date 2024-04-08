def get_user_input(x):
    query=f"Select Id,Name from Contact limit {x}"
    return query