def get_url(request):
    host = request.get_host()
    protocol = 'http://'
    if request.is_secure():
        protocol = 'https://'
    return '{}{}'.format(protocol, host)

