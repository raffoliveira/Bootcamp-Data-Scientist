8-

SELECT(SUM(salario)/COUNT(*)) AS media FROM empregado
SELECT AVG(empregado.salario) AS media FROM empregado

9-

SELECT DISTINCT COUNT(*)
FROM empregado AS emp
INNER JOIN trabalha_em AS t_em
ON t_em.essn = emp.ssn
INNER JOIN projeto AS pj
ON pj.pnumero = t_em.pno
WHERE emp.dno = 5 AND pj.pjnome = 'ProjectX' AND t_em.horas > 10

SELECT DISTINCT COUNT(*)
FROM empregado AS emp
INNER JOIN departamento AS dep 
ON emp.dno = dep.dnumero
INNER JOIN projeto AS pj
ON dep.dnumero = pj.dnum 
INNER JOIN trabalha_em AS t_em
ON pj.pnumero = t_em.pno 
WHERE emp.dno = 5 AND pj.pjnome = 'ProjectX' AND t_em.horas > 10


10 -

SELECT count(emp)
FROM empregado AS emp
INNER JOIN dependente AS depe
ON emp.ssn = depe.essn
WHERE emp.pnome= depe.nome_dependente

11-

SELECT emp.pnome
FROM empregado AS emp
WHERE (SELECT emp.ssn AS resul
	   FROM empregado AS emp
	   WHERE emp.pnome LIKE 'Fra%') = emp.superssn

12 -

select emp.pnome,te.horas
FROM empregado AS emp
INNER JOIN trabalha_em AS te
ON emp.ssn = te.essn
INNER JOIN projeto AS pj
ON pj.pnumero = te.pno
where pj.pjnome = 'Newbenefits'
ORDER BY te.horas DESC

13 - 

select SUM(emp.salario)
FROM empregado AS emp
INNER JOIN departamento AS dep
ON emp.dno = dep.dnumero
where dep.dnome = 'Research'

14-

select sum(emp.salario*1.1)
FROM empregado AS emp
INNER JOIN trabalha_em AS te
ON te.essn = emp.ssn
INNER join projeto AS pj
ON pj.pnumero = te.pno
where pj.pjnome = 'ProductX'

15 -

SELECT dep.dnome, AVG(emp.salario)
FROM departamento AS dep
INNER join empregado AS emp
ON emp.dno = dep.dnumero
GROUP BY dep.dnome
ORDER BY AVG(emp.salario) ASC




