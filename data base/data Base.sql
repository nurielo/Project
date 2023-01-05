--DROP TABLE CUSTOMERS
CREATE TABLE CUSTOMERS(
[E-mail]	varchar(40)		not null,
Password	varchar(20)		not null,
[First Name]	varchar(20)		not null,
[Last Name]		varchar(20)		not null,
Gender		char(1)			not null,
Language	varchar(7)		default 'English',
Currency	varchar(20)		default 'US Dollar'
	constraint		pk_email		primary key	([E-mail]),
	constraint		ck_language		check(Language in('English','Spanish')),
	constraint		ck_email		check ([E-mail] like '%@%.%'),
	constraint		ck_Pass		check(DATALENGTH(Password) >= 8)
)



--DROP TABLE ITEMS
CREATE TABLE ITEMS(
[Item ID]	varchar(40)		not null,
Name		varchar(100)	not null,
Brand		varchar(20)		not null,
Category	varchar(20)		not null,
Price		decimal(10,2)	not null ,
Description		varchar(256)	not null,
Image		varchar(100)	not null,
[In Stock]	bit		not null,
[New release]	bit		not null,
	constraint	PK_ITEMS	PRIMARY KEY([Item ID]),
	constraint	ck_image	check(Image like '%.jpg'),	
	constraint	ck_ItemID	check ([Item ID] like 'BH#%')
)

--DROP TABLE PAYMENTS
CREATE TABLE PAYMENTS(
[CC number]		varchar(18)		not null, 
[CC exp date]	date	not null, 
CVV			char(3)			not null, 
	constraint PK_Payment PRIMARY KEY ([CC number]),
	constraint ck_ExpDate check (year([CC exp date])>=2020 and year([CC exp date])<=2026),
	constraint ck_cvv check (CVV like '[0-9][0-9][0-9]'),
	constraint ck_CCnumInt check ([CC number] like '%[0-9]%' )
)
--delete from PAYMENTS 
--ALTER TABLE PAYS_THROUGH
--DROP TABLE  PAYS_THROUGH
CREATE TABLE PAYS_THROUGH (
[E-mail]	varchar(40)		not null,
[CC number]		varchar(16)		not null, 
	constraint PK_Payment1 PRIMARY KEY ([E-mail],[CC number])
)

--DROP TABLE NOT_CUSTOMERS 
CREATE TABLE NOT_CUSTOMERS (
[E-mail_NC]		varchar(40)		not null,
[First name]	varchar(20)		not null, 
[Last name]		varchar(20)		not null, 
	constraint PK_NOT_CUSTOMERS PRIMARY KEY ([E-mail_NC])
)

--DROP TABLE DELIVERIES 
CREATE TABLE DELIVERIES (
[Address–Country]	varchar(20)		not null, 
[Delivery Type]		varchar(20)		not null, 
[Delivery Price]	decimal(10,2)	not null, 
	constraint PK_DELIVERIES PRIMARY KEY ([Address–Country],[Delivery Type])
)

--DROP TABLE ORDERS
CREATE TABLE ORDERS (
[Purchase ID]	int		not null, 
[E-mail_NC]	varchar(40)		null, 
[E-mail]	varchar(40)		null , 
[Address–Country]	varchar(20)		not null, 
[Delivery Type]		varchar(20)		not null, 
[Address–State]		varchar(20)		not null, 
[Address–City]		varchar(20)		not null, 
[Address–Street]	varchar(20)		not null, 
[Address–Building]	varchar(10)		not null, 
[Address–Apartment]	varchar(10)		not null, 
[Zip Code]		char(7)		not null , 
[Order DT]		Date	not null, 
[CC number]		varchar(18)		not null, 
	constraint PK_Order PRIMARY KEY ([Purchase ID]),
	constraint FK_order FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail]),
	constraint FK_order2 FOREIGN KEY ([CC number]) references PAYMENTS([CC number]),
	constraint FK_order3 FOREIGN KEY ([E-mail_NC]) references NOT_CUSTOMERS([E-mail_NC]),
	constraint FK_order4 FOREIGN KEY ([Address–Country],[Delivery Type]) references DELIVERIES([Address–Country],[Delivery Type])
)

--DROP TABLE ORDERS_PHONES
CREATE TABLE ORDERS_PHONES(
[Purchase ID]	int		not null, 
[Phone Number]	varchar(20)	not null,
	constraint PK_Phones PRIMARY KEY ([Phone Number],[Purchase ID]),
	constraint FK_Phones FOREIGN KEY ([Purchase ID]) references ORDERS([Purchase ID]),
	constraint ch_phon_form check ([Phone Number] like '+%'),
	constraint ch_phon_length check (datalength([Phone Number])>=11 and datalength([Phone Number])<=20 )
)

