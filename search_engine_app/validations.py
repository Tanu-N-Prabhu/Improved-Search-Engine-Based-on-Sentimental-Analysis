

class validation:
    def isEnglish(self,topic):
        try:
            topic.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True
