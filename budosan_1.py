import streamlit as st
import requests
import pandas as pd

# API 요청에 필요한 쿠키와 헤더
cookies = {
    'ASID': '0e31e09b0000019033f1859200000050',
    'tooltipDisplayed': 'true',
    'NFS': '2',
    'NAC': 'xYu0BYQPudzW',
    'NNB': 'P45U3RK5XHOGO',
    'page_uid': 'i+4eedqVOZossZuP71Vssssssks-040630',
    'NID_AUT': 'Zzvx+1I93Ff3+wAE90cOOpJw0d6V+hxi+q0CrjxtOi1lMAfxVsGSimvgRYxbb664',
    'NID_SES': 'AAAB1XyniS/bP+0ewxtGjthTw+QZRkhOBKL/uE4jWNhK+wQtlo9s/T+B4ODbsxMIjU4CjAGoiT6o0FTMeVuxZd88Ws4Cl8C0joOPc3Ep/L/5759Weo9GpIspoS2+ZawdiYj3NfZdWpITXb5nAz9J1NCcw8WecUK+y9fc5FPKpiJcndzHFGGmZIXiMCI698ez9SmQCQpeuk6lv+6VmHaeoODwOPry19PLPLkna2kmXbb7yMp+HQpBg98xXS5gZdQid8oYQAUHg2wX2cdX2m5r3uQMT184+ZdZdBAufJwgdxZwlhfEyZK0G3inxzitOhEUaQtUS9o/JaHjUFvG4VH2Z6jnxFcuuyPLdN5g13EUw9+Kqf62WdlPuh2KMGZcEJBr7S3DGRZSsZpPWaMiq4i++RI+/IwqPYtPD3/MrO6ho8iG0wpBj8XIsD7lyoNE7gZfjsC6LfSM7W3+pq7YytkH8Gi4Qe7q5tu05Z9Ge14bJL5+/7dyrx04O6F5EEz+PrF02YMmA9XuMrAwUYJy+kgXRRpySM8MQf5atf2OkTczuaZx5XfAgraJH4OOoDYu7rnaovntb8MfhdQ8uC7nfbHbelFtFsbbnVD+l+nXigx7XkNMLKbv8hLXpTFed/8M1qtAN+mV3A==',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '5000000000',
    '_fwb': '140aY0iMIOzFmNW0s24v96q.1743048110600',
    'landHomeFlashUseYn': 'Y',
    'NACT': '1',
    '_fwb': '140aY0iMIOzFmNW0s24v96q.1743048110600',
    'SRT30': '1743049976',
    'SRT5': '1743049976',
    'REALESTATE': 'Thu%20Mar%2027%202025%2013%3A34%3A02%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'BUC': 'YujeCaEwgAb5hON9Iujzes7Gjc3pTNJwm_gyNZi8REY=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDMwNTAwNDIsImV4cCI6MTc0MzA2MDg0Mn0.oJPN-KM0LMO9Qd33o0lt0a6iKJN0LzHYfPCaMs9Os30',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/complexes/10203?ms=37.3651519,127.105399,16&a=APT:ABYG:JGC:PRE&e=RETAIL',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

base_url = 'https://new.land.naver.com/api/articles/complex/153998?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&complexNo=153998&buildingNos=&areaNos=&type=list&order=rank'

# API 요청 함수
def fetch_articles():
    all_articles = []
    for page in range(1, 11):  # 1페이지부터 10페이지까지 반복
        url = f"{base_url}&page={page}"  # 페이지 번호 추가
        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        )
        if response.status_code == 200:
            data = response.json()
            if "articleList" in data:
                articles = data["articleList"]
                if articles:
                    all_articles.extend(articles)
                else:
                    st.warning(f"No articles found on page {page}.")
            else:
                st.error(f"The 'articleList' key was not found in the JSON response for page {page}.")
        else:
            st.error(f"Failed to fetch data for page {page}. HTTP Status Code: {response.status_code}")
    return all_articles

# Streamlit UI 구성
st.title("부동산 매물 정보")
st.write("API를 통해 부동산 매물 정보를 가져옵니다.")

# 매물 데이터 가져오기 버튼
if st.button("매물 불러오기"):
    with st.spinner("매물 정보를 불러오는 중..."):
        articles = fetch_articles()
        if articles:
            # 데이터를 DataFrame으로 변환
            df = pd.DataFrame(articles)

            # price 필드가 문자열일 경우 숫자로 변환
            if 'price' in df.columns:
                df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)

            # 주요 정보 요약
            st.subheader("요약 정보")
            total_articles = len(df)
            avg_price = df['price'].mean() if 'price' in df.columns else 0
            st.metric(label="총 매물 수", value=total_articles)
            st.metric(label="평균 가격", value=f"{avg_price:,.0f} 원")

            # 매물 테이블 표시
            st.subheader("매물 목록")
            if not df.empty:
                st.dataframe(df)
            else:
                st.warning("표시할 매물 데이터가 없습니다.")
        else:
            st.warning("매물 정보를 찾을 수 없습니다.")