--DROP TABLE REVIEWS
CREATE TABLE REVIEWS(
[E-mail]	varchar(40)		not null, 
DT			DATETIME		not null,
[Item ID]	varchar(40)		not null, 
Content		varchar(256)	null, 
stars	int		null,
[Verified Buyer]	bit		not null,
	constraint PK_Reviews PRIMARY KEY (DT,[E-mail]),
	constraint FK_Reviews FOREIGN KEY  ([E-mail]) references CUSTOMERS([E-mail]),
	constraint FK_Reviews_2 FOREIGN KEY ([Item ID]) references ITEMS([Item ID]),
	constraint ch_stars check (Stars>=1 and Stars<=5)
)

--DROP TABLE WISH_LISTS
CREATE TABLE WISH_LISTS(
[E-mail]	varchar(40)		not null, 
[Wish-List number]	int		not null, 
[DT creation]	datetime	not null, 
[List Name]		varchar(20)		default 'Untitled', 
Privacy			varchar(10)		default 'Private',
	constraint PK_Wish_List PRIMARY KEY ([E-mail],[Wish-List number]),
	constraint FK_wish FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail]),
	constraint ck_Privacy check (Privacy in('Private','Public'))
)

--DROP TABLE ADDS
CREATE TABLE ADDS(
[E-mail]	varchar(40)		not null, 
[Wish-List number]	int		not null,
[Item ID]	varchar(40)		not null, 
DT			datetime		not null, 
	constraint PK_ADDS PRIMARY KEY ([Wish-List number],[E-mail],[Item ID]),
	constraint FK_Adds FOREIGN KEY ([E-mail],[Wish-List number]) references WISH_LISTS([E-mail],[Wish-List number]),
	constraint FK_Adds1 FOREIGN KEY ([Item ID]) references ITEMS([Item ID])
)

--DROP TABLE QUESTIONS
CREATE TABLE QUESTIONS(
[Item ID]	varchar(40)		not null,  
[Question number] int not null, 
DT datetime not null, 
[Content–Question] varchar(256) not null, 
[E-mail] varchar(40) not null,
constraint PK_Question PRIMARY KEY ([Item ID],[Question number]),
constraint FK_Question FOREIGN KEY ([Item ID]) references ITEMS([Item ID]),
constraint FK_Question_2 FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail])
)

--DROP TABLE ANSWERS
CREATE TABLE ANSWERS(
[Item ID]	varchar(40)		not null,
[Question number] int not null, 
DT datetime not null, 
[Content–Answer] varchar(256) not null, 
[E-mail] varchar(40) not null,
	constraint PK_Answer PRIMARY KEY (DT,[Item ID], [Question number]),
	constraint FK_Answer FOREIGN KEY ([Item ID], [Question number]) references QUESTIONS([Item ID],[Question number]),
	constraint FK_Answer_2 FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail])
)

--DROP TABLE RECENTLY_VIEWED
CREATE TABLE RECENTLY_VIEWED(
[E-mail] varchar(40) not null, 
[Item ID]	varchar(40)		not null, 
DT datetime not null,
	constraint PK_RV PRIMARY KEY ([E-mail],[Item ID]),
	constraint FK_RVCust FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail]),
	constraint FK_RV_2 FOREIGN KEY ([Item ID]) references ITEMS([Item ID])
)

--DROP TABLE INCLUDES
CREATE TABLE INCLUDES(
[Purchase ID]	int		not null,
[Item ID]	varchar(40)		not null,
Quantity	int		default 1,
	constraint PK_includes PRIMARY KEY ([Purchase ID],[Item ID]),
	constraint FK_includes FOREIGN KEY ([Purchase ID]) references ORDERS([Purchase ID]),
	constraint FK_ItemIn FOREIGN KEY ([Item ID]) references ITEMS([Item ID]),
	constraint ck_Quantity check(Quantity>0)
)

--DROP TABLE SEARCHES
CREATE TABLE SEARCHES(
[IP Address]	varchar(20)		not null, 
DT	datetime	not null, 
[Free text]		varchar(256)	null,
Category		varchar(20)		null, 
Brand			varchar(20)		null, 
[In Stock]		bit		null, 
Stars	int		null, 
Price	decimal(10,2)	null, 
[New release]	bit		null,
[E-mail]	varchar(40)		null, 
	constraint PK_Search PRIMARY KEY ([IP Address],DT),
	constraint FK_search FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail]),
	constraint ck_freetext check(datalength([Free text])>=2),
	constraint ch_IP check ([IP Address] like '%.%.%.%'),
	constraint CK_one_is_not_null CHECK (COALESCE([Free text],Category) IS NOT NULL )
)


