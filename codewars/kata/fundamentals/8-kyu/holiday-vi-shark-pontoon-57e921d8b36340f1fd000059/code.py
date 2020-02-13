def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    sec_me = pontoonDistance / youSpeed
    sec_shark = sharkDistance / (sharkSpeed / 2 if dolphin else sharkSpeed)
    print(f"sec_me: {sec_me} - sec_shark: {sec_shark}")
    if sec_shark >= sec_me:
        return "Alive!"
    else:
        return "Shark Bait!"
    
if __name__== "__main__":
    import codewars_test as test

    # Sample tests
    test.assert_equals(shark(12, 50, 4, 8, True), "Alive!")
    test.assert_equals(shark(7, 55, 4, 16, True), "Alive!")
    test.assert_equals(shark(24, 0, 4, 8, True), "Shark Bait!")

        # Test Cases
    @test.describe('Basic tests')
    def basic_tests():
        test.assert_equals(shark(12, 50, 4, 8, True), "Alive!");
        test.assert_equals(shark(7, 55, 4, 16, True), "Alive!");
        test.assert_equals(shark(24, 0, 4, 8, True), "Shark Bait!");
        test.assert_equals(shark(40, 35, 3, 20, True), "Shark Bait!");
        test.assert_equals(shark(7, 8, 3, 4, True), "Alive!");
        
    @test.describe('Random tests')
    def random_tests():

        from random import randint

        def myshark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
            if dolphin: sharkSpeed = sharkSpeed / 2
            return "Alive!" if (pontoonDistance / youSpeed < sharkDistance / sharkSpeed) else "Shark Bait!"
        
        for _ in range(40):
        
            pontoonDistance = randint(1, 50);
            sharkDistance = randint(1, 200);
            youSpeed = randint(1, 4);
            sharkSpeed =  randint(1, 20);
            dolphin = randint(0, 1) == 1;
            
            @test.it(f'Testing for {pontoonDistance} and {sharkDistance} and {youSpeed} and {sharkSpeed} and {dolphin}')
            def test_case():
                test.assert_equals( \
                    shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin), \
                    myshark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin), \
                    "It should work for random inputs too");