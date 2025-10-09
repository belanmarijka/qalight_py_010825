# Тестування REST API, 
# частина 2: Перевірка відповідності OASv3. 
# End-2-End тестування. 
# Структура тестувального фреймворку

import schemathesis

schema = schemathesis.openapi.from_url(
    #"https://petstore.swagger.io/v2/swagger.json",
    "https://example.schemathesis.io/openapi.json",
)

@schema.parametrize()
def test_api(case):
    case.call_and_validate()