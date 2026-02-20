student={
    "name":"John",
    "age":25,
    "city":"New York"
}
values=[student[key] for key in student]
keys=[key for key in student]
print(f'keys:{keys},values:{values}')