from bs4 import BeautifulSoup
import requests as req
import re

class fnguideCore:
    @staticmethod
    def getShares_flow_rate(stkCode: str) -> float:
        '''
        * function : 주식 유동비율
        '''
        fnguide_data = req.get(f"https://asp01.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{stkCode}&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN=",
                                headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", }
        )

        # FnGuide 데이터 가공
        soup = BeautifulSoup(fnguide_data.text, 'html.parser')
        extraction = soup.find('table', attrs={'class':'us_table_ty1 table-hb thbg_g h_fix zigbg_no'}).findAll('tr')[-1].find('td', attrs={'class':'cle r'}).text
        flowRate = float(re.sub(pattern='\s', repl='', string=extraction).split('/')[1]);

        return flowRate

if __name__ =='__main__':
    print(fnguideCore.getShares_flow_rate('005930'))
    pass