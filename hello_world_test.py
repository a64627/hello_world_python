from hello_world import hello

def test_hello_Mario():
    name = 'Mario'
    s = "Hello " + name + "!"
    assert s == hello(name)
    
def test_hello_Goncalo():
    name = 'Goncalo'
    s = "Hello " + name + "!"
    assert s == hello(name)