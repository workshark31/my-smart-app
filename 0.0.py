from fhirclient import client
from fhirclient.models.encounter import Encounter
from fhirclient.models.procedure import Procedure

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://r4.smarthealthit.org'
}

smart = client.FHIRClient(settings=settings)

search = Encounter.where(struct={'subject': '2cda5aad-e409-4070-9a15-e1c35c46ed5a', 'status': 'finished'})

print([res.type[0].text for res in search.perform_resources_iter(smart.server)])
# {'Encounter for symptom', 'Encounter for check up (procedure)'}