--DROP TABLE RESULTS
CREATE TABLE RESULTS(
[IP Address]	varchar(20)		not null, 
DT	datetime	not null, 
[Item ID]	varchar(40)		not null,
	constraint PK_Results PRIMARY KEY ([IP Address],DT,[Item ID]),
	constraint FK_Results FOREIGN KEY ([IP Address], DT) references SEARCHES([IP Address], DT),
	constraint FK_Results2 FOREIGN KEY ([Item ID]) references ITEMS([Item ID])
)

--task 1-
--first simple Query
SELECT C.[E-mail], [First Name], [Last Name], CountItems=count(Quantity)
FROM Customers C join Orders O on C.[E-mail]=O.[E-mail] 
		join Includes I on O.[Purchase ID]=I.[Purchase ID]
WHERE DATEDIFF(month, O.[Order DT], getDate()) <=6
Group by C.[E-mail], [First Name], [Last Name]
Order by CountItems desc

-- second simple Query
SELECT top 10  Category, [E-mail]=C.[E-mail]  , [First Name], [Last Name], countBuzz=count(C.[E-mail])
FROM  Answers A join Customers C on A.[E-mail]=C.[E-mail]
		join Items I on A.[Item ID]=I.[Item ID]

Group by Category,C.[E-mail]  , [First Name], [Last Name]
Order by countBuzz desc

--first nested Query
SELECT top 10 [Item ID],
              [view count],
			  [cost last year] = case
			  when[total Quantity] is NULL then  0
			  else [total Quantity]*Price
			  end
FROM ITEMS i join (select  orderIDT=[Item ID], [view count]=COUNT(*)
                   from RECENTLY_VIEWED
				   group by [Item ID] ) b 
					on i.[Item ID]=b.orderIDT  
						left join (SELECT  IncludesODT=[Item ID],
						                [total Quantity]=sum( Quantity) 
	from ORDERS o  join INCLUDES i on o.[Purchase ID]=i.[Purchase ID]
				where o.[Order DT]> DATEADD(YEAR, -1, GETDATE())   
							  group by [Item ID])c
							  on b.orderIDT=c.IncludesODT  
order by [view count] desc

-- second nested Query
select [Address–Country]
from ORDERS o join(select id=[Purchase ID], [num in orders]=sum(Quantity)
                    from INCLUDES 
					group by [Purchase ID])itemo on o.[Purchase ID]=itemo.id
group by [Address–Country]
having sum([num in orders])>=(select max(total)
								from (select [Address–Country],total=sum([num in orders])
								from ORDERS o join(select id=[Purchase ID], [num in orders]=sum(Quantity)
													from INCLUDES 
													group by [Purchase ID])itemo on o.[Purchase ID]=itemo.id
								group by [Address–Country]) as t1)

--first nested Query with other tools
alter table customers add Vital bit
alter table customers drop column Vital

update CUSTOMERS
set Vital = (case when [E-mail] in (select distinct ans.[E-mail]
									from (select [E-mail],num_of_answers=count(*)
											from ANSWERS
											group by [E-mail]) as ans join REVIEWS as r on ans.[E-mail]=r.[E-mail] join (select [E-mail],num_of_orders=count(*)
																											from ORDERS
																											where [E-mail] <> 'NULL'
																											group by [E-mail]) as o on o.[E-mail]=r.[E-mail]
									where num_of_orders>=1 AND (stars>=4 OR num_of_answers>5)) then 1 else 0 end)

select * from CUSTOMERS
--second nested Query with other tools
select distinct t1.[Item ID]
from (select distinct [E-mail],i.[Item ID]
from ORDERS as o join INCLUDES as i on o.[Purchase ID]=i.[Purchase ID]
where [E-mail]<>'NULL' AND (select count(*)
							from RECENTLY_VIEWED as r
							where r.[Item ID]=i.[Item ID])>4
group by [E-mail],i.[Item ID]) as t1
intersect
select distinct t2.[Item ID]
from (select distinct [E-mail_NC],i.[Item ID]
from ORDERS as o join INCLUDES as i on o.[Purchase ID]=i.[Purchase ID]
where [E-mail_NC]<>'NULL'
group by [E-mail_NC],i.[Item ID]) as t2

--task  2
--view 
CREATE VIEW  [more orders details] AS
select o.[Purchase ID] ,[order cost]= sum(total), [items count]=sum(Quantity)
from ORDERS o join (select itemID=[Purchase ID] ,i.Quantity,(Price*Quantity) as total  
                    from INCLUDES i join (select [Item ID], price
				                          from ITEMS)b                            
			                              on i.[Item ID]=b.[Item ID])  d
	                on o.[Purchase ID]= d.itemID
