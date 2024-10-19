def test_function():


    def inner_function():
        print ("Я в области видимости функции test_ function")

    inner_function()


# inner_function()
# Traceback (most recent call last):
#   File "D:\pythonProject\module_4_2.py\main.py", line 10, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()
