from triangle import get_hypotenuse_of_a_triangle

def test_get_hypotenuse_of_a_triangle():
    a, b = 2, 4
    hypotenuse = get_hypotenuse_of_a_triangle(a, b)
    hypotenuse_two = get_hypotenuse_of_a_triangle(5, 7)

    assert hypotenuse == 4.47213595499958
    assert a != b
    # a evaulates to true
    assert a  
    # assert not a == we can use this as well to check assert that a evaluates to False 

    # assert that element in a list 
    hypot_list = [hypotenuse, hypotenuse_two]
    assert hypotenuse_two in hypot_list 

    # assert that element is not in a list 
    hypotenuse_three = get_hypotenuse_of_a_triangle(5, 9)
    hypot_list = [hypotenuse, hypotenuse_two]
    assert hypotenuse_three not in hypot_list 