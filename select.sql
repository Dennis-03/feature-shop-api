select team_name,feature_coins from 
(select fs_team.team_name, fs_tact_coins.feature_coins
 from fs_team inner join fs_tact_coins 
 on fs_team.fsteamid = fs_tact_coins.team_id 
 where fs_tact_coins.status = 'done') where team_name = 'alpha'; 