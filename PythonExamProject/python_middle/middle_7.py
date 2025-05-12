import xml.etree.ElementTree as ET
tree=ET.parse("sawon.xml")
"""
  xml = 문서형 데이터베이스 B2B, B2G, P2P, P2B
        설정파일 => 모든 언어에 호환
                  무겁다 = 실행 속도가 늦다 => JSON
        1. 호환성          
  <sawon>   =======  root : table명
      <list name="">  ==== row
          <sabun></sabun>   ==== column
          <dept></dept>
          <job></job>
          <etc year="" pay=""/>
      </list>
  </sawon>
"""
root=tree.getroot()
print(root.tag)
for child in root:
  print(child.tag,child.attrib)
for etc in root.iter('etc'):
  print(etc.attrib)
for list in root.findall('list'):
  sabun=list.find('sabun').text
  dept=list.find('dept').text
  job=list.find('job').text
  print(sabun,dept,job)
"""
  root 읽기
  root => 같은 태그 여러개 읽기 => findall
          ------------------
          | 밑에 있는 태그 : find('태그명')
          | 태그사이의 값 : text
          | 속성값 : attrib
"""