def test_palindrome():
    assert palindrome("madam") == True
    assert palindrome("racecar") == True
    assert palindrome("A man a plan a canal Panama") == True
    assert palindrome("hello") == False
    assert palindrome("world") == False
    assert palindrome("Able was I ere I saw Elba") == True
    assert palindrome("Was it a car or a cat I saw") == True