group by o.[Purchase ID]
--example
SELECT * FROM [more orders details]


--function 1
CREATE FUNCTION dbo.Calculate_Relative_Income (@Country varchar(30))
RETURNS real
AS
	BEGIN
		DECLARE @L_Income float 
		DECLARE @L_totalIncome float 
	  

		SET @L_Income = (SELECT SUM(Price*Quantity)
		FROM Includes I join Orders O on I.[Purchase ID]=O.[Purchase ID] 
				join Items on I.[Item ID]=Items.[Item ID]
		WHERE [Address–Country]=@Country)

	
		SET @L_totalIncome = (SELECT sum(Price*Quantity)
		FROM Includes I join Items on I.[Item ID]=Items.[Item ID])


		RETURN CASE
					WHEN @L_Income = 0 THEN 0
					WHEN @L_Income > 0 THEN (@L_Income/@L_totalIncome)*100
				END
	END
--Demonstration 
select [Address–Country],  Relative_Income=dbo.Calculate_Relative_Income('Argentina')
from Orders
WHERE [Address–Country]='Argentina'
union
select [Address–Country],  Relative_Income=dbo.Calculate_Relative_Income('Brazil')
from Orders
WHERE [Address–Country]='Brazil'
union
select [Address–Country],  Relative_Income=dbo.Calculate_Relative_Income('Israel')
from Orders
WHERE [Address–Country]='Israel'

--function 2

CREATE FUNCTION dbo.WishList_Vs_Purchases (@Costumer_Email varchar(30))
RETURNS TABLE
AS
	RETURN
	SELECT A.[Item ID], I.Name, Price, Payment = (Price*Quantity),Date_Gap_Year=(year(O.[Order DT])-year(A.DT)), Date_Gap_Month=(month(O.[Order DT])-month(A.DT)),
			 Date_Gap_Day=(day(O.[Order DT])-day(A.DT))
	FROM Customers as C join ADDS as A on C.[E-mail]= A.[E-mail] left join INCLUDES as INC on A.[Item ID]=INC.[Item ID] 
		join ITEMS as I on INC.[Item ID]=I.[Item ID] join ORDERS as O on INC.[Purchase ID]=O.[Purchase ID]
	WHERE C.[E-mail] = @Costumer_Email

--example
select * from dbo.WishList_Vs_Purchases ('cwyld4@spotify.com')

--simple trigger
--alter table orders drop column Total_Cost
alter table orders add Total_Cost decimal(10,2)

update ORDERS
set Total_Cost = (select Total
				 from (select ord.[Purchase ID],Total = t1.cost+d.[Delivery Price]
from ORDERS as ord join (select inc.[Purchase ID], cost = sum(inc.Quantity*it.Price)
						from INCLUDES as inc join ITEMS as it on it.[Item ID]=inc.[Item ID]
						group by inc.[Purchase ID]) as t1 on t1.[Purchase ID]=ord.[Purchase ID] join DELIVERIES as d on ord.[Address–Country]=d.[Address–Country] and ord.[Delivery Type]=d.[Delivery Type]) as ttc
				 where orders.[Purchase ID]=ttc.[Purchase ID])
select * from ORDERS
--drop TRIGGER Update_Total_Cost

CREATE TRIGGER Update_Total_Cost
on includes
after insert
as
update ORDERS
set Total_Cost = (case when ORDERS.[Purchase ID] in (select [Purchase ID] from inserted) then (select Total
from inserted join (select ord.[Purchase ID],Total = t1.cost+d.[Delivery Price]
from ORDERS as ord join (select inc.[Purchase ID], cost = sum(inc.Quantity*it.Price)
						from INCLUDES as inc join ITEMS as it on it.[Item ID]=inc.[Item ID]
						group by inc.[Purchase ID]) as t1 on t1.[Purchase ID]=ord.[Purchase ID] join DELIVERIES as d on ord.[Address–Country]=d.[Address–Country] and ord.[Delivery Type]=d.[Delivery Type]) as t2 on t2.[Purchase ID]=inserted.[Purchase ID]
where ORDERS.[Purchase ID]=inserted.[Purchase ID]) else Total_Cost end)


------Exmp-------

insert into ORDERS ([Purchase ID],[E-mail],[Address–Country],[Delivery Type],[Address–State],[Address–City],[Address–Street],[Address–Building],[Address–Apartment],[Zip Code],[Order DT],[CC number]) values (306,'challe0@jalbum.net','Argentina','VIP','Virginia','Carlos Casares','Schmedeman','684','748','163','2019-02-10 10:13:09','4916320112667890')
insert into INCLUDES ([Purchase ID], [Item ID], Quantity) values(306,'BH#3',5)
insert into INCLUDES ([Purchase ID], [Item ID], Quantity) values(306,'BH#10',5)

