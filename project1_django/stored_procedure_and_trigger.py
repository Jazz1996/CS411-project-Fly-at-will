Stored Procedure:
DELIMITER //
CREATE PROCEDURE oneStop (IN deptCity nvarchar(3), arrCity nvarchar(3))
BEGIN
DROP TABLE IF EXISTS temp1;
DROP TABLE IF EXISTS temp2;
CREATE TABLE temp1 (`flight` VARCHAR(6) PRIMARY KEY,
                   `dept` VARCHAR(3),
                   `arr` VARCHAR(3),
                   `deptTime` TIME,
         `arrTime` TIME,
 `distance` INTEGER);
INSERT INTO temp1
(SELECT FlightNo, DeptIATA, ArrIATA, DeptTime, ArrTime,Distance FROM Flight WHERE DeptIATA = deptCity);
CREATE TABLE temp2 (`flight` VARCHAR(6) PRIMARY KEY,
                   `dept` VARCHAR(3),
                   `arr` VARCHAR(3),
                   `deptTime` TIME,
         `arrTime` TIME,
 `distance` INTEGER);
INSERT INTO temp2
(SELECT FlightNo, DeptIATA, ArrIATA, DeptTime, ArrTime,Distance FROM Flight WHERE ArrIATA = arrCity);
SELECT * FROM (SELECT temp1.deptTime as t1, temp1.dept AS d1, temp1.flight AS f1, temp1.arrTime as a1, temp1.arr AS at1, (temp2.deptTime - temp1.arrTime)/100 AS st, temp2.deptTime as dt2, temp2.flight AS f2, temp2.arrTime as at2, temp2.arr AS a2 FROM temp1, temp2 WHERE temp1.arr = temp2.dept AND temp2.deptTime > temp1.arrTime order by st,(temp1.distance+temp2.distance)) as rs;
END //
DELIMITER ;



Trigger:
Delimiter /
create trigger trig before insert on Flight for each row begin set @dept=(select IATACode from Airport where IATACode=new.DeptIATA); set @arr=(select IATACode from Airport where IATACode=new.ArrIATA); if @dept is NULL then insert into Airport(IATACode) value(new.DeptIATA); end if; if @arr is NULL then insert into Airport(IATACode) value(new.ArrIATA); end if; end; /
Delimiter ;

