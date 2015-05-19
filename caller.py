import urllib3, certifi
import json

api_key = '7cfdf680476fee82be7be8013c00d364bac962c2'
uid = 'QMySfV'
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET', 'https://api.typeform.com/v0/form/'+uid+'?key='+
	api_key+'&completed=true')
print("Status: "+str(r.status))

parsed = json.loads(r.data.decode())
keys = parsed.keys()

answers = parsed['responses']

# to keep track of users by mapping their ids to their names (First and last)
cache = {}
# dictionary to keep track of the responses recorded by unique id 
log = {} 

for respondent in answers:
	print(respondent['id'])
	vals = list(respondent.values())
	for i in vals:
		print(i)