delete from INCLUDES
where [Purchase ID] = 306

delete from ORDERS
where [Purchase ID]=306

select *
from ORDERS
where [Purchase ID]=306

-- Stored Procedure
CREATE PROCEDURE SP_UpdateDeliveryType @PID int, @Type varchar(20)
AS
select o.[Purchase ID],o.[Delivery Type],d.[Delivery Price]
from ORDERS as o join DELIVERIES as d on o.[Address–Country]=d.[Address–Country] and o.[Delivery Type]=d.[Delivery Type]
where [Purchase ID]=@PID
update ORDERS
set [Delivery Type] = @Type
where [Purchase ID] = @PID
select o.[Purchase ID],o.[Delivery Type],d.[Delivery Price]
from ORDERS as o join DELIVERIES as d on o.[Address–Country]=d.[Address–Country] and o.[Delivery Type]=d.[Delivery Type]
where [Purchase ID]=@PID

--example
exec SP_UpdateDeliveryType 1,'VIP'
exec SP_UpdateDeliveryType 1,'Express'

--task 3 
--view Revenue by brand
create view [Revenue by brand] as
select Brand,[total brand price]=sum([item Quantity price])
from ITEMS for_brand   right join (select i.[Item ID], [item Quantity price]=[items count]*Price
                                   from ITEMS i  right join (select [Item ID],[items count]=sum(Quantity)
                                                             from INCLUDES
													         group by [Item ID] )b
										              on i.[Item ID]=b.[Item ID]
				                          )f
				   on f.[Item ID]=for_brand.[Item ID]
group by Brand

select * from [Revenue by brand]


--task 4
----complicated tool-----
---function that calculate the average stars of each item---

--DROP FUNCTION AvgStars

CREATE FUNCTION AvgStars (@itemID varchar(40))
returns int
as begin 
declare @ans int
select @ans=AVG(stars)
from REVIEWS 
where [Item ID]=@itemID
return @ans
end

---function that calculate the number of purchases for each item---

--DROP FUNCTION NumberOfPurchases

CREATE FUNCTION NumberOfPurchases (@itemID varchar(40))
returns int
as begin 
declare @ans int
select @ans=t1.numberofpurchases
from (select [Item ID],numberofpurchases=count([Purchase ID])
	from INCLUDES
	where [Item ID]=@itemID
	group by [Item ID]) as t1
return @ans
end

---add a column to ITEMS(Rank)+(Discount)---

alter table ITEMS
add Rank varchar(20)
alter table ITEMS
add Discount real 
-- alter table ITEMS drop column Rank
-- alter table ITEMS drop column Discount
---view avg of purchases---

--drop view V_avgpurchases
create view V_avgpurchases
as
select avgp=avg(t1.numberofpurchases)
from (select [Item ID],numberofpurchases=count([Purchase ID])
	from INCLUDES
	group by [Item ID]) as t1

---view avg of stars---

--drop view V_avgstars
create view V_avgstars
as
select avgs=AVG(stars)
from REVIEWS

---SP_rank---

create procedure SetItemRank @itemID varchar(40), @Rank varchar(20)
as
update ITEMS
set Rank=@Rank
where [Item ID]=@itemID

---SP_discount---

create procedure SetItemDiscount @itemID varchar(40), @Discount real
as
update ITEMS
set Discount=@Discount
where [Item ID]=@itemID

---updating---

update ITEMS
set Rank=(case 
when dbo.AvgStars(ITEMS.[Item ID])>(select avgs from V_avgstars)*2 OR dbo.NumberOfPurchases(ITEMS.[Item ID])>(select avgp from V_avgpurchases)*2 then 'Best Seller'
when dbo.AvgStars(ITEMS.[Item ID])>(select avgs from V_avgstars) AND dbo.AvgStars(ITEMS.[Item ID])<=(select avgs from V_avgstars)*2
OR dbo.NumberOfPurchases(ITEMS.[Item ID])>(select avgp from V_avgpurchases) AND dbo.NumberOfPurchases(ITEMS.[Item ID])<=(select avgp from V_avgpurchases)*2 then 'Great Choice' 
when dbo.AvgStars(ITEMS.[Item ID])=(select avgs from V_avgstars) OR dbo.NumberOfPurchases(ITEMS.[Item ID])=(select avgp from V_avgpurchases) then 'Average Product' 
when dbo.AvgStars(ITEMS.[Item ID])<(select avgs from V_avgstars) OR dbo.NumberOfPurchases(ITEMS.[Item ID])<(select avgp from V_avgpurchases) then 'Bad One' end)

