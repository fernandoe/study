describe "Basic tests" do
  it "should pass fixed tests" do
    Test.assert_equals(find_smallest_int([78,56,232,12,8]), 8)
    Test.assert_equals(find_smallest_int([78,56,-2,12,8]), -2)
    Test.assert_equals(find_smallest_int([-78,56,-2,12,8]), -78)
    Test.assert_equals(find_smallest_int([-8]), -8)
    Test.assert_equals(find_smallest_int([1,2,3,4,5,6,7,8,9,10]), 1)
    Test.assert_equals(find_smallest_int([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]), -10)
    Test.assert_equals(find_smallest_int([-78,56,232,12,8]), -78)
    Test.assert_equals(find_smallest_int([78,56,-2,12,-8]), -8)
    Test.assert_equals(find_smallest_int([-8,-3]), -8)
    Test.assert_equals(find_smallest_int([-3,-8]), -8)
  end
end
