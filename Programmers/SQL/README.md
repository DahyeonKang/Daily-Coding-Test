# SQL 문법
코딩테스트 대비 SQL 문법을 정리했습니다. 

### WHERE
```SQL
SELECT col1, col2 FROM table
WHERE col1 = 1
```
WHERE 뒤에 조건을 줌으로써 원하는 데이터를 출력할 수 있다. 또한 WHERE 뒤에 숫자일 때는 연산자가 문장일 때 IN, LIKE가 올 수 있다. IN은 여러 개의 OR을 연결한 것과 같다.   
그리고 BETWEEN AND는 이상, 이하인 조건을 한번에 묶어서 처리한다.
```SQL
WHERE col IN('A')
WHERE col IN('A','B','C')
WHERE col LIKE 'B%'
WHERE col LIKE '_C'
WHERE col BETWEEN '사성' AND '삼성'
```

<br/>

### SUM, AVG, MAX, COUNT
```SQL
SUM(col)  
AVG(col)  
MAX(col)  
COUNT(col)  
STDEV(col)
```
NULL값을 집계하지 않은 함수들이다. 순서대로 합, 평균, 최댓값, 개수, 표준편차를 구하는 함수이다.  SELECT SUM(컬럼이름) 같이 SELECT 절 뒤에서 활용할 수 있다.  
COUNT는 해당 컬럼의 행의 갯수를 출력한다. COUTN(*)는 NULL 값을 포함한 행의 수를 출력한다. 

<br/>

### ROUND, CEILING
```SQL
ROUND(수치, 반올림 자릿수)  
```
소수점, 정수에서 반올림이 가능하다.  
```SQL
CEILING(수치)  
```
소수점에서 올림이 가능하다. 소수점 이하 값이 존재하기만 하면 소수점을 버리고 1을 올림한다.

<br/>

### GROUP BY, HAVING
GROUP BY는 FROM, WHERE 절 뒤에 오고, 데이터를 작은 그룹으로 분류해 소그룹에 대해 조건을 줄 수 있다. 그룹화하기 위해 집계함수와 함께 자주 사용된다.  
HAVING은 GROUP BY에 의해 생성된 결과에서 원하는 데이터만 보는 조건을 주고 싶을 떄 사용한다. GROUP BY 절과 함께 사용된다.  
&#42;&#42; WHERE vs HAVING :WHERE은 개별 열에 대한 조건을 지정, HAVING은 그룹화된 결과에 대한 조건을 지정


* 응용: 중복값 찾아내는 방법  

1개의 컬럼일 때 
```SQL
GROUP BY col  
HAVING COUNT(col) > 1
```   
여러 컬럼일 때  
```SQL
GROUP BY col1, col2  
HAVING COUNT(*) > 1 
``` 
 * 응용: 전체 집계값을 추가하고 싶을 때 
```SQL
GROUP BY col WITH ROLLUP
```

<br/>

### ORDER BY
SELECT문에서 나온 결과를 정렬하는 함수이다. 오름차순(ASC), 내림차순(DESC)을 선택할 수 있다. 코드에서 따로 명시하지 않으면 오름차순으로 정렬된다.   

1개의 컬럼일 때  
```SQL
ORDER BY col DESC   
```
여러 컬럼일 때  
```SQL
ORDER BY col1 ASC, col2 DESC   
```

<br/>

### DATE
DATE_FORMAT은 날짜의 출력 형식을 바꿀 때 사용한다. SELECT 절에서 사용되고, 이 함수를 사용하면 컬럼 이름을 AS로 다시 설정해줘야 한다. 
```sql
SELECT DATE_FORMAT(col, '%Y-%m-%d')
```
STR_TO_DATE은 문자열을 날짜로 바꿀 때 사용한다. 
```sql
SELECT STR_TO_DATE('20080101', '%Y-%M-%D')
```
* %Y: 연도 4자리  
* %y: 연도 2자리  
* %M: 긴 월(영어, 예: July)  
* %b: 짧은 월(영어, 예: Jul)  
* %W: 긴 요일 이름(영어, 예: Monday)  
* %a: 짧은 요일 이름(영어, 예: Mon)  
* %i: 분  
* %T: hh:mm:SS  
* %m: 숫자 월(두 자리)  
* %c: 숫자 월(한 자리)  
* %d: 일자(두 자리)  
* %e: 일자(한 자리)  
* %I: 시간(12시간)  
* %H: 시간(24시간)  
* %r: hh:mm:ss AM,PM  
* %s: 초  

그리고 날짜에서 날짜 관련 값을 추출할 수 있다. 
```SQL
YEAR(col) #년
MONTH(col) #월
DAY(col) #일
HOUR(col) #시간
DAYOFWEEK(col) #요일을 숫자로(1=일요일, 2=월요일,..)
DAYNAME(col) # 요일을 영어로
QUARTER(col) #분기
```

<br/>

### UNION
여러 쿼리문을 하나로 합쳐 하나의 쿼리문으로 만들어주는 함수다. UNION은 중복된 값을 제거해 출력하고, UNION ALL은 중복된 값을 제거하지 않고 모두 출력한다.   
UNION을 사용하려면 컬럼명 동일(같지 않으면 AS로 동일하게 맞춰줘야 함), 컬럼의 데이터 타입 동일, 출력할 컬럼 개수가 동일해야 한다.   
** UNION vs JOIN : UNION은 수직결합, JOIN은 수평결합이다.

```SQL
SELECT col1AS A, col2 AS B FROM table1  
UNION
SELECT col3 AS A, col4 AS B FROM table2
```
<br/>