update ITEMS
set Discount=(case
when rank is null then NULL
when rank = 'Bad One' then 0.25
end)


---Trigger---
--drop trigger updateItemsRank
create trigger updateItemsRank
on reviews
for insert
as
declare @itemID varchar(40)

begin

if CURSOR_STATUS('global','i_cursor')>=-1
begin
	deallocate i_cursor
end

declare i_cursor cursor for
select [Item ID]
from inserted

open i_cursor
fetch next from i_cursor
into @itemID

while (@@FETCH_STATUS=0)
begin
if dbo.AvgStars(@itemID)>(select avgs from V_avgstars)*2 OR dbo.NumberOfPurchases(@itemID)>(select avgp from V_avgpurchases)*2 begin 
exec SetItemRank @itemID,'Best Seller'
exec SetItemDiscount @itemID,NULL  end

else if dbo.AvgStars(@itemID)>(select avgs from V_avgstars) AND dbo.AvgStars(@itemID)<=(select avgs from V_avgstars)*2
OR dbo.NumberOfPurchases(@itemID)>(select avgp from V_avgpurchases) AND dbo.NumberOfPurchases(@itemID)<=(select avgp from V_avgpurchases)*2 begin
exec SetItemRank @itemID,'Great Choice'
exec SetItemDiscount @itemID,NULL  end

else if dbo.AvgStars(@itemID)=(select avgs from V_avgstars) OR dbo.NumberOfPurchases(@itemID)=(select avgp from V_avgpurchases) begin 
exec SetItemRank @itemID,'Average Product'
exec SetItemDiscount @itemID,NULL  end

else begin 
exec SetItemRank @itemID,'Bad One'
exec SetItemDiscount @itemID,0.25  
print 'An Item just need a push, a discount was added :)'; end



fetch next from i_cursor
into @itemID


end
close i_cursor
end


--example--
---'BH#350'---
insert into REVIEWS values ('mmouat1x@vk.com','2016-03-19 09:13:42.000','BH#350','Toxic effect of latex, intentional self-harm',5,0)

insert into REVIEWS values ('koldacre7@ihg.com','2016-09-28 13:18:40.000','BH#350','Disp fx of medial phalanx of r mid finger, init for opn fx',1,1)
insert into REVIEWS values ('koldacre7@ihg.com','2016-09-28 12:18:41.000','BH#350','Disp fx of medial phalanx of r mid finger, init for opn fx',1,1)
insert into REVIEWS values ('koldacre7@ihg.com','2016-09-28 12:14:41.000','BH#350','Disp fx of medial phalanx of r mid finger, init for opn fx',1,1)
insert into REVIEWS values ('koldacre7@ihg.com','2016-09-28 12:12:41.000','BH#350','Disp fx of medial phalanx of r mid finger, init for opn fx',1,1)


delete from reviews where [Item ID]='BH#350'

-- Systemic of several tools
Create Table Messages_to_Customers(
[E-mail]	varchar (40)	not null,
Regarding	varchar (40)	not null, 

	constraint	PK_Messages	primary key	([E-mail]),
	constraint FK_Messages FOREIGN KEY ([E-mail]) references CUSTOMERS([E-mail])
)
--DROP TABLE  Messages_to_Customers

CREATE TRIGGER 	Notify_Customers
ON 		dbo.ITEMS
FOR    UPDATE
AS
	DECLARE @ItemID varchar(40)
	DECLARE @EMAIL varchar(40)
 BEGIN 
	IF CURSOR_STATUS('global','C1')>=-1
	BEGIN
		DEALLOCATE C1
	END

	DECLARE C1 CURSOR FOR 
	SELECT [E-mail],ADDS.[Item ID]
	FROM ((SELECT [Item ID] FROM INSERTED UNION SELECT [Item ID] FROM DELETED)  AS UN
	 join ADDS on UN.[Item ID] = ADDS.[Item ID])

	OPEN C1
	FETCH  NEXT  FROM C1 INTO @EMAIL, @ItemID
	WHILE (@@FETCH_STATUS = 0)
		BEGIN 
		INSERT 	INTO 	dbo.Messages_to_Customers
		SELECT		@EMAIL,Regarding=@ItemID
		FETCH NEXT FROM C1
		Into @EMAIL, @ItemID
		END 
		CLOSE C1
		DEALLOCATE C1

	END


CREATE PROCEDURE  SP_update_Items_to_Discount 
  	@dis_per_month	 real, @num_of_months int
