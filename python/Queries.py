def get_user_input(x):
    query=f"Select Id,Name from Account limit {x}"
    return query