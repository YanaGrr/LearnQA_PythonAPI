#Ex10: Тест на короткую фразу

class Test_Phrase:
    def test_phrase_len(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Phrase is too long"