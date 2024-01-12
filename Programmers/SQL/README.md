# SQL 문법
코딩테스트 대비 SQL 문법을 정리했습니다. 

* 코드 실행 순서 : FROM > ON > JOIN > WHERE > GROUP BY > HAVING > SELECT > ORDER BY  
STEP 1. 테이블 인식 : FROM  
STEP 2. 테이블 구조 : JOIN ON-WHERE-GROUP BY- HAVING (⭐중요)  
STEP 3. 테이블 조회 : SELECT-DISTINCT-ORDER BY-LIMIT  

### WHERE
```SQL
SELECT col1, col2 FROM table
WHERE col1 = 1;
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
SELECT col3 AS A, col4 AS B FROM table2;
```
<br/>

### DISTINCT
SELECT 절 뒤에 오는 DISTINCT는 중복을 제거해 출력할 때 사용된다. 이 함수는 NULL을 제거하고 출력하진 않는다. 
```SQL
SELECT DISTINCT col, col2
FROM table;
```
* 응용 : 고유값 개수 구하기
```sql
SELECT COUNT(DISTINCT col)
FROM table;
```
COUNT와 함께 사용해서 고유값의 개수를 구할 수 있다. 이 코드는 COUNT로 인해 NULL이 무시된다. 

<br/>

### 서브쿼리
하나의 쿼리 문장 내에 포함된 또 하나의 쿼리 문장. 반드시 괄호 안에 넣어야 한다 .메인 쿼리가 실행되기 전에 한 번 실행된다. 
1. SELECT 서브쿼리  
```SQL
SELECT 학생이름,
       (  SELECT 학과.학과이름
            FROM 학과
           WHERE 학과.학과ID = 학생.학생ID ) AS 학과이름
  FROM 학생
 WHERE 학생이름 = '홍길동' ; 
```
SELECT 절에서는 서브쿼리 결과가 반드시 단일 행, 단일 값으로 나와야 한다. 

2. FROM 서브쿼리 
```SQL
SELECT 학생이름, 수학점수
  FROM ( SELECT 학생.학생이름 AS 학생이름,
                과목.과목점수 AS 수학점수
           FROM 학생, 과목
          WHERE 학생.학생이름 = 과목.학생이름
            AND  과목.과목이름 = '수학' ) ; 
```
FROM 절에서는 서브쿼리 결과가 하나의 테이블로 나와야 한다. 왜냐하면 서브쿼리의 결과 테이블은 메인쿼리의 FROM 절에서의 테이블이 되기 때문이다. 

3. WHERE 서브쿼리(중첩쿼리)
```SQL
SELECT *
  FROM 학생
 WHERE 학생.학생이름 IN ( SELECT 과목.학생이름 FROM 과목 WHERE 과목.과목이름 = '수학' ) ;
```
자주 쓰이는 대중적인 쿼리 종류이다. WHERE 절은 서브쿼리 결과가 단일 행도 가능하고, 테이블도 가능하다. 왜냐하면 서브쿼리 결과로 메인쿼리 WHERE의 조건에서 비교하기 때문이다. 
서브 쿼리에 사용되는 컬럼값만 메인 쿼리로 전달되며, 컬럼 자체는 메인쿼리에 사용할 수 없다. 

다중행 비교연산자로 IN, ANY, ALL, SOME, EXISTS이 있다.   
__IN__ : 메인쿼리의 비교조건이 서브쿼리의 결과 중에서 하나라도 일치하면 참  
__ALL__ : 메인쿼리의 비교조건이 서브쿼리의 결과와 모든 값이 일치하면 참  
__ANY__ : 메인쿼리의 비교조건이 서브쿼리의 결과와 하나 이상 일치하면 참  
__EXISTS__ : 메인쿼리의 비교조건이 서브쿼리의 결과 중에 하나라도 만족하는 값이 존재하면 참  


<br/>

### IF 
```SQL
IF(조건문, 참일때 값, 거짓일때 값)
IFNULL(컬럼이름, null일때 바꿀 값)
```
```SQL
CASE 
    WHEN 조건1 THEN 조건1 참일 때 값
    WHEN 조건2 THEN 조건2 참일 때 값
    ELSE 위 조건 중 아무것도 만족하지 않을 때 값
END
```
IF 절은 조건문을 넣어서 참/거짓일 때 반환값을 지정하고, IFNULL은 특정 컬럼이 NULL일 때 변환될 값을 넣어준다.  
CASE WHEN은 Python의 if~elsse문과 비슷한데, WHEN으로 조건을 주고 THEN으로 조건이 만족할 때의 리턴값을 적어준다. 
ELSE는 만족하는 조건들이 없을 떄의 리턴값을 적어준다. 

<br/>

### NULL
```SQL
WHERE col IS NULL
WHERE col IS NOT NULL
```
IS NULL은 NULL인 데이터를, IS NOT NULL은 NULL이 아닌 테이터를 조회한다.

<br/>

### JOIN
1. INNER JOIN


2. LEFT JOIN


3.  RIGHT JOIN



## 응용

Q. 주문량이 많은 아이스크림들 내림차순으로 조회하기
```SQL
SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN JULY B ON A.FLAVOR = B.FLAVOR    
GROUP BY A.FLAVOR
ORDER BY A.TOTAL_ORDER+SUM(B.TOTAL_ORDER) DESC
LIMIT 3;
```
GROUP BY로 아이스크림 종류를 묶은 뒤, ORDER BY로 아이스크림 종류 별로 매출을 계산해서 내림차순하는 코드이다.


