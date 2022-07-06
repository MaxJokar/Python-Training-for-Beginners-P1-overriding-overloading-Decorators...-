def hello_name(name: str )-> str:
    """we want to test docstring plus
    python -m pylint, pycodestyle , 
    """
    return f"Hello {name }"



h=hello_name("Maxim jokar  ")
print(h)


#After I had installed: python -m pylint .\test1.py 
#test1.py:2:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens) => return (f"Hello {name}")
# test1.py:9:0: C0304: Final newline missing (missing-final-newline)
# test1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# test1.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)

# pip install pylint


#python -m pycodestyle .\test1.py
# C:\Program Files\Python310\python.exe: No module named pycodestyle


# python -m black .\test1.py
# C:\Program Files\Python310\python.exe: No module named black




#============pip install black==============================================================================

# PS D:\practise Py2>  python -m black .\test1.py
# reformatted test1.py

# All done! ✨ 🍰 ✨


#==============================================pip install pycodestyle

# PS D:\practise Py2> python -m pycodestyle .\test1.py
# .\test1.py:13:80: E501 line too long (113 > 79 characters)
# .\test1.py:16:80: E501 line too long (88 > 79 characters)
# PS D:\practise Py2>

