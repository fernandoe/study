describe "Basic Tests" do
  it "should pass the basic tests" do
    Test.assert_equals(make_upper_case("hello"), "HELLO")
  end
end