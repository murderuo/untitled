import zeep
wsdl = 'https://api.n11.com/ws/CategoryService.wsdl'
client = zeep.Client(wsdl=wsdl,strict=False)
key=[{
'appKey' : 'api keyiniz',
'appSecret' : 'api secret keyiniz'
}]
print(client.service.GetTopLevelCategories(key))
