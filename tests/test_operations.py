
from src.operations import add, sub 


def test_add():
    
    assert add(2,3)==5
    
    assert add(-1,1)==0
    
    assert sub(5,3)==2
    
def test_sub():
    
    assert sub(4,1)==3
    assert sub(10,5)==5
    assert sub(5,10)==-1