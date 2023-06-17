from ipware import get_client_ip

lista_ip = []
def is_valid_ip(get_response):
    def middleware(request):
        ip, is_routable = get_client_ip(request)
        response = get_response(request)
        print("ip",ip)
        print("is_routable",is_routable)
        lista_ip.append(ip)
        print("lista_ip",lista_ip)
        return response
    return middleware