# 🔖RealEstateCrawler-GoogleForms
이 프로젝트는 부동산 웹사이트에서 특정지역의 부동산 정보를 수집하고, 이를 Google Form을 활용하여 효율적으로 정리하는 프로그램입니다.

## 1. 개발 목적

부동산 시장의 빠른 변동 속에서 필요한 부동산 정보를 수집하고 정리하는 과정은 번거로움을 동반합니다. 

이에 따라, 이 프로젝트는 사용자들이 부동산 정보를 쉽게 얻고 활용할 수 있도록 하기 위해 개발되었습니다.

프로그램은 부동산 웹사이트에서 제공하는 다양한 부동산 정보를 자동으로 수집하고, 사용자가 쉽게 이해하고 활용할 수 있는 양식으로 정리하여 Google Form을 통해 전송하는 것을 목적으로 합니다. 

이를 통해 사용자는 필요한 부동산 정보를 효율적으로 얻을 수 있고, 개발자는 자동화된 시스템을 통해 시간과 노력을 절약할 수 있습니다.


## 2. 제작기간 & 참여인원

- 제작기간: 2주
- 참여인원: 1인 (개인 프로젝트)

## 3. 사용기술

- Python
- Selenium (웹 크롤링 및 자동화)
- BeautifulSoup (HTML 파싱)
- Requests (HTTP 요청)
- Google Forms (데이터 전송)
- ChromeDriverManager (웹 드라이버 관리)

## 4. 핵심 기능

프로그램은 부동산 웹사이트에서 동적으로 특정지역 주변의 원하는 부동산 정보를 크롤링하며, Selenium과 BeautifulSoup을 활용하여 페이지를 넘겨가며 자동으로 데이터를 추출합니다. 

이후, 크롤링한 정보는 Google Form에 자동으로 입력되어 사용자가 정의한 양식에 맞춰 데이터가 효율적으로 전송됩니다. 

이를 통해 사용자는 간편하게 다양한 부동산 정보를 얻을 수 있으며, 개발자는 자동화된 시스템을 통해 데이터 수집 및 정리를 더욱 효율적으로 관리할 수 있습니다.
 
 <details>
  <summary>핵심 기능 설명 펼치기</summary>

  ### 4-1. 부동산 웹사이트에서 부동산 정보 크롤링
  🔖[코드확인](https://github.com/Ahnhyeongkyu/RealEstateCrawler-GoogleForms/blob/main/main.py#L15)
     
   - 웹사이트 크롤링
     - Selenium과 BeautifulSoup을 사용하여 부동산 웹사이트에서 부동산 정보를 동적으로 크롤링합니다. 프로그램은 페이지를 넘기며 각 웹 페이지에서 필요한 정보를 수집합니다.
   
   - 데이터 추출
     - extract_data_from_page 함수는 현재 페이지의 HTML 소스를 받아와서 가격, 방의 형태, 방의 특징 등 다양한 정보를 추출합니다.
   
   - 가공 및 저장
     - 추출한 데이터는 리스트에 저장되고, 가공된 형태로 관리됩니다. 이를 통해 사용자가 쉽게 데이터를 확인하고 활용할 수 있도록 합니다.
    
  ### 4-2. Google Form에 정의된 양식에 맞게 데이터 자동 전송
  🔖[코드확인](https://github.com/Ahnhyeongkyu/RealEstateCrawler-GoogleForms/blob/main/main.py#L95)

  - Google Form 접근
    - Selenium을 활용하여 Google Form에 접근합니다. 이때, Google Form의 URL을 사용하여 프로그램이 정확한 폼에 접근할 수 있습니다.

  - 데이터 자동 입력
    - 크롤링한 데이터는 Google Form에 정의된 양식에 맞게 자동으로 입력됩니다. 각 입력 필드에 데이터를 삽입하고, 데이터가 올바르게 입력되었는지 확인하는 과정이
    자동화됩니다.

  - 자동 응답 전송
    - 데이터 입력이 완료되면 Selenium을 사용하여 제출 버튼을 클릭하여 Google Form에 자동으로 응답을 전송합니다. 이를 통해 사용자가 웹사이트를 직접 접근하지 않아도 자동으로     데이터를       전송할 수 있습니다.
  
  - 다음 응답 페이지 이동
    - Google Form은 여러 응답 페이지로 구성될 수 있습니다. 프로그램은 각 페이지의 다음 응답으로 이동하는 기능을 구현하여 다량의 데이터를 순차적으로 전송합니다.
</details>
   
## 5. 핵심 트러블 슈팅


### 5-1. 페이지 전환 및 다음 페이지 버튼 동적 처리
  
  - 문제
    - 다방 웹사이트는 동적인 페이지 구조를 가지고 있어 페이지 전환 시에 동적으로 변경되는 요소를 정확히 찾아야 합니다.   

  - 해결책
    - Selenium을 활용하여 페이지 전환 버튼의 XPath 등을 동적으로 감지하고 클릭하는 코드를 구현합니다. WebDriverWait 등을 사용하여 페이지가 완전히 로드될 때까지 대기하는 로직을 추가하여       안정성을 확보합니다.
   

### 5-2. Google Form 데이터 입력 시 대기 및 버튼 클릭 처리

  - 문제
    - Google Form의 웹 페이지는 JavaScript 등을 사용하여 동적으로 업데이트되기 때문에 데이터 입력 및 버튼 클릭 시에 대기 시간이 필요합니다.

  - 해결책
    - WebDriverWait를 활용하여 각 입력 필드나 버튼이 로드되고 활성화될 때까지 대기하는 로직을 구현합니다. 적절한 대기 시간을 설정하여 안정적으로 데이터를 입력하고 전송할 수 있도록 합니다.


### 5-3. 웹 드라이버 관련 에러 처리

 - 문제
   - 웹 드라이버의 버전이나 설정 문제로 인해 예기치 않은 에러가 발생할 수 있습니다.

- 해결책
   - ChromeDriverManager를 사용하여 항상 최신 버전의 웹 드라이버를 자동으로 다운로드하고 설정합니다.
 

## 6. 회고/느낀점

프로젝트 개발 회고 글:  https://ans-tech-blog.onrender.com/post/17


