def song_decoder(song):
    decoded = " ".join(song.split("WUB"))
    return " ".join(decoded.split()) # The second split remove the double spaces


if __name__== "__main__":
    import codewars_test as test

    # Sample tests
    test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
    test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
    test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")

    # Test Cases
    test.assert_equals(song_decoder("RWUBWUBWUBLWUB"), "R L")
    test.assert_equals(song_decoder("WUBJKDWUBWUBWBIRAQKFWUBWUBYEWUBWUBWUBWVWUBWUB"), "JKD WBIRAQKF YE WV")
    test.assert_equals(song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB"), "KSDHEMIXUJ R S H")
    test.assert_equals(song_decoder("QWUBQQWUBWUBWUBIWUBWUBWWWUBWUBWUBJOPJPBRH"), "Q QQ I WW JOPJPBRH")
    test.assert_equals(song_decoder("WUBWUBOWUBWUBWUBIPVCQAFWYWUBWUBWUBQWUBWUBWUBXHDKCPYKCTWWYWUBWUBWUBVWUBWUBWUBFZWUBWUB"), "O IPVCQAFWY Q XHDKCPYKCTWWY V FZ")
    test.assert_equals(song_decoder("WUBYYRTSMNWUWUBWUBWUBCWUBWUBWUBCWUBWUBWUBFSYUINDWOBVWUBWUBWUBFWUBWUBWUBAUWUBWUBWUBVWUBWUBWUBJB"), "YYRTSMNWU C C FSYUINDWOBV F AU V JB")
    test.assert_equals(song_decoder("WUBKSDHEMIXUJWUBWUBRWUBWUBWUBSWUBWUBWUBHWUBWUBWUB"), "KSDHEMIXUJ R S H")
    test.assert_equals(song_decoder("AWUBWUBWUB"), "A")
    test.assert_equals(song_decoder("AWUBBWUBCWUBD"), "A B C D")
    test.assert_equals(song_decoder("WUBWWUBWUBWUBUWUBWUBBWUB"), "W U B")
    test.assert_equals(song_decoder("WUWUBBWWUBUB"), "WU BW UB")
    test.assert_equals(song_decoder("WUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUABWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUBWUB"), "WUAB")
    test.assert_equals(song_decoder("U"), "U")
    test.assert_equals(song_decoder("WUWUB"), "WU")
    test.assert_equals(song_decoder("UBWUB"), "UB")
    test.assert_equals(song_decoder("WUWUBUBWUBUWUB"), "WU UB U")
    test.assert_equals(song_decoder("WUBWWUBAWUB"), "W A")
    test.assert_equals(song_decoder("WUUUUU"), "WUUUUU")
    test.assert_equals(song_decoder("WUBWUBA"), "A")
