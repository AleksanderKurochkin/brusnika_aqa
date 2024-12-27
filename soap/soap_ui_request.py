from datetime import datetime
from faker import Faker
import requests
import allure
import xml.etree.ElementTree as ET
from base.base_page import BasePage
from data.links import Links

faker = Faker()


@allure.epic("SOAP Requests")
class SoapRequests(BasePage):
    URL = Links.URL_XML
    # URL = "https://brusnika-qa.demo.ultimeta.ru/ws/brusnika-1c"
    headers = {"Content-Type": "text/xml; charset=utf-8"}
    auth = ("test", "test")
    _PAGE_URL = None
    _TRADES_URL = None
    _title = f"AQA_SoapUi_Закупка_СМР {datetime.now().strftime('%d.%m.%Y')} {datetime.now().strftime('%H:%M')}"
    _random_data = faker.random_int(min=10000, max=99999)

    @allure.title("UploadWorksTenderRequest")
    def upload_works_tender_request(self):
        url = self.URL
        headers = self.headers
        auth = self.auth
        xml_request = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:brus="http://ultimeta.ru/schemas/brusnika-1c">
   <soapenv:Header/>
   <soapenv:Body>
      <brus:UploadWorksTenderRequest>
         <brus:packageId>{self._random_data}</brus:packageId>
         <brus:tenderId>{self._random_data}</brus:tenderId>
         <brus:registeredNumber>{self._random_data}</brus:registeredNumber>
         <brus:emailOrganizer>o1s2@test.ru</brus:emailOrganizer>
         <brus:title>{self._title}</brus:title>
         <brus:currencyCode>RUB</brus:currencyCode>
         <brus:vatType>INCLUDED</brus:vatType>
         <brus:notes>Первый тестовый коммент</brus:notes>
         
         <brus:lots>
            <brus:lot>
               <brus:id>{self._random_data}</brus:id>
               <brus:registeredNumber>{self._random_data}</brus:registeredNumber>
               <brus:title>Первый лот</brus:title>
               <brus:initialContractPrice>1000000</brus:initialContractPrice>
               <brus:description>Закупка концтоваров</brus:description>
               <brus:projectClassifierCode>100</brus:projectClassifierCode>
               <brus:procurementClassifierCode>55</brus:procurementClassifierCode>
               <brus:executionPeriod>120</brus:executionPeriod>
               <brus:guaranteePeriodReserveAssurance>100000</brus:guaranteePeriodReserveAssurance>
               <brus:guaranteePeriod>2 года</brus:guaranteePeriod>
               <brus:generalContractingPercentage>2%</brus:generalContractingPercentage>
               <brus:enablePricePerPurchaseItem>false</brus:enablePricePerPurchaseItem>
               <brus:paymentTermsType>MULTISTAGE_PAYMENT_BY_PARTICIPANT</brus:paymentTermsType>
               
               <brus:worksPurchaseItems>
                  <brus:worksPurchaseItem>
                     <!--You have a CHOICE of the next 2 items at this level-->
                     <brus:sectionNumber>1</brus:sectionNumber>
                     <brus:sectionTitle>Раздел 1</brus:sectionTitle>
                     <brus:comment>коммент для раздела 1</brus:comment>
                  </brus:worksPurchaseItem>
                     
                  <brus:worksPurchaseItem>   
                     <brus:id>{self._random_data}</brus:id>
                     <brus:workTypeCode>11</brus:workTypeCode>
                     <brus:productClassifierCode>22</brus:productClassifierCode>
                     <brus:quantity>100</brus:quantity>
                     <brus:unitCode>15</brus:unitCode>
                     <brus:consumptionRate>1</brus:consumptionRate>
                     <brus:fixWorksPrice>false</brus:fixWorksPrice>
                    <brus:fixGoodsPrice>false</brus:fixGoodsPrice>
                     <brus:comment>коммент для позиции 1</brus:comment>
                  </brus:worksPurchaseItem>
               </brus:worksPurchaseItems>
            </brus:lot>
         </brus:lots>
         
      </brus:UploadWorksTenderRequest>
   </soapenv:Body>
</soapenv:Envelope>
        """
        response = requests.post(url, data=xml_request, headers=headers, auth=auth)
        # Проверка статуса
        assert response.status_code == 200, f"HTTP ошибка: {response.status_code}"
        # Убедиться, что статус успеха
        if "<ns2:success>false</ns2:success>" in response.text:
            # Парсинг XML ответа для извлечения ошибки
            root = ET.fromstring(response.text)
            namespaces = {'ns2': 'http://ultimeta.ru/schemas/brusnika-1c'}
            error_message = root.find(".//ns2:errors/ns2:error", namespaces)
            if error_message is not None:
                raise AssertionError(f"Ошибка в ответе: {error_message.text}")
            else:
                raise AssertionError("Ошибка в ответе, но текст ошибки отсутствует!")
        # Убедиться, что статус успеха
        assert "<ns2:success>true</ns2:success>" in response.text, "Некорректный статус в ответе!"
        root = ET.fromstring(response.text)

        # Указываем пространство имен
        namespaces = {'ns2': 'http://ultimeta.ru/schemas/brusnika-1c'}

        # Извлекаем значение <ns2:url>
        url_element = root.find(".//ns2:url", namespaces)
        if url_element is not None and url_element.text:
            self._TRADES_URL = url_element.text
            print(f"Извлеченный URL: {self._TRADES_URL}")
        else:
            raise AssertionError("Элемент <ns2:url> отсутствует или не содержит текст!")
        return self._TRADES_URL

    def get_url_purchase(self):
        with allure.step(f"Получаем ID закупки: {self._PAGE_URL}"):
            self._PAGE_URL = f"https://brusnika-qa.demo.ultimeta.ru{self._TRADES_URL}"
            print(self._PAGE_URL)
            return self._PAGE_URL

    @allure.title("Upload project classifier request")
    def upload_project_classifier(self):
        url = self.URL
        headers = self.headers
        auth = self.auth

        xml_request = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:brus="http://ultimeta.ru/schemas/brusnika-1c">
               <soapenv:Header/>
               <soapenv:Body>
                  <brus:UploadProjectClassifierRequest>
                     <brus:packageId>100</brus:packageId>
                     <brus:projectClassifiers>
                        <brus:projectClassifier>
                           <brus:id>100</brus:id>
                           <brus:code>100</brus:code>
                           <brus:title>мышь</brus:title>
                           <brus:actual>true</brus:actual>
                           <brus:contactsForWinners>99</brus:contactsForWinners>
                           <brus:address>Москва</brus:address>
                        </brus:projectClassifier>
                     </brus:projectClassifiers>
                  </brus:UploadProjectClassifierRequest>
               </soapenv:Body>
            </soapenv:Envelope>
            """

        response = requests.post(url, data=xml_request, headers=headers, auth=auth)
        # Проверка статуса
        assert response.status_code == 200, f"HTTP ошибка: {response.status_code}"
        # Проверка содержимого ответа
        assert "<ns2:success>true</ns2:success>" in response.text, "Некорректный статус в ответе!"