AS
DECLARE @ITEMid varchar(40)
DECLARE C1 CURSOR FOR
	SELECT [Item ID] FROM ITEMS
	BEGIN
	OPEN C1
	FETCH  NEXT  FROM C1 INTO @ITEMid
	WHILE (@@FETCH_STATUS = 0)
		BEGIN 
		UPDATE ITEMS
			 SET ITEMS.Price = ITEMS.Price-ITEMS.Price*@dis_per_month*To_discount_table.[dead months] 
			 from dbo.To_discount_table(@num_of_months)
			 where ITEMS.[Item ID]= @ITEMid
	
	FETCH NEXT FROM C1
		Into @ITEMid
		END 
		CLOSE C1
		DEALLOCATE C1
		END


CREATE 	FUNCTION    To_discount_table(@num_of_months int) 
	RETURNS 	TABLE
	AS
		RETURN
			SELECT [Item ID], [Last perchase], DATEDIFF(month,R.[Last perchase],getdate()) [dead months]
			FROM (select  [Item ID], max([Order DT]) [Last perchase]
				from INCLUDES I join Orders O on I.[Purchase ID]=O.[Purchase ID]
				group by [Item ID]) AS R
			WHERE DATEDIFF(month,R.[Last perchase],getdate())>@num_of_months 
		group by [Item ID], [Last perchase]

--example

EXEC SP_update_Items_to_Discount 0.01, 6
select * from Messages_to_Customers


----Year By Month  Report

--Basic Functions of Orders according to months

--Function calculates the average number of items sold on a certain month through certain years
CREATE 	FUNCTION    dbo.num_sales_per_month(@month date,@start_year date,@end_year date) 
RETURNS 	real
AS
	BEGIN
		DECLARE @L_num_sales int
		DECLARE @L_yearDiff int 
		
		SET @L_yearDiff = DATEDIFF(yy, @start_year ,@end_year)
		SET @L_num_sales = (SELECT count(*) FROM (SELECT [Item ID]
			FROM dbo.INCLUDES I join dbo.Orders O on I.[Purchase ID]=O.[Purchase ID]
		
			WHERE month([Order DT])=month(@month) and 
				  year([Order DT])>=year(@start_year) and 
				  year([Order DT])<=year(@end_year) ) AS IT)

		RETURN CASE
					WHEN @L_yearDiff = 0 THEN @L_num_sales
					WHEN @L_yearDiff > 0 THEN @L_num_sales/(@L_yearDiff+1)
			END	
	END

--Function calculates the monthly sales rate out of the annual sales
CREATE 	FUNCTION    dbo.monthly_rate(@month date,@start_year date,@end_year date) 
RETURNS 	varchar(8)
AS
	BEGIN
		DECLARE @L_total_sales DOUBLE PRECISION
		DECLARE @L_monthly_sales DOUBLE PRECISION
		DECLARE @L_monthly_sales1 DOUBLE PRECISION
		DECLARE @L_yearDiff int 
		
		SET @L_yearDiff = DATEDIFF(yy, @start_year ,@end_year)
		SET @L_total_sales = (SELECT count(*) FROM (SELECT [Item ID]
			FROM dbo.INCLUDES I join dbo.Orders O on I.[Purchase ID]=O.[Purchase ID]
			WHERE  year([Order DT])>=year(@start_year) and 
				   year([Order DT])<=year(@end_year) ) AS TOT)

		 SET @L_monthly_sales = @L_yearDiff*dbo.num_sales_per_month(@month, @start_year, @end_year)
		 SET @L_monthly_sales1 = dbo.num_sales_per_month(@month, @start_year, @end_year)
			
		RETURN CASE	
		 WHEN @L_yearDiff > 0 THEN
			cast(cast(@L_monthly_sales/@L_total_sales*100 as decimal(18,2)) as varchar(5)) +'%'  	
		 WHEN @L_yearDiff = 0 THEN
			cast(cast(@L_monthly_sales1/@L_total_sales*100 as decimal(18,2)) as varchar(5)) +'%'	
		END
	END

CREATE 	FUNCTION    dbo.top_category(@month date,@year date) 
RETURNS 	varchar(30)  
AS
	BEGIN
		DECLARE @L_top varchar(30)
		
		SET @L_top = (SELECT top 1 T_cat.Category FROM (
		SELECT Category, [Order DT]
			FROM dbo.INCLUDES I join dbo.Orders O on I.[Purchase ID]=O.[Purchase ID] 
				join Items IT on I.[Item ID]=IT.[Item ID] )AS T_cat
			WHERE  month([Order DT]) = month(@month) and 
				   year([Order DT]) = year(@year) 
			group by Category
			order by count(T_cat.Category) desc )
 
		RETURN  @L_top
			
	END


