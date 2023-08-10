deploy =\
"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  labels:
    app: mywebsite
    tier: frontend
spec:
  replicas: 3
  template:
    metadata:
      name: myapp-pod
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx
          image: nginx
  selector:
    matchLabels:
      app: myapp
      app: myapp
"""

job = \
"""
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl:5.34.0
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
"""

vs = \
"""
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: banking-external
spec:
  hosts:
  - "*"
  gateways:
  - banking-gateway
  http:
  - match:
    - uri:
        prefix: /api/v1/k8s
    route:
    - destination:
        host: k8sh
        port:
          number: 5000
  - match:
    - uri:
        prefix: /api/v1/summation
    route:
    - destination:
        host: event
        subset: v1
        port:
          number: 5000
  - match:
    - uri:
        prefix: /api/v1/event
    route:
    - destination:
        host: event
        subset: v1
        port:
          number: 5000
  - match:
    - uri:
        prefix: /api/v1/raffle
    route:
    - destination:
        host: raffle
        port:
          number: 5000
  - match:
    - uri:
        prefix: /api/v1/deposit
    route:
    - destination:
        host: deposit
        port:
          number: 5000
"""

service = \
"""
apiVersion: v1
kind: Service
metadata:
  name: deposit2
spec:
  type: ClusterIP
  selector:
    app: deposit
  ports:
  - protocol: TCP
    targetPort: 5000
    port: 5000
    name: http
"""

import yaml
from pprint import pprint
import requests

#data = yaml.load(deploy, Loader=yaml.Loader)
#data = yaml.load(job, Loader=yaml.Loader)
#data = yaml.load(vs, Loader=yaml.Loader)
data = yaml.load(service, Loader=yaml.Loader)
"""
json_d = dict(
    namespace = 'banking',
    job = data
)
json_d = dict(
    group       = 'networking.istio.io',
    version     = 'v1alpha3',
    plural      = 'virtualservices',
    patch_function_name   = 'patch_dict',
    patch_function_code   = patch_dict_str
)
"""
patch_dict_str = \
"""
def patch_dict(data):
  data['spec']['http'][1]['route'][0] = {'destination': {'host': 'event2','port': {'number': 5000},'subset': 'v3'}}
"""
json_d = dict(
    service = data
)


#r = requests.post('http://banking.leebalso.org/api/v1/k8s/deployments', json=json_d)
#requests.delete('http://banking.leebalso.org/api/v1/k8s/deployment/banking/frontend')
#r = requests.post('http://banking.leebalso.org/api/v1/k8s/jobs', json=json_d)
#r = requests.put('http://banking.leebalso.org/api/v1/k8s/customobject/banking/banking-external', json=json_d)
#r = requests.get('http://banking.leebalso.org/api/v1/k8s/deployment/banking/event-v1')
r = requests.get('http://banking.leebalso.org/api/v1/k8s/services/banking')
#r = requests.delete('http://banking.leebalso.org/api/v1/k8s/service/banking/deposit')
#r = requests.post('http://banking.leebalso.org/api/v1/k8s/services/banking', json=json_d)

"""
local_vars = {}
exec(patch_dict_str, local_vars)
f = local_vars['patch_dict']
f(data)
pprint(data)
"""
pprint(r.text) 