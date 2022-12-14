class RequestFormData:
    '''
    * class : krx reqeust body
    '''
    def __init__(self):
        self.formData = {}
    
    def setFormData(self, key: str, value: str) :
        self.formData[key] = value
        return self