--Create view table (1 row) of january
--Data Row of each month = (num items this year , num items recent year , avg num last 5 years,
--sales rate this year,  sales rate last year,avg sales rate last 5 years,
--top category this year, top category last year, top category 2 years ago)

create view dbo.Data_Jan AS
SELECT 
		[period]='January',
	   [num items this year] = dbo.num_sales_per_month('2020-01-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-01-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-01-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-01-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-01-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-01-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-01-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-01-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-01-01','2018-01-01')

create view dbo.Data_Feb AS
SELECT 
		[period]='Febuary',
	   [num items this year] = dbo.num_sales_per_month('2020-02-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-02-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-02-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-02-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-02-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-02-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-02-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-02-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-02-01','2018-01-01')

create view dbo.Data_Mar AS
SELECT 
		[period]='March',
	   [num items this year] = dbo.num_sales_per_month('2020-03-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-03-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-03-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-03-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-03-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-03-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-03-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-03-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-03-01','2018-01-01')

create view dbo.Data_Apr AS
SELECT 
		[period]='April',
	   [num items this year] = dbo.num_sales_per_month('2020-04-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-04-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-04-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-04-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-04-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-04-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-04-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-04-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-04-01','2018-01-01')

create view dbo.Data_May AS
SELECT 
		[period]='May',
	   [num items this year] = dbo.num_sales_per_month('2020-05-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-05-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-05-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-05-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-05-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-05-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-05-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-05-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-05-01','2018-01-01')

create view dbo.Data_June AS
SELECT 
		[period]='June',
	   [num items this year] = dbo.num_sales_per_month('2020-06-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-06-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-06-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-06-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-06-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-06-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-06-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-06-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-06-01','2018-01-01')

create view dbo.Data_July AS
SELECT 
		[period]='July',
	   [num items this year] = dbo.num_sales_per_month('2020-07-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-07-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-07-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-07-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-07-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-07-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-07-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-07-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-07-01','2018-01-01')

create view dbo.Data_Aug AS
SELECT 
		[period]='August',
	   [num items this year] = dbo.num_sales_per_month('2020-08-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-08-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-08-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-08-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-08-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-08-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-08-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-08-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-08-01','2018-01-01')

create view dbo.Data_Sep AS
SELECT 
		[period]='September',
	   [num items this year] = dbo.num_sales_per_month('2020-09-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-09-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-09-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-09-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-09-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-09-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-09-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-09-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-09-01','2018-01-01')

create view dbo.Data_Oct AS
SELECT 
		[period]='October',
	   [num items this year] = dbo.num_sales_per_month('2020-10-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-10-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-10-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-10-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-10-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-10-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-10-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-10-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-10-01','2018-01-01')

create view dbo.Data_Nov AS
SELECT 
		[period]='November',
	   [num items this year] = dbo.num_sales_per_month('2020-11-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-11-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-11-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-11-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-11-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-11-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-11-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-11-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-11-01','2018-01-01')

create view dbo.Data_Dec AS
SELECT 
		[period]='December',
	   [num items this year] = dbo.num_sales_per_month('2020-12-01','2020-01-01','2020-01-01'),
	   [num items recent year] = dbo.num_sales_per_month('2020-12-01','2019-01-01','2019-01-01'),
	   [avg num last 5 years] = dbo.num_sales_per_month('2020-12-01','2015-01-01','2019-01-01'),
	   [sales rate this year] = dbo.monthly_rate('2020-12-01','2020-01-01','2020-01-01'),
	   [sales rate last year] = dbo.monthly_rate('2020-12-01','2019-01-01','2019-01-01'),
	   [avg sales rate last 5 years] =dbo.monthly_rate('2020-12-01','2015-01-01','2019-01-01'),
	   [top category this year] = dbo.top_category('2020-12-01','2020-01-01'), 
	   [top category last year] = dbo.top_category('2020-12-01','2019-01-01'), 
	   [top category 2 years ago] = dbo.top_category('2020-12-01','2018-01-01')

--Union of all complexed queries to one view
Create view dbo.Year_By_Month_Report as
		(select	 *	from dbo.Data_Jan
		UNION
		select	 *	from dbo.Data_Feb
		UNION
		select	 *	from dbo.Data_Mar
		UNION
		select	 *	from dbo.Data_Apr
		UNION
		select	 *	from dbo.Data_May
		UNION
		select	 *	from dbo.Data_June
		UNION
		select	 *	from dbo.Data_July
		UNION
		select	 *	from dbo.Data_Aug
		UNION
		select	 *	from dbo.Data_Sep
		UNION
		select	 *	from dbo.Data_Oct
		UNION
		select	 *	from dbo.Data_Nov
		UNION
		select	 *	from dbo.Data_Dec)

select * from dbo.Year_By_Month_Report
