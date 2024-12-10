import basic

while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>',text) #stdin as a placeholder
    
    if error: 
        print(error.as_string())
    else:
        print(result)