class Phone:
    price = 30000
    color = 'blue'
    brand = 'samsung'
    features = ['camera','speaker','hammer']

    def call(self):   #self ba nam na dile error for python
        print('calling')

    def send_sms(self,phone,sms):
        text = f'sending SMS to: {phone} & message: {sms}'
        return text
myPhone = Phone()

print(myPhone)
print(myPhone.price)
print(myPhone.color)
print(myPhone.brand)
print(myPhone.features)
myphone.call()

result = my_phone.send_sms(143553545,'i missed to miss')
print(result)
