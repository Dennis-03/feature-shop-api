FS table:
	fs_user
		fsuid
		user_name
		email
		password
		location
		country
		registered_at
		updated_at
		
	fs_team
		fsteamid
		team_name
		added_at
		updated_at
	
	fs_team_members
		fstmid
		team_id
		member_id
		added_at
		
	fs_feature
		fsfeatureid
		title
		content
		created_by /fsteamid
		created_at
		updated_at
		
	fs_feature_holder (team who is holding the feature)
		fsfhid
		team_id
		feature_id
		added_at
		status
		
	fs_tact_coins
		fstcid
		team_id
		feature_id
		feature_coins
		status
		
	need to get:
		How much tact coins user-XYZ collected?
		How much tact coins team-ABC collected? - DONE
		How much do we owe to team-ABC which has to be released soon? - DONE
		Which team collected max coins in this week?
		
--------/


(select fs_team.team_name as Team , max(fs_tact_coins.feature_coins) as maximum from fs_team inner join fs_tact_coins on fs_team.fsteamid = fs_tact_coins.team_id where fs_tact_coins.status ='done');



Which team collected max coins in this week?
select fs_team.team_name as Team , max(fs_tact_coins.feature_coins) as Maximum from fs_team inner join fs_tact_coins on fs_team.fsteamid = fs_tact_coins.team_id where fs_tact_coins.status ='done' and fs_tact_coins.feature_id IN (select fs_feature_holder.feature_id as FeatureID from fs_feature_holder inner join fs_feature on fs_feature_holder.feature_id = fs_feature.fsfeatureid where fs_feature.updated_at between '14-08-2020' and '20-08-2020');


-----------------------------------------------------------------------------------------/
Joining 3 tables
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

-----------------------------------------------------------------------------------------/
Which team collected max coins in this week? - DONE

select team_id,sum(feature_coins) as fc from fs_tact_coins inner join fs_feature on fsfeatureid = feature_id where updated_at between '14-08-2020' and '20-08-2020'
group by team_id having status = 'done'  order by fc DESC;

------------------------------------------------------------------------------------------/

How much tact coins team-ABC collected?  - DONE

select fs_team.team_name as Team , fs_tact_coins.feature_coins as TotalAmount from fs_team inner join fs_tact_coins on fs_team.fsteamid = fs_tact_coins.team_id 
where fs_tact_coins.status = 'done';

select fs_team.team_name as Team , fs_tact_coins.feature_coins as TotalAmount from fs_team inner join fs_tact_coins on fs_team.fsteamid = fs_tact_coins.team_id 
where fs_tact_coins.status = 'done' and fs_tact_coins.feature_id IN 
(select fs_feature_holder.feature_id from fs_feature_holder where fs_feature_holder.status = 'Completed');

--------------------------------------------------------------------------------------------/

How much do we owe to team-ABC which has to be released soon? - DONE

select fs_team.team_name as Team , fs_tact_coins.feature_coins as TotalAmount from fs_team inner join fs_tact_coins on fs_team.fsteamid = fs_tact_coins.team_id 
where fs_tact_coins.status = 'pending' and fs_team.team_name = 'alpha' and fs_tact_coins.feature_id IN 
(select fs_feature_holder.feature_id from fs_feature_holder where fs_feature_holder.status = 'Completed');

---------------------------------------------------------------------------------------------/


How many features have been created in a particular period of time? -DONE

select count(fsfeatureid) as feature_count from fs_feature where created_at BETWEEN '12-08-2020' and '14-08-2020'

---------------------------------------------------------------------------------------------/

How many features have been created totally? 

select count(fsfeatureid) as feature_count from fs_feature

---------------------------------------------------------------------------------------------/

How many features have been completed by the corresponding teams?

select team_name,count(feature_id) as feature_count from fs_team inner join fs_feature_holder on fsteamid = team_id group by team_id having status = 'Completed' 

---------------------------------------------------------------------------------------------/

How many features have been completed by the a particular team?

select count(fs_feature_holder.feature_id) as feature_count from fs_team inner join fs_feature_holder on fs_team.fsteamid = fs_feature_holder.team_id group by fs_feature_holder.team_id having fs_feature_holder.status = 'Completed' and fs_team.team_name = 'mindfreakzz';

---------------------------------------------------------------------------------------------/

select max(sumTotal) from
(select fs_tact_coins.team_id as TeamID , sum(fs_tact_coins.feature_coins) as sumTotal from fs_tact_coins group by fs_tact_coins.team_id having fs_tact_coins.status = 'done');

---------------------------------------------------------------------------------------------/

Which team did the feature ?
select fs_team.team_name from fs_team inner join fs_feature on fs_team.fsteamid = fs_feature.created_by where fs_feature.title = 'mythraki';

---------------------------------------------------------------------------------------------/
How many tact coins did a feature get ?
select feature_coins from fs_tact_coins join fs_feature on fs_feature.fsfeatureid = fs_tact_coins.feature_id where title = 'soul recommender';
---------------------------------------------------------------------------------------------/


---------------------------------------------------------------------------------------------/


---------------------------------------------------------------------------------------------/



---------------------------------------------------------------------------------------------/


---------------------------------------------------------------------------------------------/