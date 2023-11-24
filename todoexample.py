user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print (todos)

print(type(user_prompt))


Todos= []
while True:
    todo = input(user_prompt)
    Todos.append(todo)
    print(Todos)