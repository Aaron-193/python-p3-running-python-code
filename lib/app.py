#print("Hello world!")
#print("Hello sun!")
#print("Hello sky")

#print("Hello world!", end=" ")
#print("Hello sun!", end="!! ")
#print("Hello sky!", end="!!!\n")

print("Hello World!", end=" ")
print("Pass this test", end=", ")
print("please", end=".\n")

def test_app_py_exists():
  assert(path.exists("lib/app.py"))